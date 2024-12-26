from kink import di
from commons.utils import getOrSet


try:
    print("loading controller (manage app initialization)")
    di["MONGO_STOCKAGE_DB_URL"] = getOrSet("MONGO_STOCKAGE_DB_URL", "test")
    print("MONGO_STOCKAGE_DB_URL configuration", di["MONGO_STOCKAGE_DB_URL"])
    print("checking version...")

    print("commons settings")

except Exception as e:
    print(e)
    # log_service.display_logging_error(e=e)
    # raise Exception("Erreur lors de l'initialisation du controller")


def global_parameters():
    pass
