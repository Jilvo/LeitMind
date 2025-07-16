import boto3
from botocore.client import Config
from botocore.exceptions import ClientError, NoCredentialsError
from kink import di


class S3Storage:
    def __init__(self):
        """Initialize the S3 storage repository"""
        self.endpoint_url = di["S3_ENDPOINT_URL"]
        self.access_key = di["S3_ACCESS_KEY"]
        self.secret_key = di["S3_SECRET_KEY"]
        self.bucket_name = di["S3_BUCKET_NAME"]
        self.s3_client = boto3.client(
            "s3",
            endpoint_url=self.endpoint_url,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            config=Config(signature_version="s3v4"),
            region_name=di["S3_REGION"],
        )

    def upload_blob(self, file_content: bytes, destination_blob_name: str):
        """Upload blob to storage"""
        print(f"Uploading to {destination_blob_name} in bucket {self.bucket_name}")
        try:
            from io import BytesIO

            # Convertir le contenu en objet file-like
            file_obj = BytesIO(file_content)

            self.s3_client.upload_fileobj(
                file_obj,
                self.bucket_name,
                destination_blob_name,
                ExtraArgs={"ACL": "public-read"},
            )
            return f"{self.endpoint_url}/{self.bucket_name}/{destination_blob_name}"
            print(f"File uploaded to {destination_blob_name}.")
        except NoCredentialsError:
            raise Exception("S3 credentials not available")
        except ClientError as e:
            raise Exception(f"S3 upload failed: {e}")


# S3StorageRepository().upload_blob("lake.png", "test/lake.png")
