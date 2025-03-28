from domains.auth.interfaces.auth_repository_postgres import AuthRepository
from kink import inject


@inject
class GetUserUseCase:
    def __init__(
        self,
        auth_repository: AuthRepository,
    ):
        self.auth_repository = auth_repository

    def execute(
        self,
        user_info,
    ):
        # if user_info.get("username"):
        #     return self.auth_repository.get_user_by_username(user_info.get("username"))
        # elif user_info.get("email"):
        #     return self.auth_repository.get_user_by_email(user_info.get("email"))
        # else:
        #     return self.auth_repository.get_user_by_id(user_info.get("user_id"))
        if isinstance(
            user_info,
            int,
        ):
            user = self.auth_repository.get_user_by_id(user_info)
        return user.to_dict()

    def execute_all(
        self,
    ):
        return [user.to_dict() for user in self.auth_repository.get_all_users()]
    def get_user_by_email(
        self,
        email,
    ):
        return self.auth_repository.get_user_by_email(email)
