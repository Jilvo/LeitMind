from domains.questions.schemas.question import (
    QuestionRequest,
)
from domains.use_cases_services import (
    UseCasesService,
)
from fastapi import (
    APIRouter,
    Depends,
)
from fastapi.responses import (
    JSONResponse,
)
from fastapi.security import (
    HTTPBasic,
)
from kink import (
    di,
)
from utils.security import (
    get_current_user,
)

router = APIRouter()
di["questions_api_router"] = router

security = HTTPBasic()


@router.post("/new_question/")
def create_new_question(
    question_data: QuestionRequest,
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Create a new question
    """
    service: UseCasesService = di[UseCasesService]
    service.manageQuestionUseCase.create_question(
        question_data,
        current_user,
    )
    return JSONResponse(
        status_code=201,
        content={"message": "Question created"},
    )


@router.get("/questions/")
def get_all_questions(
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Get all questions
    """
    service: UseCasesService = di[UseCasesService]
    questions = service.manageQuestionUseCase.get_all_questions()
    return JSONResponse(
        status_code=201,
        content={"message": questions},
    )


@router.delete("/questions/{question_id}")
def delete_question(
    question_id: int,
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Delete a question
    """
    service: UseCasesService = di[UseCasesService]
    service.manageQuestionUseCase.delete_question(question_id)
    return JSONResponse(
        status_code=201,
        content={"message": "Question deleted"},
    )


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
    service.manageQuestionUseCase.update_question(
        question_id,
        question_data,
        current_user,
    )
    return JSONResponse(
        status_code=201,
        content={"message": "Question updated"},
    )


@router.get("/questions/{question_id}")
def get_question_by_id(
    question_id: int,
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Get a question by ID
    """
    service: UseCasesService = di[UseCasesService]
    questions_and_answers = service.manageQuestionUseCase.get_question_by_id(question_id)
    return JSONResponse(
        status_code=200,
        content={"message": questions_and_answers},
    )


@router.get("/bulk_create_questions/")
def bulk_create_questions(
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Bulk create questions
    """
    service: UseCasesService = di[UseCasesService]
    res = service.manageQuestionUseCase.bulk_create_questions()
    return JSONResponse(
        status_code=201,
        content={"message": res},
    )


@router.get("/questions/daily_questions")
def get_daily_questions(
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Get daily questions
    """
    service: UseCasesService = di[UseCasesService]
    res = service.selectDailyQuestionsUseCase.execute()
    return JSONResponse(
        status_code=200,
        content={"message": res},
    )
