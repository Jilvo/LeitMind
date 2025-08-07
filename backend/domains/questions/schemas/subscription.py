from pydantic import BaseModel


class SubscriptionRequest(BaseModel):
    """
    Schema for creating a category subscription.
    """

    category_name: str
    subscribed: bool


class SubscriptionUserUpdateRequest(BaseModel):
    """
    Schema for updating a subscription by user ID.
    """

    subscriptions: list[SubscriptionRequest]


class SubscriptionResponse(BaseModel):
    """
    Schema for the response of a subscription.
    """

    user_id: int
    category_name: str
    active: bool
