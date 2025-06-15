import boto3
from botocore.client import Config
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

    def upload_blob(self, source_file_name: str, destination_blob_name: str):
        """Upload blob to storage"""
        self.s3_client.upload_file(source_file_name, self.bucket_name, destination_blob_name)
        print(f"File {source_file_name} uploaded to {destination_blob_name}.")


# S3StorageRepository().upload_blob("lake.png", "test/lake.png")
