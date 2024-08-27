import http

from context.context_manager import context_log_meta
from logger import logger
from repository.user import UserRepository
from schemas.base import GenericResponseSchema
from schemas.user import UserInsertSchema, UserSchema
from utils.password_hasher import PasswordHasher


class UserService:
    MSG_USER_CREATED_SUCCESS = "User created successfully"

    @staticmethod
    def signup_user(user: UserInsertSchema) -> GenericResponseSchema:
        hashed_password = PasswordHasher.get_password_hash(user.password)
        user_to_create = user.create_db_entity(password_hash=hashed_password)
        user_data = UserRepository.create_user(user_to_create)
        logger.info(extra=context_log_meta.get(),
                    msg="User created successfully with uuid {}".format(user_to_create.uuid))
        return GenericResponseSchema(status_code=http.HTTPStatus.CREATED, message=UserService.MSG_USER_CREATED_SUCCESS,
                                     data=UserSchema.model_validate(user_data))
