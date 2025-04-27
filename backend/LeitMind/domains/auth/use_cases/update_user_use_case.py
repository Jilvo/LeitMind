from domains.auth.interfaces.auth_repository_postgres import AuthRepository
from domains.auth.schemas.user import UserUpdateRequest
from kink import inject


@inject
class UpdateUserUseCase:
    def __init__(
        self,
        auth_repository: AuthRepository,
    ):
        self.auth_repository = auth_repository

    def execute(
        self,
        user_id: int,
        user_data: UserUpdateRequest,
    ):
        return self.auth_repository.update_user(user_id=user_id,
        username=user_data.username,
        email=user_data.email,
        country=user_data.country)
