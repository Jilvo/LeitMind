from kink import inject

from domains.questions.interfaces.attempt_repository_postgres import \
    AttemptRepository


@inject
class ManageAttemptUseCase:
    def __init__(
        self,
        attempt_repository: AttemptRepository,
    ):
        self.attempt_repository = attempt_repository

    def execute(
        self,
    ):
        pass

    def get_all_attempts(
        self,
    ) -> list:
        return self.attempt_repository.get_all_attempts()

    def get_attempt_by_id(
        self,
        attempt_id: int,
    ):
        return self.attempt_repository.get_attempt_by_id(attempt_id)

    def create_attempt(
        self,
        attempt,
    ):
        return self.attempt_repository.create_attempt(attempt)

    def update_attempt(
        self,
        attempt,
    ):
        return self.attempt_repository.update_attempt(attempt)

    def delete_attempt(
        self,
        attempt_id: int,
    ):
        return self.attempt_repository.delete_attempt(attempt_id)

    def get_attempts_by_user_id(
        self,
        user_id: int,
    ) -> list:
        return self.attempt_repository.get_attempts_by_user_id(user_id)

    def get_attempts_by_question_id(
        self,
        question_id: int,
    ) -> list:
        return self.attempt_repository.get_attempts_by_question_id(question_id)
