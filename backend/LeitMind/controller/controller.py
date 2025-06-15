from controller.global_parameters import global_parameters
from infrastructure.api.bootstrap import bootstrap as bootstrap_infrastructure
from infrastructure.spi.repository.bootstrap import \
    bootstrap as boostrap_repository
from infrastructure.spi.storage.bootstrap import bootstrap as bootstrap_storage

try:
    print("bootstraping dependencies for base services (logs,...)")
    global_parameters()
    bootstrap_infrastructure()
    boostrap_repository()
    bootstrap_storage()
except Exception as e:
    print(e)
    raise e


def controller():
    pass
