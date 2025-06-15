from kink import inject

from domains.auth.interfaces.auth_repository_postgres import AuthRepository


@inject
class DeleteUserUseCase:
    def __init__(
        self,
        auth_repository: AuthRepository,
    ):
        self.auth_repository = auth_repository

    def execute(
        self,
        user_id: int,
    ):
        return self.auth_repository.delete_user(user_id)
