from kink import inject

from domains.auth.interfaces.auth_repository_postgres import AuthRepository
from domains.auth.schemas.user import UserUpdateRequest


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
        return self.auth_repository.update_user(
            user_id=user_id,
            username=user_data.username,
            email=user_data.email,
            country=user_data.country,
        )

    def update_avatar(
        self,
        user_id: int,
        avatar_url: str,
    ):
        """
        Update the user's avatar URL.
        """
        if not avatar_url:
            raise ValueError("Avatar URL cannot be empty")
        return self.auth_repository.update_user_avatar(
            user_id=user_id,
            avatar_url=avatar_url,
        )
