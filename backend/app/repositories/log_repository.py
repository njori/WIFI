from app.extensions import db
from app.models.log import Log


class LogRepository:

    @staticmethod
    def create(log):
        db.session.add(log)
        db.session.commit()
        return log

    @staticmethod
    def get_all():
        return Log.query.order_by(Log.created_at.desc()).all()

    @staticmethod
    def get_recent(limit=20):
        return (
            Log.query
            .order_by(Log.created_at.desc())
            .limit(limit)
            .all()
        )

    @staticmethod
    def get_by_module(module):
        return Log.query.filter_by(module=module).all()

    @staticmethod
    def delete_all():
        Log.query.delete()
        db.session.commit()