from datetime import datetime

from pytz import timezone
from sqlalchemy import Column, TIMESTAMP, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

UTC = timezone('UTC')


def time_now():
    return datetime.now(UTC)

class Common:
    created_at = Column(TIMESTAMP(timezone=True), default=time_now, nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), default=time_now, onupdate=time_now, nullable=False)
    is_deleted = Column(Boolean, default=False)
