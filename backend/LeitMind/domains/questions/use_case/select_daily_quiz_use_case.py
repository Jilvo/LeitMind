from datetime import datetime

from kink import inject

from domains.auth.interfaces.auth_repository_postgres import AuthRepository
from domains.questions.interfaces.questions_repository_postgres import \
    QuestionsRepository
from domains.questions.models.attempt import Attempt


@inject
class SelectDailyQuestionsUseCase:
    def __init__(
        self,
        questions_repository: QuestionsRepository,
        auth_repository: AuthRepository,
        # user_id: int,
    ):
        self.questions_repository = questions_repository
        self.auth_repository = auth_repository

    def execute(
        self,
        current_user: str,
    ):
        """
        Select daily questions for a user based on Leitner's system.
        """
        try:
            today = datetime.now()
            user = self.auth_repository.get_user_by_email(current_user)
            if not user:
                raise ValueError(f"User with email {current_user} not found")
            attempts: list[Attempt] = self.questions_repository.get_all_attempts_by_user_id(user.id)
            # not_correct_attempts = self.get_not_correct_user_attempts(attempts)
            outdated_attempts = self.get_outdated_attempts(
                attempts,
                today,
            )
            list_id_sub_categories = self.questions_repository.get_subscriptions_by_user(user.id)
            if not list_id_sub_categories:
                return []
            questions_to_review = []
            if outdated_attempts:
                questions_to_review = [a.question_id for a in outdated_attempts]
                questions = self.questions_repository.get_questions_by_ids(questions_to_review)
            else:
                questions = []

            length = len(questions)
            if length < 10:
                needed = 15
            elif length < 20:
                needed = 10
            elif length < 30:
                needed = 5
            else:
                needed = 0

            new_questions = []
            if needed:
                new_questions = self.questions_repository.get_unattempted_questions_by_user_id_and_subscribed_sub_categories(
                    user_id=user.id,
                    list_id_sub_categories=list_id_sub_categories,
                    count=needed,
                )

            list_of_daily_questions = questions + new_questions
            if list_of_daily_questions:
                return list_of_daily_questions
            else:
                return []
        except Exception as e:
            print(f"Error in execute: {str(e)}")
            raise ValueError(f"Unable to retrieve daily questions: {str(e)}")

    def get_outdated_attempts(
        self,
        attempts: list[Attempt],
        today,
    ) -> list[Attempt]:
        """
        Get all outdated attempts.
        """
        leitner_intervals = {
            1: 1,
            2: 3,
            3: 7,
            4: 15,
            5: 30,
        }  # Days bettween revisions

        outdated_attempts = []
        for attempt in attempts:
            last_attempt_date = attempt.timestamp.date()
            days_since_last_attempt = (today.date() - last_attempt_date).days

            # Vérifie si la question doit être révisée
            if attempt.leitner_box in leitner_intervals:
                interval = leitner_intervals[attempt.leitner_box]
                if days_since_last_attempt >= interval:
                    outdated_attempts.append(attempt)

        return outdated_attempts
