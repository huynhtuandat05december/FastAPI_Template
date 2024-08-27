import http

from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/healthcheck", status_code=http.HTTPStatus.OK)
async def status_code_check():
    return JSONResponse(status_code=http.HTTPStatus.OK, content={"status_code": "OK"})

