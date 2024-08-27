from datetime import datetime
from typing import Optional, Any
from uuid import UUID

from pydantic.main import BaseModel, ConfigDict


class GenericResponseSchema(BaseModel):
    error: Optional[str] = None
    message: Optional[str] = None
    data: Optional[Any] = None
    status_code: Optional[int] = None



class DBBaseSchema(BaseModel):
    """Base model for all models that will be stored in the database"""
    model_config = ConfigDict(from_attributes=True)

    id: int
    uuid: UUID
    created_at: datetime
    updated_at: Optional[datetime]
    is_deleted: bool