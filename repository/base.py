from sqlalchemy.orm import Session


class RepoBase:

    @classmethod
    def get_by_uuid(cls, uuid):
        from context.context_manager import get_db_session
        db: Session = get_db_session()
        return db.query(cls).filter(cls.uuid == uuid, cls.is_deleted.is_(False)).first()

    @classmethod
    def get_by_id(cls, id):
        from context.context_manager import get_db_session
        db: Session = get_db_session()
        return db.query(cls).filter(cls.id == id, cls.is_deleted.is_(False)).first()
