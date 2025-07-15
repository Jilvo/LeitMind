from domains.questions.schemas.question import ValidateRequest
from domains.use_cases_services import UseCasesService
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic
from kink import di
from utils.security import get_current_user

router = APIRouter()
di["validation_api_router"] = router

security = HTTPBasic()


@router.post("/validate")
def validate_question(
    validation_data: ValidateRequest,
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Validate a question
    """
    service: UseCasesService = di[UseCasesService]
    service.manageQuestionUseCase.validate_question(
        validation_data,
        current_user,
    )
    return JSONResponse(
        status_code=200,
        content={"message": "Question validated"},
    )


@router.get("/answer/correct/{question_id}")
def get_correct_answer(
    question_id: int,
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Get the correct answer for a question
    """
    service: UseCasesService = di[UseCasesService]
    answer = service.manageQuestionUseCase.get_correct_answer(question_id)
    return JSONResponse(
        status_code=200,
        content={"message": answer},
    )


@router.post("/validate/batch")
def validate_batch(
    answers: list[dict],
    current_user: str = Depends(get_current_user),
):
    # Logique pour valider plusieurs réponses
    pass


@router.get("/questions/{question_id}/stats")
def get_question_stats(
    question_id: int,
    current_user: str = Depends(get_current_user),
):
    # Logique pour récupérer les stats d'une question
    pass


@router.get("/users/{user_id}/score")
def get_user_score(
    user_id: int,
    current_user: str = Depends(get_current_user),
):
    # Logique pour récupérer le score d'un utilisateur
    pass
