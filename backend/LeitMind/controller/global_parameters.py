from commons.utils import getOrSet
from kink import di
try:
    print("loading controller (manage app initialization)")
    di["POSTGRES_DB_URL"] = getOrSet(
        "POSTGRES_DB_URL",
        "test",
    )
    print(
        "POSTGRES_DB_URL configuration",
        di["POSTGRES_DB_URL"],
    )
    di["S3_BUCKET_NAME"] = getOrSet(
        "S3_BUCKET_NAME",
        "test",
    )
    di["S3_ENDPOINT_URL"] = getOrSet(
        "S3_ENDPOINT_URL",
        "test",
    )
    di["S3_REGION"] = getOrSet(
        "S3_REGION",
        "test",
    )
    di["S3_ACCESS_KEY"] = getOrSet(
        "S3_ACCESS_KEY",
        "test",
    )
    di["S3_SECRET_KEY"] = getOrSet(
        "S3_SECRET_KEY",
        "test",
    )

    print("checking version...")

    print("commons settings")

except Exception as e:
    print(e)
    # log_service.display_logging_error(e=e)
    # raise Exception("Erreur lors de l'initialisation du controller")


def global_parameters():
    pass
