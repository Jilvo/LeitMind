from domains.questions.schemas.question import CategoryRequest
from domains.use_cases_services import UseCasesService
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic
from infrastructure.spi.repository.dependencies import get_db
from kink import di
from sqlalchemy.orm import Session
from utils.security import get_current_user

router = APIRouter()
di["category_api_router"] = router

security = HTTPBasic()


# Category
@router.get("/categories/")
def get_all_categories(current_user: str = Depends(get_current_user)) -> JSONResponse:
    """
    Get all categories
    """
    service: UseCasesService = di[UseCasesService]
    categories = service.manageQuestionUseCase.get_all_categories()
    return JSONResponse(status_code=200, content={"categories": categories})


@router.post("/new_category/")
def create_new_category(category_request: CategoryRequest, current_user: str = Depends(get_current_user)) -> JSONResponse:
    """
    Create a new category
    """
    service: UseCasesService = di[UseCasesService]
    service.manageQuestionUseCase.create_category(category_request)
    return JSONResponse(status_code=201, content={"message": "Category created"})


@router.delete("/categories/{category_id}")
def delete_category(category_id: int, current_user: str = Depends(get_current_user)) -> JSONResponse:
    """
    Delete a category
    """
    service: UseCasesService = di[UseCasesService]
    service.manageQuestionUseCase.delete_category(category_id)
    return JSONResponse(status_code=201, content={"message": "Category deleted"})


@router.put("/categories/{category_id}")
def update_category(
    category_id: int,
    category_name: str,
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Update a category
    """
    service: UseCasesService = di[UseCasesService]
    service.manageQuestionUseCase.update_category(category_id, category_name)
    return JSONResponse(status_code=201, content={"message": "Category updated"})


@router.get("/categories/{category_id}")
def get_category_by_id(category_id: int, current_user: str = Depends(get_current_user)) -> JSONResponse:
    """
    Get a category by ID
    """
    service: UseCasesService = di[UseCasesService]
    category = service.manageQuestionUseCase.get_category_by_id(category_id)
    return JSONResponse(status_code=201, content={"message": category})


# Subscriptions to Categories and Sub-Categories


@router.post("/subscribe")
def subscribe_to_category_or_sub_category(
    category_id: int = None,
    sub_category_id: int = None,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Subscribe a user to a category or sub-category.
    """
    # service: UseCasesService = di[UseCasesService]
    # subscription = repo.add_subscription(
    #     user_id=current_user.id,
    #     category_id=category_id,
    #     sub_category_id=sub_category_id,
    # )
    return {"message": "Subscribed successfully", "subscription": "subscription"}


@router.get("/subscriptions")
def get_user_subscriptions(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """
    Returns the subscriptions of the logged in user.
    """
    # service: UseCasesService = di[UseCasesService]
    # subscriptions = repo.get_subscriptions_by_user(current_user.id)
    return {"subscriptions": "subscriptions"}


@router.delete("/unsubscribe")
def unsubscribe_from_category_or_sub_category(
    category_id: int = None,
    sub_category_id: int = None,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Unsubscribe a user from a category or sub-category.
    """
    # repo = UserSubscriptionRepository(db)
    # success = repo.remove_subscription(
    #     user_id=current_user.id,
    #     category_id=category_id,
    #     sub_category_id=sub_category_id,
    # )
    # if success:
    #     return {"message": "Unsubscribed successfully"}
    return {"message": "Subscription not found"}
