from commons.utils import getOrSet
from kink import di

try:
    print("loading controller (manage app initialization)")
    di["POSTGRES_DB_URL"] = getOrSet("POSTGRES_DB_URL", "test")
    print("POSTGRES_DB_URL configuration", di["POSTGRES_DB_URL"])
    print("checking version...")

    print("commons settings")

except Exception as e:
    print(e)
    # log_service.display_logging_error(e=e)
    # raise Exception("Erreur lors de l'initialisation du controller")


def global_parameters():
    pass
