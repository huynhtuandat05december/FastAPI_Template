import uuid as uuid

from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID

from db.base_class import Base, Common


class User(Base, Common):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False)
    password_hash = Column(String(255), nullable=False)
    status = Column(String(20), nullable=False)