from domains.questions.models.attempt import Attempt


class AttemptRepository:
    def __init__(
        self,
    ):
        """
        Initializes a new repository for managing attempts.
        """
        pass

    # Attempts #
    def get_all_attempts(
        self,
    ) -> list[Attempt]:
        """
        Get all attempts.
        """
        pass

    def get_attempt_by_id(
        self,
        attempt_id: int,
    ) -> Attempt:
        """
        Get an attempt by ID.
        """
        pass

    def create_attempt(
        self,
        attempt: Attempt,
    ) -> Attempt:
        """
        Create a new attempt.
        """
        pass

    def update_attempt(
        self,
        attempt: Attempt,
    ) -> Attempt:
        """
        Update an attempt.
        """
        pass

    def delete_attempt(
        self,
        attempt_id: int,
    ):
        """
        Delete an attempt.
        """
        pass

    def get_attempts_by_user_id(
        self,
        user_id: int,
    ) -> list[Attempt]:
        """
        Get all attempts by user ID.
        """
        pass

    def get_attempts_by_question_id(
        self,
        question_id: int,
    ) -> list[Attempt]:
        """
        Get all attempts by question ID.
        """
        pass

    def count_attempts_by_user_and_question(
        self,
        user_id: int,
        question_id: int,
    ) -> int:
        """
        Count attempts by user ID and question ID.
        """
        pass


    def get_last_attempt_by_user_and_question(
        self,
        user_id: int,
        question_id: int,
    ) -> Attempt:
        """
        Get the last attempt by user ID and question ID.
        """
        pass

    