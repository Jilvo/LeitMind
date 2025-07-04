from fastapi import APIRouter

from infrastructure.api.attempt_api_rest.api import router as attempt_router
from infrastructure.api.auth_api_rest.api import router as auth_router
from infrastructure.api.category_api_rest.api import router as category_router
from infrastructure.api.questions_api_rest.api import \
    router as questions_router
from infrastructure.api.subscription_api_rest.api import \
    router as subscription_router
from infrastructure.api.validation_api_rest.api import \
    router as validation_router

auth_router: APIRouter = auth_router  # noqa: F841
questions_router: APIRouter = questions_router  # noqa: F841
validation_router: APIRouter = validation_router  # noqa: F841
category_router: APIRouter = category_router  # noqa: F841
subscription_router: APIRouter = subscription_router  # noqa: F841
attempt_router: APIRouter = attempt_router  # noqa: F841


def bootstrap():
    pass
