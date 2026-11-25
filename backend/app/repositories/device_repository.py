from app.core.base_repository import BaseRepository
from app.models.device import Device


class DeviceRepository(BaseRepository):

    model = Device

    @classmethod
    def get_by_mac(cls, mac):

        return Device.query.filter_by(
            mac_address=mac
        ).first()

    @classmethod
    def get_by_ip(cls, ip):

        return Device.query.filter_by(
            ip_address=ip
        ).first()

    @classmethod
    def connected(cls):

        return Device.query.filter_by(
            is_connected=True
        ).all()

    @classmethod
    def disconnected(cls):

        return Device.query.filter_by(
            is_connected=False
        ).all()