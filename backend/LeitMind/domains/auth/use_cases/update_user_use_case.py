from domains.auth.interfaces.auth_repository_postgres import AuthRepository


class UpdateUserUseCase:
    def __init__(self, user_repository: AuthRepository):
        self.user_repository = user_repository

    def execute(self, user_id: int, username: str = None, email: str = None, country: str = None):
        return self.user_repository.update_user(user_id, username, email, country)
