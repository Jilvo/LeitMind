from domains.auth.interfaces.auth_repository_postgres import (
    AuthRepository,
)
from domains.questions.interfaces.questions_repository_postgres import (
    QuestionsRepository,
)
from kink import (
    inject,
)


@inject
class ManageCategoryUseCase:
    def __init__(
        self,
        questions_repository: QuestionsRepository,
        auth_repository: AuthRepository,
    ):
        self.questions_repository = questions_repository
        self.auth_repository = auth_repository

    def execute(
        self,
    ):
        pass

    def subscribe_to_category_or_sub_category(
        self,
        category_id: int,
        sub_category_id: int,
        user_id: int,
    ):
        if category_id:
            self.questions_repository.subscribe_to_category(
                category_id,
                user_id,
            )
        elif sub_category_id:
            self.questions_repository.subscribe_to_sub_category(
                sub_category_id,
                user_id,
            )
        else:
            raise ValueError("category_id or sub_category_id must be provided")

    def get_subscriptions_by_user(
        self,
        user_id: int,
    ):
        return self.questions_repository.get_subscriptions_by_user(user_id)

    def remove_subscription(
        self,
        category_id: int,
        sub_category_id: int,
        user_id: int,
    ):
        if category_id:
            self.questions_repository.unsubscribe_from_category(
                category_id,
                user_id,
            )
            return True
        elif sub_category_id:
            self.questions_repository.unsubscribe_from_sub_category(
                sub_category_id,
                user_id,
            )
            return True
        else:
            raise ValueError("category_id or sub_category_id must be provided")
