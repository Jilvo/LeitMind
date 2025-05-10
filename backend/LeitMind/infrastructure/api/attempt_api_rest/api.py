
from domains.use_cases_services import UseCasesService
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic
from kink import di
from utils.security import decode_access_token, get_current_user
from domains.questions.use_case.manage_attempt_use_case import ManageAttemptUseCase


router = APIRouter()
di["attempt_api_router"] = router
security = HTTPBasic()


@router.get("/attempts")
def get_all_attempts(
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Get all attempts
    """
    service: UseCasesService = di[UseCasesService]
    attempts = service.manageAttemptUseCase.get_all_attempts()
    return JSONResponse(
        status_code=200,
        content={"attempts": attempts},
    )
@router.get("/attempts/{attempt_id}")
def get_attempt_by_id(
    attempt_id: int,
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Get an attempt by ID
    """
    service: UseCasesService = di[UseCasesService]
    attempt = service.manageAttemptUseCase.get_attempt_by_id(attempt_id)
    if not attempt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Attempt not found",
        )
    return JSONResponse(
        status_code=200,
        content={"attempt": attempt},
    )
@router.post("/attempts")
def create_attempt(
    attempt: dict,
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Create a new attempt
    """
    service: UseCasesService = di[UseCasesService]
    new_attempt = service.manageAttemptUseCase.create_attempt(attempt)
    return JSONResponse(
        status_code=201,
        content={"attempt": new_attempt},
    )
@router.put("/attempts/{attempt_id}")
def update_attempt(
    attempt_id: int,
    attempt: dict,
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Update an attempt
    """
    service: UseCasesService = di[UseCasesService]
    updated_attempt = service.manageAttemptUseCase.update_attempt(attempt)
    if not updated_attempt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Attempt not found",
        )
    return JSONResponse(
        status_code=200,
        content={"attempt": updated_attempt},
    )
@router.delete("/attempts/{attempt_id}")
def delete_attempt(
    attempt_id: int,
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Delete an attempt
    """
    service: UseCasesService = di[UseCasesService]
    service.manageAttemptUseCase.delete_attempt(attempt_id)
    return JSONResponse(
        status_code=204,
        content={},
    )
@router.get("/attempts/user/{user_id}")
def get_attempts_by_user_id(
    user_id: int,
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Get all attempts by user ID
    """
    service: UseCasesService = di[UseCasesService]
    attempts = service.manageAttemptUseCase.get_attempts_by_user_id(user_id)
    return JSONResponse(
        status_code=200,
        content={"attempts": attempts},
    )
@router.get("/attempts/question/{question_id}")
def get_attempts_by_question_id(
    question_id: int,
    current_user: str = Depends(get_current_user),
) -> JSONResponse:
    """
    Get all attempts by question ID
    """
    service: UseCasesService = di[UseCasesService]
    attempts = service.manageAttemptUseCase.get_attempts_by_question_id(question_id)
    return JSONResponse(
        status_code=200,
        content={"attempts": attempts},
    )