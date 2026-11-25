from app.models.device import Device
from app.repositories.device_repository import DeviceRepository
from app.services.topology_service import TopologyService
from app.sockets.emitter import SocketEmitter

class DeviceService:

    @staticmethod
    def get_all():
        return [
            device.to_dict()
            for device in DeviceRepository.get_all()
        ]

    @staticmethod
    def get(device_id):

        device = DeviceRepository.get_by_id(device_id)

        if device is None:
            raise Exception("Device not found.")

        return device.to_dict()

    @staticmethod
    def create(data):

        if DeviceRepository.get_by_mac(data["mac_address"]):
            raise Exception("MAC address already exists.")

        device = Device(
            mac_address=data["mac_address"],
            ip_address=data["ip_address"],
            hostname=data.get("hostname"),
            device_name=data.get("device_name"),
            manufacturer=data.get("manufacturer"),
            operating_system=data.get("operating_system"),
            device_type=data.get("device_type"),
            signal_strength=data.get("signal_strength", 0),
            connection_speed=data.get("connection_speed", 0),
            upload_speed=data.get("upload_speed", 0),
            download_speed=data.get("download_speed", 0),
            network_id=data["network_id"],
            router_id=data.get("router_id"),
            is_connected=data.get("is_connected", True)
        )

        # DeviceRepository.create(device)

        # return device.to_dict()
        device = DeviceRepository.create(device)

        SocketEmitter.topology(
            TopologyService.generate()
        )

        return device

    @staticmethod
    def update(device_id, data):

        device = DeviceRepository.get_by_id(device_id)

        if device is None:
            raise Exception("Device not found.")

        device.mac_address = data.get(
            "mac_address",
            device.mac_address
        )

        device.ip_address = data.get(
            "ip_address",
            device.ip_address
        )

        device.hostname = data.get(
            "hostname",
            device.hostname
        )

        device.device_name = data.get(
            "device_name",
            device.device_name
        )

        device.manufacturer = data.get(
            "manufacturer",
            device.manufacturer
        )

        device.operating_system = data.get(
            "operating_system",
            device.operating_system
        )

        device.device_type = data.get(
            "device_type",
            device.device_type
        )

        device.signal_strength = data.get(
            "signal_strength",
            device.signal_strength
        )

        device.connection_speed = data.get(
            "connection_speed",
            device.connection_speed
        )

        device.upload_speed = data.get(
            "upload_speed",
            device.upload_speed
        )

        device.download_speed = data.get(
            "download_speed",
            device.download_speed
        )

        device.network_id = data.get(
            "network_id",
            device.network_id
        )

        device.router_id = data.get(
            "router_id",
            device.router_id
        )

        device.is_connected = data.get(
            "is_connected",
            device.is_connected
        )

        DeviceRepository.update()

        SocketEmitter.topology(
            TopologyService.generate()
        )

        return device

    @staticmethod
    def delete(device_id):

        device = DeviceRepository.get_by_id(device_id)

        if device is None:
            raise Exception("Device not found.")

        
    
        DeviceRepository.delete(device)

        SocketEmitter.topology(
            TopologyService.generate()
        )