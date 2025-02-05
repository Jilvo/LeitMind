from domains.auth.interfaces.auth_repository_postgres import (
    AuthRepository,
)
from domains.auth.models.user import (
    User,
)
from domains.auth.schemas.user import (
    UserCreationRequest,
)
from kink import (
    inject,
)
from pydantic import (
    ValidationError,
)
from utils.security import (
    get_password_hash,
)


@inject
class SignUpUserUseCase:
    def __init__(
        self,
        auth_repository: AuthRepository,
    ):
        self.auth_repository = auth_repository

    def execute(
        self,
        user_data: UserCreationRequest,
    ):
        # Logique métier (si nécessaire)
        try:
            user_data = UserCreationRequest(**user_data.model_dump())
            hashed_password = get_password_hash(user_data.password)
            user = User(
                username=user_data.username,
                email=user_data.email,
                hashed_password=hashed_password,
                country=user_data.country,
            )
        except ValidationError as e:
            raise ValueError(f"Invalid data: {e}")
        return self.auth_repository.create_user(user)
