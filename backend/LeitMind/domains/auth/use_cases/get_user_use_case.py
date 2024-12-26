from domains.auth.interfaces.auth_repository_postgres import AuthRepository


class GetUserUseCase:
    def __init__(self, user_repository: AuthRepository):
        self.user_repository = user_repository

    def execute(self, user_id: int):
        return self.user_repository.get_user_by_id(user_id)
