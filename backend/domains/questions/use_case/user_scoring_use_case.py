from kink import inject

from commons.errors import UserNotFoundError
from domains.auth.interfaces.auth_repository_postgres import AuthRepository
from domains.questions.interfaces.questions_repository_postgres import QuestionsRepository
from domains.questions.interfaces.subscription_repository_postgres import \
    SubscriptionRepository
from domains.questions.models.subscription import UserSubscription
from domains.questions.use_case.manage_question_use_case import \
    ManageQuestionUseCase

@inject
class UserScoringUseCase:
    def __init__(
        self,
        subscription_repository: SubscriptionRepository,
        manage_question_use_case: ManageQuestionUseCase,
        auth_repository: AuthRepository,
        questions_repository: QuestionsRepository,
    ):
        """
        Initializes a new use case for managing subscriptions.
        """
        self.subscription_repository = subscription_repository
        self.auth_repository = auth_repository
        self.manage_question_use_case = manage_question_use_case
        self.questions_repository = questions_repository

    def get_user_scoring(self, current_user: str):
        """
        Get user scoring data.
        Responded questions, first try success rate, success after first retry, category subscribed, consecutive answer question streak.
        """
        user = self.auth_repository.get_user_by_email(current_user)
        if not user:
            raise UserNotFoundError(f"User with email {current_user} not found")
        
        # Get all user attempts
        attempts = self.questions_repository.get_all_attempts_by_user_id(user.id)
        
        # Get user subscriptions 
        subscriptions = self.questions_repository.get_subscriptions_by_user(user.id)
        active_categories = []
        for sub in subscriptions:
            active_categories.append(sub["category_name"])
        
        if not attempts:
            return {
                "responded_questions": 0,
                "first_try_success_rate": 0,
                "success_after_first_retry": 0,
                "category_subscribed": active_categories,
                "consecutive_answer_streak": 0,
                "global_streak": 0,
                "global_score": 0
            }
        
        # Calculate statistics
        total_questions = len(attempts)
        
        # First try success rate (attempt_count == 1 and is_correct == True)
        first_try_successes = len([a for a in attempts if a.attempt_count == 1 and a.is_correct])
        first_try_success_rate = round((first_try_successes / total_questions) * 100, 1) if total_questions > 0 else 0
        
        # Success after first retry (is_correct == True regardless of attempt_count)
        total_successes = len([a for a in attempts if a.is_correct])
        success_after_retry_rate = round((total_successes / total_questions) * 100, 1) if total_questions > 0 else 0
        
        # Calculate consecutive streak (most recent correct answers)
        consecutive_streak = self._calculate_consecutive_streak(attempts)
        
        # Calculate global streak (best streak ever)
        global_streak = self._calculate_global_streak(attempts)
        
        # Calculate global score (based on Leitner boxes and correct answers)
        global_score = self._calculate_global_score(attempts)
        
        return {
            "responded_questions": total_questions,
            "first_try_success_rate": first_try_success_rate,
            "success_after_first_retry": success_after_retry_rate,
            "category_subscribed": active_categories,
            "consecutive_answer_streak": consecutive_streak,
            "global_streak": global_streak,
            "global_score": global_score
        }
    
    def _calculate_consecutive_streak(self, attempts):
        """
        Calculate current consecutive correct answers streak.
        """
        if not attempts:
            return 0
        
        # Sort attempts by attempted_at descending (most recent first)
        sorted_attempts = sorted(attempts, key=lambda x: x.attempted_at, reverse=True)
        
        consecutive = 0
        for attempt in sorted_attempts:
            if attempt.is_correct:
                consecutive += 1
            else:
                break  # Streak broken
                
        return consecutive
    
    def _calculate_global_streak(self, attempts):
        """
        Calculate the best streak ever achieved.
        """
        if not attempts:
            return 0
        
        # Sort attempts by attempted_at ascending (chronological order)
        sorted_attempts = sorted(attempts, key=lambda x: x.attempted_at)
        
        max_streak = 0
        current_streak = 0
        
        for attempt in sorted_attempts:
            if attempt.is_correct:
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 0
                
        return max_streak
    
    def _calculate_global_score(self, attempts):
        """
        Calculate global score based on Leitner boxes and performance.
        """
        if not attempts:
            return 0
        
        score = 0
        for attempt in attempts:
            if attempt.is_correct:
                # Points based on Leitner box (higher box = more points)
                box_multiplier = attempt.leitner_box if attempt.leitner_box else 1
                
                # Bonus points for first try
                if attempt.attempt_count == 1:
                    score += box_multiplier * 2  # Double points for first try
                else:
                    score += box_multiplier  # Base points
                    
        return score