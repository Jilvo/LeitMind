from domains.auth_services import AuthService
from fastapi import APIRouter
from fastapi.responses import JSONResponse
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


@router.post("/users/")
def create_user_endpoint(
    username: str,
    email: str,
    hashed_password: str,
    country: str,
) -> JSONResponse:
    service: AuthService = di[AuthService]
    service.createUserUseCase.execute(username, email, hashed_password, country)
    return JSONResponse(status_code=201, content={"message": "User created"})


@router.get("/users/{user_id}")
def get_user_endpoint(user_id: int) -> JSONResponse:
    return JSONResponse(status_code=201, content={"message": "User created"})


@router.get("/users/")
def get_all_users_endpoint() -> JSONResponse:
    return JSONResponse(status_code=201, content={"message": "User"})


@router.put("/users/{user_id}")
def update_user_endpoint(
    user_id: int,
    username: str = None,
    email: str = None,
    country: str = None,
) -> JSONResponse:
    return JSONResponse(status_code=201, content={"message": "User updated"})


@router.delete("/users/{user_id}")
def delete_user_endpoint(user_id: int) -> JSONResponse:
    return JSONResponse(status_code=201, content={"message": "User deleted"})
