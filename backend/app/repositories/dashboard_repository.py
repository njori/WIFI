from app.models.user import User
from app.models.network import Network
from app.models.router import Router
from app.models.device import Device
from app.models.log import Log


class DashboardRepository:

    @staticmethod
    def total_users():
        return User.query.count()

    @staticmethod
    def total_networks():
        return Network.query.count()

    @staticmethod
    def total_routers():
        return Router.query.count()

    @staticmethod
    def total_devices():
        return Device.query.count()

    @staticmethod
    def online_devices():
        return Device.query.filter_by(is_connected=True).count()

    @staticmethod
    def online_routers():
        return Router.query.filter_by(is_online=True).count()

    @staticmethod
    def recent_devices(limit=5):
        return Device.query.order_by(Device.created_at.desc()).limit(limit).all()

    @staticmethod
    def recent_logs(limit=10):
        return Log.query.order_by(Log.created_at.desc()).limit(limit).all()