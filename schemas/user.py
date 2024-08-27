from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel, validator, ConfigDict

from schemas.base import DBBaseSchema


class UserRole(str, Enum):
    ADMIN = "admin"
    CUSTOMER = "customer"


class UserStatus(str, Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"


class UserResponseModel(BaseModel):
    first_name: str
    last_name: str
    email: str
    role: UserRole = UserRole.CUSTOMER


class UserBaseSchema(UserResponseModel):
    status: UserStatus = UserStatus.ACTIVE


class UserInsertSchema(UserBaseSchema):
    password: str

    def create_db_entity(self, password_hash: str):
        from models.user import User
        dict_to_build_db_entity = self.dict()
        dict_to_build_db_entity['password_hash'] = password_hash
        dict_to_build_db_entity.pop('password')
        return User(**dict_to_build_db_entity)


class UserSchema(UserBaseSchema, DBBaseSchema):
    model_config = ConfigDict(from_attributes=True)

    password_hash: str








