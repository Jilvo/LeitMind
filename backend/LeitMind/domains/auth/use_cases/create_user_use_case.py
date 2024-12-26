from domains.auth.interfaces.auth_repository_postgres import AuthRepository


class CreateUserUseCase:
    def __init__(self, user_repository: AuthRepository):
        self.user_repository = user_repository

    def execute(self, username: str, email: str, hashed_password: str, country: str):
        # Logique métier (si nécessaire)
        return self.user_repository.create_user(username, email, hashed_password, country)
