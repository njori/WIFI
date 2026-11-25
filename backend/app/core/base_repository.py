from app.extensions import db


class BaseRepository:

    model = None

    @classmethod
    def get_all(cls):
        return cls.model.query.all()

    @classmethod
    def get_by_id(cls, object_id):
        return cls.model.query.get(object_id)

    @classmethod
    def create(cls, obj):
        db.session.add(obj)
        db.session.commit()
        return obj

    @classmethod
    def update(cls, obj=None):
        db.session.commit()
        return obj

    @classmethod
    def delete(cls, obj):
        db.session.delete(obj)
        db.session.commit()

    @classmethod
    def count(cls):
        return cls.model.query.count()