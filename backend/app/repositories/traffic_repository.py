from app.core.base_repository import BaseRepository
from app.models.traffic import Traffic


class TrafficRepository(BaseRepository):

    model = Traffic

    @classmethod
    def latest(cls):

        return (
            Traffic.query
            .order_by(Traffic.created_at.desc())
            .all()
        )

    @classmethod
    def router_history(cls, router_id):

        return (
            Traffic.query
            .filter_by(router_id=router_id)
            .order_by(Traffic.created_at.desc())
            .all()
        )