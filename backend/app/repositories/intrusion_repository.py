from app.core.base_repository import BaseRepository
from app.models.intrusion import Intrusion


class IntrusionRepository(BaseRepository):

    model = Intrusion

    @classmethod
    def unresolved(cls):

        return Intrusion.query.filter_by(
            resolved=False
        ).all()

    @classmethod
    def resolved(cls):

        return Intrusion.query.filter_by(
            resolved=True
        ).all()