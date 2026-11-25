# from app.models.router import Router
# from app.extensions import db


# class RouterRepository:

#     @staticmethod
#     def all():
#         return Router.query.all()

#     @staticmethod
#     def get(router_id):
#         return Router.query.get(router_id)

#     @staticmethod
#     def create(router):
#         db.session.add(router)
#         db.session.commit()
#         return router

#     @staticmethod
#     def delete(router):
#         db.session.delete(router)
#         db.session.commit()

from app.core.base_repository import BaseRepository
from app.models.router import Router


class RouterRepository(BaseRepository):

    model = Router