from datetime import datetime

from domains.auth.interfaces.auth_repository_postgres import AuthRepository
from domains.questions.interfaces.questions_repository_postgres import (
    QuestionsRepository,
)
from domains.questions.models.attempt import Attempt
from kink import inject


@inject
class SelectDailyQuestionsUseCase:
    def __init__(self, questions_repository: QuestionsRepository, auth_repository: AuthRepository):
        self.questions_repository = questions_repository
        self.auth_repository = auth_repository

    def execute(self, num_questions: int = 10):
        """
        Select daily questions for a user based on Leitner's system.
        """
        today = datetime.now()
        attempts: list[Attempt] = self.questions_repository.get_all_attempts_by_user_id(self.user_id)
        # not_correct_attempts = self.get_not_correct_user_attempts(attempts)
        outdated_attempts = self.get_outdated_attempts(attempts, today)

        # questions_to_review = list(
        #     set([a.question_id for a in not_correct_attempts + outdated_attempts])
        # )
        if len(outdated_attempts) > 0:
            questions_to_review = [a.question_id for a in outdated_attempts]
            questions = self.questions_repository.get_questions_by_ids(questions_to_review)
            # return questions
        if len(questions) >= 0 and len(questions) < 5:  # 15
            # new_questions = self.questions_repository.get_all_questions()
            pass
        elif len(questions) >= 5 and len(questions) < 10:  # 15
            pass
        elif len(questions) >= 10 and len(questions) < 15:  # 10
            pass
        elif len(questions) >= 15 and len(questions) < 20:  # 10
            pass
        elif len(questions) >= 20 and len(questions) < 25:  # 5
            pass
        elif len(questions) >= 25 and len(questions) < 30:  # 5
            pass
        else:
            pass
        # return []

    # def get_not_correct_user_attempts(self, attempts: list[Attempt]) -> list[Attempt]:
    #     """
    #     Get all not correct user attempts.
    #     """
    #     return [attempt for attempt in attempts if not attempt.is_correct]

    def get_outdated_attempts(self, attempts: list[Attempt], today) -> list[Attempt]:
        """
        Get all outdated attempts.
        """
        leitner_intervals = {1: 1, 2: 3, 3: 7, 4: 15, 5: 30}  # Days bettween revisions

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
