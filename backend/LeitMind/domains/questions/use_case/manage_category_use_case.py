from domains.auth.interfaces.auth_repository_postgres import AuthRepository
from domains.questions.interfaces.questions_repository_postgres import QuestionsRepository
from kink import inject


@inject
class ManageCategoryUseCase:
    def __init__(self, questions_repository: QuestionsRepository, auth_repository: AuthRepository):
        self.questions_repository = questions_repository
        self.auth_repository = auth_repository

    def execute(self):
        pass
