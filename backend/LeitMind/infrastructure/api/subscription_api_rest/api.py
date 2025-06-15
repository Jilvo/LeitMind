from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic
from kink import di

from domains.questions.models.subscription import UserSubscription
from domains.questions.schemas.subscription import (SubscriptionRequest,
                                                    SubscriptionUpdateRequest)
from domains.use_cases_services import UseCasesService
from utils.security import get_current_user

router = APIRouter()
di["subscription_api_router"] = router
security = HTTPBasic()


@router.post("/new_subscription/")
def create_subscription(
    subscription_data: SubscriptionRequest,
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Create a new subscription
    """

    service: UseCasesService = di[UseCasesService]
    service.manageSubscriptionUseCase.create_subscription(
        subscription_data,
        current_user,
    )
    return JSONResponse(
        status_code=201,
        content={"message": "Subscription created"},
    )


@router.get("/subscriptions/")
def get_all_subscriptions(
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Get all subscriptions
    """
    service: UseCasesService = di[UseCasesService]
    try:
        subscriptions = service.manageSubscriptionUseCase.get_all_subscriptions()
        return JSONResponse(
            status_code=200,
            content={
                "message": "List of subscriptions",
                "subscriptions": subscriptions,
            },
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": f"An error occurred while retrieving subscriptions: {str(e)}"},
        )


@router.get("/subscriptions/{subscription_id}")
def get_subscription_by_id(
    subscription_id: int,
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Get a subscription by ID
    """
    service: UseCasesService = di[UseCasesService]
    try:
        subscription = service.manageSubscriptionUseCase.get_subscription_by_id(subscription_id)
        return JSONResponse(
            status_code=200,
            content={
                "message": "Subscription retrieved",
                "subscription": subscription.to_dict(),
            },
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": f"An error occurred while retrieving the subscription: {str(e)}"},
        )


@router.put("/subscriptions/{subscription_id}")
def update_subscription(
    subscription_id: int,
    subscription_data: SubscriptionUpdateRequest,
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Update a subscription
    """
    service: UseCasesService = di[UseCasesService]
    try:
        service.manageSubscriptionUseCase.update_subscription(
            subscription_id,
            subscription_data,
            current_user,
        )
        return JSONResponse(
            status_code=200,
            content={"message": "Subscription updated"},
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": f"An error occurred while updating the subscription: {str(e)}"},
        )


@router.delete("/subscriptions/{subscription_id}")
def delete_subscription(
    subscription_id: str,
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Delete a subscription
    """
    service: UseCasesService = di[UseCasesService]
    try:
        service.manageSubscriptionUseCase.delete_subscription(subscription_id)
        return JSONResponse(
            status_code=200,
            content={"message": "Subscription deleted"},
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": f"An error occurred while deleting the subscription: {str(e)}"},
        )


@router.get("/subscriptions/user/{user_id}")
def get_subscription_by_user_id(
    user_id: int,
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Get a subscription by user ID
    """
    service: UseCasesService = di[UseCasesService]
    try:
        subscription = service.manageSubscriptionUseCase.get_subscription_by_user_id(user_id)
        if not subscription:
            return JSONResponse(
                status_code=404,
                content={"message": "Subscription not found"},
            )
        return JSONResponse(
            status_code=200,
            content={
                "message": "Subscription retrieved",
                "subscription": subscription,
            },
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": f"An error occurred while retrieving the subscription: {str(e)}"},
        )


@router.get("/subscriptions/count/{sub_category_id}")
def count_subscriptions_by_sub_category(
    sub_category_id: int,
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Count subscriptions by sub-category ID
    """
    service: UseCasesService = di[UseCasesService]
    try:
        result = service.manageSubscriptionUseCase.count_subscriptions_by_sub_category(sub_category_id)
        return JSONResponse(
            status_code=200,
            content={
                "sub_category_id": sub_category_id,
                "count": result["count"],
                "users": result["users"],
            },
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": f"An error occurred while counting subscriptions: {str(e)}"},
        )
