from fastapi import APIRouter
from kink import di

router = APIRouter()
di["questions_api_router"] = router
