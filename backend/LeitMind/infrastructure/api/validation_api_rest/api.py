from domains.questions.schemas.question import QuestionRequest
from domains.use_cases_services import UseCasesService
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic
from kink import di
from utils.security import get_current_user

router = APIRouter()
di["validation_api_router"] = router

security = HTTPBasic()


@router.post("/new_question/")
def create_new_question(question_data: QuestionRequest, current_user: str = Depends(get_current_user)) -> JSONResponse:
    """
    Create a new question
    """
    service: UseCasesService = di[UseCasesService]
    service.manageQuestionUseCase.create_question(question_data, current_user)
    return JSONResponse(status_code=201, content={"message": "Question created"})
