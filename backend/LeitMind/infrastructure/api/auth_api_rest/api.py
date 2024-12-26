from fastapi import APIRouter
from kink import di

router = APIRouter()
di["auth_api_router"] = router


@router.get("/health")
def check_health():
    """
    Check the health of the Auth API.

    Returns:
        dict: A dictionary indicating that the Stockage API has successfully started.
    """
    return {"Stockage API successfully started!"}
