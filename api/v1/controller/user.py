import http

from fastapi import APIRouter, Depends

from context.context_manager import build_request_context
from schemas.base import GenericResponseSchema
from schemas.user import UserInsertSchema
from services.user import UserService
from utils.helper import build_api_response

router = APIRouter()


@router.post("/signup", status_code=http.HTTPStatus.CREATED, response_model=GenericResponseSchema)
async def signup_user(user: UserInsertSchema, _=Depends(build_request_context)):
    response: GenericResponseSchema = UserService.signup_user(user=user)
    return build_api_response(response)
