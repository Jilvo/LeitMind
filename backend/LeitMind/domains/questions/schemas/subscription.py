from pydantic import BaseModel

class SubscriptionRequest(BaseModel):
    """
    Schema for creating a new subscription.
    """
    user_id: int
    sub_category_id: int

class SubscriptionUpdateRequest(BaseModel):
    """
    Schema for updating an existing subscription.
    """
   
    user_id: int
    sub_category_id: int
    active: bool

class SubscriptionResponse(BaseModel):
    """
    Schema for the response of a subscription.
    """
   
    user_id: int
    sub_category_id: int
    active: bool

