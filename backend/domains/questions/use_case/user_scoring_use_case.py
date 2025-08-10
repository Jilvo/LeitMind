from kink import inject

from domains.auth.interfaces.auth_repository_postgres import AuthRepository
from domains.questions.interfaces.subscription_repository_postgres import \
    SubscriptionRepository
from domains.questions.use_case.manage_question_use_case import \
    ManageQuestionUseCase

@inject
class UserScoringUseCase:
    def __init__(
        self,
        subscription_repository: SubscriptionRepository,
        manage_question_use_case: ManageQuestionUseCase,
        auth_repository: AuthRepository,
    ):
        """
        Initializes a new use case for managing subscriptions.
        """
        self.subscription_repository = subscription_repository
        self.auth_repository = auth_repository
        self.manage_question_use_case = manage_question_use_case

    def execute(self):
        """
        Get user scoring data.
        Responded questions, first try success rate, success after first retry, category subscribed, consecutive answer question streak.
        """
        