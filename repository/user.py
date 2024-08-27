from sqlalchemy.orm import Session
from schemas.user import UserSchema
from .base import RepoBase
from models.user import User


class UserRepository(RepoBase):

    @classmethod
    def create_user(cls, user: User) -> UserSchema:
        from context.context_manager import get_db_session
        db: Session = get_db_session()
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
