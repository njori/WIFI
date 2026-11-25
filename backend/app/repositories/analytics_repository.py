from app.models.router import Router
from app.models.device import Device
from app.models.network import Network
from app.models.intrusion import Intrusion
from app.models.traffic import Traffic


class AnalyticsRepository:

    @staticmethod
    def total_routers():
        return Router.query.count()

    @staticmethod
    def online_routers():
        return Router.query.filter_by(
            is_online=True
        ).count()

    @staticmethod
    def offline_routers():
        return Router.query.filter_by(
            is_online=False
        ).count()

    @staticmethod
    def total_networks():
        return Network.query.count()

    @staticmethod
    def total_devices():
        return Device.query.count()

    @staticmethod
    def connected_devices():
        return Device.query.filter_by(
            is_connected=True
        ).count()

    @staticmethod
    def disconnected_devices():
        return Device.query.filter_by(
            is_connected=False
        ).count()

    @staticmethod
    def active_alerts():
        return Intrusion.query.filter_by(
            resolved=False
        ).count()

    @staticmethod
    def traffic():
        return (
            Traffic.query
            .order_by(Traffic.created_at.desc())
            .limit(30)
            .all()
        )