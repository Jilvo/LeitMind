from domains.auth.schemas.user import Token, UserCreationRequest, UserLoginRequest, UserUpdateRequest
from domains.use_cases_services import UseCasesService
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic
from kink import di
from utils.security import decode_access_token, get_current_user

router = APIRouter()
di["auth_api_router"] = router

security = HTTPBasic()


@router.get("/health")
def check_health():
    """
    Check the health of the Auth API.

    Returns:
        dict: A dictionary indicating that the Stockage API has successfully started.
    """
    return {"Stockage API successfully started!"}


@router.post("/users/")
def create_user(user_data: UserCreationRequest) -> JSONResponse:
    service: UseCasesService = di[UseCasesService]
    service.signUpUserUseCase.execute(user_data)
    return JSONResponse(status_code=201, content={"message": "User created"})


@router.get("/users/{user_id}")
def get_user(user_id: int) -> JSONResponse:
    service: UseCasesService = di[UseCasesService]
    user = service.getUserUseCase.execute(user_id)
    print(user)
    return JSONResponse(status_code=201, content={"message": user})


@router.post("/signup", response_model=Token)
def signup(user_data: UserCreationRequest) -> JSONResponse:
    service: UseCasesService = di[UseCasesService]
    user = service.auth_repository.signup(user_data)
    access_token = service.auth_repository.create_access_token(user)
    return JSONResponse(status_code=201, content={"access_token": access_token, "token_type": "bearer"})


@router.post("/login", response_model=Token)
def login(user_data: UserLoginRequest) -> JSONResponse:
    service: UseCasesService = di[UseCasesService]
    user = service.auth_repository.login(user_data.email, user_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = service.auth_repository.create_access_token(user)
    return JSONResponse(status_code=200, content={"access_token": access_token, "token_type": "bearer"})


@router.get("/users/")
def get_all_users(current_user: str = Depends(get_current_user)) -> JSONResponse:
    """
    Retourne une liste d'utilisateurs uniquement si un JWT valide est fourni.
    """
    return JSONResponse(status_code=200, content={"message": "List of users", "user": current_user})


@router.get("/users/me", response_model=None)
def get_current_user_info(token: str = Depends(get_current_user)) -> JSONResponse:
    """
    Retourne le contenu du JWT déchiffré sans appel en DB.
    """
    decoded_token = decode_access_token(token)
    return JSONResponse(status_code=200, content={"token_data": decoded_token})


@router.put("/users/{user_id}")
def update_user(user_data: UserUpdateRequest) -> JSONResponse:
    return JSONResponse(status_code=201, content={"message": "User updated"})


@router.delete("/users/{user_id}")
def delete_user(user_id: int) -> JSONResponse:
    return JSONResponse(status_code=201, content={"message": "User deleted"})


@router.get("/me", response_model=None)
def get_me(current_user: str = Depends(get_current_user)):
    """
    Retourne les informations de l'utilisateur connecté à partir du JWT.
    """
    return {"username": current_user}
