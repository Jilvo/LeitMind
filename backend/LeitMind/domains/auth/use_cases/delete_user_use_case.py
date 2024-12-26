from domains.auth.interfaces.auth_repository_postgres import AuthRepository


class DeleteUserUseCase:
    def __init__(self, user_repository: AuthRepository):
        self.user_repository = user_repository

    def execute(self, user_id: int):
        return self.user_repository.delete_user(user_id)
