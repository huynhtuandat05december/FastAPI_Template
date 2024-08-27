from fastapi import APIRouter
from .controller.user import router as user_router

api_v1_router = APIRouter()
api_v1_router.include_router(user_router, prefix='/auth', tags=["Auth"])