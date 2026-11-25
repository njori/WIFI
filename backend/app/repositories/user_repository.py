from app.models.user import User
from app.extensions import db


class UserRepository:

    @staticmethod
    def exists_email(email):
        return User.query.filter_by(email=email).first() is not None

    @staticmethod
    def exists_username(username):
        return User.query.filter_by(username=username).first() is not None

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def create(user):
        db.session.add(user)
        db.session.commit()
        return user
    
    
    @staticmethod
    def update(user):
        db.session.add(user)
        db.session.commit()
        return user