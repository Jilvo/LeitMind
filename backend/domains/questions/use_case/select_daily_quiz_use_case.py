from datetime import datetime, timedelta

from kink import inject

from commons.errors import UserNotFoundError, SessionIntervalError, NoSubscriptionError, DailyQuestionsError
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
        Select daily questions for a user based on enhanced Leitner's system.
        Maximum 25 questions per session with intelligent distribution.
        """
        now = datetime.now()
        user = self.auth_repository.get_user_by_email(current_user)
        if not user:
            raise UserNotFoundError(f"User with email {current_user} not found")
        
        # Check if enough time has passed since last session (4 hours minimum)
        last_session = self.get_last_session_time(user.id)
        if last_session and (now - last_session).total_seconds() < 4 * 3600:  # 4 hours
            next_available = last_session + timedelta(hours=4)
            raise SessionIntervalError(f"Session minimum interval not reached. Next session available at {next_available.strftime('%H:%M')}")

        attempts: list[Attempt] = self.questions_repository.get_all_attempts_by_user_id(user.id)
        list_categories = self.questions_repository.get_subscriptions_by_user(user.id)
        list_id_categories = [c["category_id"] for c in list_categories if c["is_active"] == 1]
        
        if not list_categories:
            raise NoSubscriptionError("You have not yet subscribed to any categories. Please subscribe to at least one category to receive personalized questions.")

        try:
            # Categorize questions by urgency and type
            urgent_review = self.get_urgent_review_questions(attempts, now)
            regular_review = self.get_regular_review_questions(attempts, now)
            maintenance_questions = self.get_maintenance_questions(attempts, now)
            
            # Calculate optimal distribution for 25 questions max
            distribution = self.calculate_question_distribution(
                len(urgent_review), 
                len(regular_review), 
                len(maintenance_questions)
            )
            
            # Select questions based on distribution and priority
            selected_questions = []
            
            # 1. Priority: Urgent reviews (overdue questions)
            selected_urgent = self.prioritize_urgent_questions(urgent_review, distribution['urgent'])
            selected_questions.extend(selected_urgent)
            
            # 2. Regular reviews (due questions)
            selected_regular = self.prioritize_regular_questions(regular_review, distribution['review'])
            selected_questions.extend(selected_regular)
            
            # 3. Maintenance questions (well-known questions)
            selected_maintenance = self.prioritize_maintenance_questions(maintenance_questions, distribution['maintenance'])
            selected_questions.extend(selected_maintenance)
            
            # 4. New questions to fill remaining slots
            remaining_slots = 25 - len(selected_questions)
            new_questions = []
            if remaining_slots > 0:
                new_questions = self.questions_repository.get_unattempted_questions_by_user_id_and_subscribed_categories(
                    user_id=user.id,
                    list_id_categories=list_id_categories,
                    count=min(remaining_slots, distribution['new']),
                )
            
            # Get question objects
            all_question_ids = [q.question_id for q in selected_questions]
            questions_from_attempts = self.questions_repository.get_questions_by_ids(all_question_ids)
            all_questions = list(questions_from_attempts) + list(new_questions)
            
            # Randomize order to avoid predictable patterns
            import random
            random.shuffle(all_questions)

            return {
                "daily_questions": [q.to_dict() for q in all_questions],
                "total_questions": len(all_questions),
                "review_questions": len(selected_urgent) + len(selected_regular),
                "new_questions": len(new_questions),
                "maintenance_questions": len(selected_maintenance),
                "urgent_questions": len(selected_urgent),
                "user_id": user.id,
                "categories_subscribed": list_id_categories,
                "distribution_used": distribution
            }
        except (UserNotFoundError, SessionIntervalError, NoSubscriptionError):
            # Re-raise specific exceptions
            raise
        except Exception as e:
            print(f"Error in execute: {str(e)}")
            raise DailyQuestionsError(f"Unable to retrieve daily questions due to technical error: {str(e)}")

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
            last_attempt_date = attempt.attempted_at.date()
            days_since_last_attempt = (today.date() - last_attempt_date).days

            # Vérifie si la question doit être révisée
            if attempt.leitner_box in leitner_intervals:
                interval = leitner_intervals[attempt.leitner_box]
                if days_since_last_attempt >= interval:
                    outdated_attempts.append(attempt)

        return outdated_attempts

    def get_last_session_time(self, user_id: int) -> datetime:
        """
        Get the timestamp of the user's last session.
        This would typically query a sessions table or user activity log.
        For now, we'll use the most recent attempt as a proxy.
        """
        attempts = self.questions_repository.get_all_attempts_by_user_id(user_id)
        if not attempts:
            return None
        
        # Get the most recent attempt
        latest_attempt: Attempt = max(attempts, key=lambda x: x.attempted_at)
        return latest_attempt.attempted_at

    def get_urgent_review_questions(self, attempts: list[Attempt], now: datetime) -> list[Attempt]:
        """
        Get questions that are overdue for review (urgent priority).
        """
        leitner_intervals = {1: 1, 2: 3, 3: 7, 4: 15, 5: 30}
        urgent_attempts = []
        
        for attempt in attempts:
            days_since = (now.date() - attempt.attempted_at.date()).days
            interval = leitner_intervals.get(attempt.leitner_box, 30)
            
            # Urgent if overdue by more than 1 day
            if days_since > interval + 1:
                urgent_attempts.append(attempt)
        
        return urgent_attempts

    def get_regular_review_questions(self, attempts: list[Attempt], now: datetime) -> list[Attempt]:
        """
        Get questions that are due for review (normal priority).
        """
        leitner_intervals = {1: 1, 2: 3, 3: 7, 4: 15, 5: 30}
        regular_attempts = []
        
        for attempt in attempts:
            days_since = (now.date() - attempt.attempted_at.date()).days
            interval = leitner_intervals.get(attempt.leitner_box, 30)
            
            # Due today or within 1 day
            if interval <= days_since <= interval + 1:
                regular_attempts.append(attempt)
        
        return regular_attempts

    def get_maintenance_questions(self, attempts: list[Attempt], now: datetime) -> list[Attempt]:
        """
        Get well-mastered questions for maintenance (box 4-5 that are not due yet).
        """
        maintenance_attempts = []
        
        for attempt in attempts:
            # Only consider well-mastered questions (box 4-5)
            if attempt.leitner_box >= 4:
                days_since = (now.date() - attempt.attempted_at.date()).days
                interval = 15 if attempt.leitner_box == 4 else 30
                
                # Not due yet but available for maintenance
                if days_since < interval:
                    maintenance_attempts.append(attempt)
        
        return maintenance_attempts

    def calculate_question_distribution(self, urgent_count: int, review_count: int, maintenance_count: int) -> dict:
        """
        Calculate optimal distribution of 25 questions based on available questions.
        Target: 5-10 new, 8-12 review, 3-7 maintenance
        """
        total_available = urgent_count + review_count + maintenance_count
        
        if total_available >= 25:
            # We have enough questions, use target distribution
            return {
                'urgent': min(urgent_count, 8),  # Prioritize urgent
                'review': min(review_count, 8),
                'maintenance': min(maintenance_count, 4),
                'new': 5  # Fill remaining with new questions
            }
        else:
            # Adapt distribution based on available questions
            urgent_take = min(urgent_count, 12)  # Take more urgent if available
            review_take = min(review_count, max(0, 15 - urgent_take))
            maintenance_take = min(maintenance_count, max(0, 20 - urgent_take - review_take))
            new_take = max(0, 25 - urgent_take - review_take - maintenance_take)
            
            return {
                'urgent': urgent_take,
                'review': review_take,
                'maintenance': maintenance_take,
                'new': new_take
            }

    def prioritize_urgent_questions(self, urgent_attempts: list[Attempt], count: int) -> list[Attempt]:
        """
        Prioritize urgent questions by how overdue they are and difficulty.
        """
        if not urgent_attempts or count <= 0:
            return []
        
        # Sort by days overdue (descending) and then by leitner_box (ascending for harder questions first)
        now = datetime.now()
        leitner_intervals = {1: 1, 2: 3, 3: 7, 4: 15, 5: 30}

        def urgency_score(attempt: Attempt):
            days_since = (now.date() - attempt.attempted_at.date()).days
            interval = leitner_intervals.get(attempt.leitner_box, 30)
            overdue_days = days_since - interval
            return (overdue_days, -attempt.leitner_box)  # More overdue first, then harder questions
        
        sorted_attempts = sorted(urgent_attempts, key=urgency_score, reverse=True)
        return sorted_attempts[:count]

    def prioritize_regular_questions(self, review_attempts: list[Attempt], count: int) -> list[Attempt]:
        """
        Prioritize regular review questions by difficulty and last performance.
        """
        if not review_attempts or count <= 0:
            return []
        
        # Sort by leitner_box (ascending - harder questions first) and then by last attempt date
        def priority_score(attempt: Attempt):
            return (attempt.leitner_box, attempt.attempted_at)
        
        sorted_attempts = sorted(review_attempts, key=priority_score)
        return sorted_attempts[:count]

    def prioritize_maintenance_questions(self, maintenance_attempts: list[Attempt], count: int) -> list[Attempt]:
        """
        Prioritize maintenance questions randomly to avoid predictable patterns.
        """
        if not maintenance_attempts or count <= 0:
            return []
        
        import random
        shuffled = maintenance_attempts.copy()
        random.shuffle(shuffled)
        return shuffled[:count]
