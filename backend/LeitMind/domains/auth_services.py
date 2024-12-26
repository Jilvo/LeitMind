from domains.auth.use_cases.create_user_use_case import CreateUserUseCase
from domains.auth.use_cases.delete_user_use_case import DeleteUserUseCase
from domains.auth.use_cases.get_user_use_case import GetUserUseCase
from domains.auth.use_cases.update_user_use_case import UpdateUserUseCase
from kink import di, inject


@inject
class AuthService:
    def __init__(self):
        self.createUserUseCase: CreateUserUseCase = di[CreateUserUseCase]
        self.deleteUserUseCase: DeleteUserUseCase = di[DeleteUserUseCase]
        self.getUserUseCase: GetUserUseCase = di[GetUserUseCase]
        self.updateUserUseCase: UpdateUserUseCase = di[UpdateUserUseCase]
