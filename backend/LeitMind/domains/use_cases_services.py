from domains.auth.use_cases.auth_user_use_case import AuthUserUseCase
from domains.auth.use_cases.delete_user_use_case import DeleteUserUseCase
from domains.auth.use_cases.get_user_use_case import GetUserUseCase
from domains.auth.use_cases.update_user_use_case import UpdateUserUseCase
from domains.questions.use_case.manage_question_use_case import ManageQuestionUseCase
from kink import di, inject


@inject
class UseCasesService:
    def __init__(self):
        self.deleteUserUseCase: DeleteUserUseCase = di[DeleteUserUseCase]
        self.getUserUseCase: GetUserUseCase = di[GetUserUseCase]
        self.updateUserUseCase: UpdateUserUseCase = di[UpdateUserUseCase]
        self.auth_repository: AuthUserUseCase = di[AuthUserUseCase]

        self.manageQuestionUseCase: ManageQuestionUseCase = di[ManageQuestionUseCase]
