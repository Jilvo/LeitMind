from typing import (
    List,
)

from domains.auth.models.user import (
    User,
)


class AuthRepository:
    def __init__(
        self,
    ):
        """
        Initializes a new repository for managing prompts.
        """
        pass

    def create_user(
        self,
        user: User,
    ) -> User:
        pass

    def get_user_by_id(
        self,
        user_id: int,
    ) -> User:
        pass

    def get_all_users(
        self,
    ) -> List[User]:
        pass

    def update_user(
        self,
        user_id: int,
        username: str,
        email: str,
        country: str,
    ) -> User:
        pass

    def delete_user(
        self,
        user_id: int,
    ):
        pass

    def get_user_by_email(
        self,
        email: str,
    ) -> User:
        pass

    def get_user_by_username(
        self,
        username: str,
    ) -> User:
        pass

    def authenticate_user(
        self,
        username: str,
        password: str,
    ) -> User:
        pass
