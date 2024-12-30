from domains.questions.schemas.question import CategoryRequest, QuestionRequest
from domains.use_cases_services import UseCasesService
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic
from kink import di
from utils.security import get_current_user

router = APIRouter()
di["questions_api_router"] = router

security = HTTPBasic()


@router.post("/new_question/")
def create_new_question(question_data: QuestionRequest, current_user: str = Depends(get_current_user)) -> JSONResponse:
    """
    Create a new question
    """
    service: UseCasesService = di[UseCasesService]
    service.manageQuestionUseCase.create_question(question_data, current_user)
    return JSONResponse(status_code=201, content={"message": "Question created"})


@router.get("/questions/")
def get_all_questions(current_user: str = Depends(get_current_user)) -> JSONResponse:
    """
    Get all questions
    """
    service: UseCasesService = di[UseCasesService]
    questions = service.manageQuestionUseCase.get_all_questions()
    return JSONResponse(status_code=201, content={"message": questions})


@router.delete("/questions/{question_id}")
def delete_question(question_id: int, current_user: str = Depends(get_current_user)) -> JSONResponse:
    """
    Delete a question
    """
    service: UseCasesService = di[UseCasesService]
    service.manageQuestionUseCase.delete_question(question_id)
    return JSONResponse(status_code=201, content={"message": "Question deleted"})


@router.put("/questions/{question_id}")
def update_question(
    question_id: int,
    question_data: QuestionRequest,
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Update a question
    """
    service: UseCasesService = di[UseCasesService]
    service.manageQuestionUseCase.update_question(question_id, question_data, current_user)
    return JSONResponse(status_code=201, content={"message": "Question updated"})


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


@router.get("/questions/{question_id}")
def get_question_by_id(question_id: int, current_user: str = Depends(get_current_user)) -> JSONResponse:
    """
    Get a question by ID
    """
    service: UseCasesService = di[UseCasesService]
    question = service.manageQuestionUseCase.get_question_by_id(question_id)
    return JSONResponse(status_code=201, content={"message": question})
