from app.core.base_repository import BaseRepository
from app.models.network import Network


class NetworkRepository(BaseRepository):

    model = Network

    @classmethod
    def get_by_ssid(cls, ssid):
        return Network.query.filter_by(
            ssid=ssid
        ).first()

    @classmethod
    def get_by_bssid(cls, bssid):
        return Network.query.filter_by(
            bssid=bssid
        ).first()

    @classmethod
    def get_by_router(cls, router_id):
        return Network.query.filter_by(
            router_id=router_id
        ).all()