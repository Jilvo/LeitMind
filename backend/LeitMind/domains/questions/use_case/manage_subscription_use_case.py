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
       
    ) -> UserSubscription:
        """
        Create a new subscription.
        """
        try:
            # Validate the subscription data
            subscription = UserSubscription(**subscription_data.dict())
            
            # Create the subscription
            return self.subscription_repository.create_subscription(subscription)
        except ValidationError as e:
            raise e
        except Exception as e:
            raise Exception(f"An error occurred while creating the subscription: {str(e)}")

    def get_all_subscriptions(
        self,
    ) -> pd.DataFrame:
        """
        Get all subscriptions.
        """
        try:
            # Get all subscriptions
            subscriptions = self.subscription_repository.get_all_subscriptions()
            # Convert to DataFrame
            return pd.DataFrame([subscription.dict() for subscription in subscriptions])
        except Exception as e:
            raise Exception(f"An error occurred while retrieving subscriptions: {str(e)}")