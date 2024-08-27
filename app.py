#!/usr/bin/env python3
import http
import json

import uvicorn
from fastapi import FastAPI, Request
from pydantic import ValidationError
from sqlalchemy.exc import ProgrammingError, DataError, IntegrityError

from context.context_manager import context_log_meta, context_set_db_session_rollback
from logger import logger
from schemas.base import GenericResponseSchema
from utils.exceptions import AppException
from utils.helper import build_api_response
from constants.error_message import *
from api.v1 import api_v1_router
from api.healthcheck import router as router_base


app = FastAPI()

app.include_router(router_base)
app.include_router(api_v1_router, prefix='/api/v1')


#  register exception handlers here
@app.exception_handler(ValidationError)
async def pydantic_validation_exception_handler(request: Request, exc):
    context_set_db_session_rollback.set(True)
    logger.error(extra=context_log_meta.get(), msg=VALIDATION_FORMAT.format(error=exc.errors()))
    return build_api_response(GenericResponseSchema(status_code=http.HTTPStatus.BAD_REQUEST, error=VALIDATION_MESSAGE))


@app.exception_handler(ProgrammingError)
async def sql_exception_handler(request: Request, exc):
    context_set_db_session_rollback.set(True)
    logger.error(extra=context_log_meta.get(), msg=SQL_FORMAT.format(exc_args=str(exc.args), exc_statement=exc.statement))
    return build_api_response(GenericResponseSchema(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR, error=SQL_MESSAGE))


@app.exception_handler(DataError)
async def sql_data_exception_handler(request, exc):
    context_set_db_session_rollback.set(True)
    logger.error(extra=context_log_meta.get(), msg=SQL_DATA_FORMAT.format(exc_args=str(exc.args), exc_statement=exc.statement))
    return build_api_response(GenericResponseSchema(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR, error=SQL_DATA_MESSAGE))


@app.exception_handler(AppException)
async def application_exception_handler(request, exc):
    context_set_db_session_rollback.set(True)
    logger.error(extra=context_log_meta.get(), msg=APPLICATION_FORMAT.format(exc=json.loads(str(exc))))
    return build_api_response(GenericResponseSchema(status_code=exc.status_code, error=exc.message))


@app.exception_handler(IntegrityError)
async def sql_integrity_exception_handler(request, exc):
    context_set_db_session_rollback.set(True)
    logger.error(extra=context_log_meta.get(), msg=SQL_INTEGRITY_FORMAT.format(exc_args=str(exc.args), exc_statement=exc.statement))
    return build_api_response(GenericResponseSchema(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR, error=SQL_INTEGRITY_MESSAGE))


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=9999, reload=True)
