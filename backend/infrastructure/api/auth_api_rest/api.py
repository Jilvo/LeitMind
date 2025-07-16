import uuid

from commons.errors import UserAuthenticationError, UserNotFoundError
from domains.auth.models.user import User
from domains.auth.schemas.user import (Token, UserCreationRequest,
                                       UserLoginRequest, UserUpdateRequest)
from domains.use_cases_services import UseCasesService
from fastapi import (APIRouter, Depends, File, HTTPException, Request,
                     UploadFile, status)
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic
from infrastructure.spi.storage.s3_storage import S3Storage
from kink import di
from localization import translate
from starlette.requests import Request
from utils.security import decode_access_token, get_current_user

router = APIRouter()
di["auth_api_router"] = router

security = HTTPBasic()


@router.get("/health")
def check_health(
    request: Request,
) -> dict:
    """
    Check the health of the Auth API.

    Returns:
        dict: A dictionary indicating that the Stockage API has successfully started.
    """
    lang = request.state.lang
    return JSONResponse(
        status_code=200,
        content={"message": "Stockage API successfully started!", "lang": lang},
    )


@router.get(
    "/users/me",
    response_model=None,
)
def get_current_user_info(
    token: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Retourne le contenu du JWT déchiffré sans appel en DB.
    """
    try:
        decoded_token = decode_access_token(token)
        return JSONResponse(
            status_code=200,
            content={"token_data": decoded_token},
        )
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.get("/users/{user_id}")
def get_user(
    user_id: int,
) -> JSONResponse:
    service: UseCasesService = di[UseCasesService]
    try:
        user = service.getUserUseCase.execute(user_id)

        return JSONResponse(
            status_code=201,
            content={"message": user},
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to retrieve user: {str(e)}",
        )


@router.post(
    "/signup",
    response_model=Token,
)
def signup(
    user_data: UserCreationRequest,
) -> JSONResponse:
    service: UseCasesService = di[UseCasesService]
    try:
        user = service.authUserUseCase.signup(user_data)
        access_token = service.authUserUseCase.create_access_token(user)
        return JSONResponse(
            status_code=201,
            content={
                "access_token": access_token,
                "token_type": "bearer",
            },
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to sign up user: {str(e)}",
        )


@router.post(
    "/login",
    response_model=Token,
)
def login(
    user_data: UserLoginRequest,
    request: Request,
) -> JSONResponse:
    lang = request.state.lang
    try:
        service: UseCasesService = di[UseCasesService]
        user: User = service.authUserUseCase.login(
            user_data.email,
            user_data.password,
        )

        access_token = service.authUserUseCase.create_access_token(user)
        return JSONResponse(
            status_code=200,
            content={
                "access_token": access_token,
                "detail": "Login successful",
                "user": {
                    "user_id": str(user.id),
                    "username": user.username,
                    "email": user.email,
                    "country": user.country,
                },
                "token_type": "bearer",
            },
        )
    except UserNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "error": "user_not_found",
                "message": translate("user_not_found", lang),
            },
        )
    except UserAuthenticationError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={
                "error": "invalid_password",
                "message": translate("invalid_password", lang),
            },
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )


@router.get("/users/{user_id}/avatar")
def get_user_avatar(
    user_id: int,
) -> JSONResponse:
    service: UseCasesService = di[UseCasesService]
    try:
        avatar_url = service.getUserUseCase.get_avatar(user_id)
        return JSONResponse(
            status_code=200,
            content={"avatar_url": avatar_url},
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to retrieve user avatar: {str(e)}",
        )


@router.post("/users/{user_id}/avatar")
async def upload_user_avatar(
    user_id: int,
    avatar: UploadFile = File(...),
) -> JSONResponse:
    service: UseCasesService = di[UseCasesService]
    try:
        file_ext = avatar.filename.split(".")[-1]
        filename = f"leitmind/avatars/{user_id}.{file_ext}"
        # filename = f"leitmind/avatars/{uuid.uuid4()}.{file_ext}"
        content = await avatar.read()  # Ajouter await
        s3_storage = S3Storage()

        url = s3_storage.upload_blob(content, filename)
        user: User = service.updateUserUseCase.update_avatar(user_id, url)
        return JSONResponse(
            status_code=200,
            content={"avatar_url": user.avatar},
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to upload user avatar: {str(e)}",
        )


@router.get("/users/")
def get_all_users(
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Retourne une liste d'utilisateurs uniquement si un JWT valide est fourni.
    """
    service: UseCasesService = di[UseCasesService]

    try:

        users = service.getUserUseCase.execute_all()
        return JSONResponse(
            status_code=200,
            content={
                "message": "List of users",
                "user": users,
            },
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to retrieve users: {str(e)}",
        )


@router.put("/users/{user_id}")
def update_user(
    user_id: int,
    user_data: UserUpdateRequest,
) -> JSONResponse:
    service: UseCasesService = di[UseCasesService]
    try:
        update_user = service.updateUserUseCase.execute(user_id, user_data)

        return JSONResponse(
            status_code=200,
            content={"message": "User updated"},
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to update user: {str(e)}",
        )


@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
) -> JSONResponse:
    service: UseCasesService = di[UseCasesService]
    try:
        delete_user = service.deleteUserUseCase.execute(user_id)
        return JSONResponse(
            status_code=200,
            content={"message": "User deleted"},
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to delete user: {str(e)}",
        )


@router.get(
    "/me",
    response_model=None,
)
def get_me(
    current_user: str = Depends(get_current_user),
):
    """
    Retourne les informations de l'utilisateur connecté à partir du JWT.
    """
    return {"username": current_user}
