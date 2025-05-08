import pandas as pd
from domains.auth.interfaces.auth_repository_postgres import AuthRepository
from domains.auth.schemas.user import UserCreationRequest
from domains.questions.interfaces.subscription_repository_postgres import (
    SubscriptionRepository,
)
from domains.questions.models.subscription import UserSubscription
from domains.questions.schemas.subscription import (
    SubscriptionRequest,
    SubscriptionUpdateRequest,
)

from kink import inject
from pydantic import ValidationError


@inject
class ManageSubscriptionUseCase:
    def __init__(
        self,
        subscription_repository: SubscriptionRepository,
        auth_repository: AuthRepository,
    ):
        """
        Initializes a new use case for managing subscriptions.
        """
        self.subscription_repository = subscription_repository
        self.auth_repository = auth_repository

    def create_subscription(
        self,
        subscription_data: SubscriptionRequest,
        current_user: str,
       
    ) -> UserSubscription:
        """
        Create a new subscription.
        """
        try:
            user = self.auth_repository.get_user_by_email(current_user)
            # Validate the subscription data
            subscription = UserSubscription(
                user_id = user.id,
                sub_category_id = subscription_data.sub_category_id,
                
            )
            
            # Create the subscription
            return self.subscription_repository.create_subscription(subscription)
        except ValidationError as e:
            raise e
        except Exception as e:
            raise Exception(f"An error occurred while creating the subscription: {str(e)}")

    def get_all_subscriptions(
        self,
    ) -> list[dict]:
        """
        Get all subscriptions.
        """
        try:
           return self.subscription_repository.get_all_subscriptions()
        except Exception as e:
            raise Exception(f"An error occurred while retrieving subscriptions: {str(e)}")
        
    def get_subscription_by_id(
        self,
        subscription_id: str,
    ) -> UserSubscription:
        """
        Get a subscription by ID.
        """
        try:
            return self.subscription_repository.get_subscription_by_id(subscription_id)
        except Exception as e:
            raise Exception(f"An error occurred while retrieving the subscription: {str(e)}")
        
    def get_subscription_by_user_id(
        self,
        user_id: int,
        
    ) -> UserSubscription:
        """
        Get a subscription by user ID.
        """
        subscription = self.subscription_repository.get_subscription_by_user_id(user_id)
        if not subscription:
            raise Exception("Subscription not found")
        return subscription
    
    def count_subscriptions_by_sub_category(
        self,
        sub_category_id: int,
    ) -> int:
        """
        Count subscriptions by sub_category_id.
        """
        try:
            return self.subscription_repository.count_subscriptions_by_sub_category(sub_category_id)
        except Exception as e:
            raise Exception(f"An error occurred while counting subscriptions: {str(e)}")
    