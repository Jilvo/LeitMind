from domains.questions.models.subscription import UserSubscription


class SubscriptionRepository:
    def __init__(
        self,
    ):
        """
        Initializes a new repository for managing subscriptions.
        """
        pass

    def get_all_subscriptions(
        self,
    ) -> list[UserSubscription]:
        """
        Get all subscriptions.
        """
        pass

    def get_subscription_by_id(
        self,
        subscription_id: str,
    ) -> UserSubscription:
        """
        Get a subscription by ID.
        """
        pass

    def create_subscription(
        self,
        subscription: UserSubscription,
    ) -> UserSubscription:
        """
        Create a new subscription.
        """
        pass

    def update_subscription(
        self,
        subscription: UserSubscription,
    ) -> UserSubscription:
        """
        Update a subscription.
        """
        pass

    def delete_subscription(
        self,
        subscription_id: str,
    ):
        """
        Delete a subscription.
        """
        pass

    def get_subscriptions_by_user_id(
        self,
        user_id: str,
    ) -> UserSubscription:
        """
        Get a subscription by user ID.
        """
        pass

    def count_subscriptions_by_sub_category(
        self,
        sub_category_id: str,
    ) -> int:
        """
        Count subscriptions by sub-category ID.
        """
        pass
    
    def get_subscription_by_user_and_category(
        self,
        user_id: int,
        category_id: int,
    ) -> UserSubscription:
        """
        Get a subscription by user ID and category ID.
        """
        pass

    def update_subscription_by_id(
        self,
        subscription_id: str,
        subscription_data: UserSubscription,
    ) -> UserSubscription:
        """
        Update subscriptions by user ID.
        """
        pass