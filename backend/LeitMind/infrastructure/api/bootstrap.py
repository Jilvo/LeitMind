from fastapi import APIRouter
from infrastructure.api.auth_api_rest.api import router as auth_router
from infrastructure.api.questions_api_rest.api import router as questions_router
from infrastructure.api.validation_api_rest.api import router as validation_router

auth_router: APIRouter = auth_router  # noqa: F841
questions_router: APIRouter = questions_router  # noqa: F841
validation_router: APIRouter = validation_router  # noqa: F841


def bootstrap():
    pass
