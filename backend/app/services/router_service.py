from app.core.base_service import BaseService
from app.models.router import Router
from app.repositories.router_repository import RouterRepository
from app.services.notification_service import NotificationService
from app.sockets.emitter import SocketEmitter
from app.services.topology_service import TopologyService
from app.sockets.emitter import SocketEmitter

class RouterService(BaseService):

    repository = RouterRepository

    @classmethod
    def create(cls, data):

        router = Router(
            name=data["name"],
            ip_address=data["ip_address"],
            mac_address=data.get("mac_address"),
            manufacturer=data.get("manufacturer"),
            model=data.get("model"),
            firmware_version=data.get("firmware_version"),
            serial_number=data.get("serial_number"),
            location=data.get("location"),
            uptime=data.get("uptime", 0),
            cpu_usage=data.get("cpu_usage", 0),
            memory_usage=data.get("memory_usage", 0),
            is_online=data.get("is_online", False)
        )

        cls.repository.create(router)

        notification = NotificationService.create(
            title="Router Added",
            message=f"Router '{router.name}' has been added.",
            notification_type="success"
        )

        SocketEmitter.router_online(router)
        SocketEmitter.notification(notification)

        router = RouterRepository.create(router)

        SocketEmitter.topology(
            TopologyService.generate()
        )

        return router

    @classmethod
    def update(cls, router_id, data):

        router = cls.repository.get_by_id(router_id)

        if router is None:
            raise Exception("Router not found.")

        router.name = data.get("name", router.name)
        router.ip_address = data.get("ip_address", router.ip_address)
        router.mac_address = data.get("mac_address", router.mac_address)
        router.manufacturer = data.get("manufacturer", router.manufacturer)
        router.model = data.get("model", router.model)
        router.firmware_version = data.get(
            "firmware_version",
            router.firmware_version
        )
        router.serial_number = data.get(
            "serial_number",
            router.serial_number
        )
        router.location = data.get("location", router.location)
        router.cpu_usage = data.get("cpu_usage", router.cpu_usage)
        router.memory_usage = data.get(
            "memory_usage",
            router.memory_usage
        )
        router.uptime = data.get("uptime", router.uptime)
        router.is_online = data.get(
            "is_online",
            router.is_online
        )

        cls.repository.update()

        notification = NotificationService.create(
            title="Router Updated",
            message=f"Router '{router.name}' has been updated.",
            notification_type="info"
        )

        if router.is_online:
            SocketEmitter.router_online(router)
        else:
            SocketEmitter.router_offline(router)

        SocketEmitter.notification(notification)

        RouterRepository.update()

        SocketEmitter.topology(
            TopologyService.generate()
        )

        return router

    @classmethod
    def delete(cls, router_id):

        router = cls.repository.get_by_id(router_id)

        if router is None:
            raise Exception("Router not found.")

        cls.repository.delete(router)

        notification = NotificationService.create(
            title="Router Removed",
            message=f"Router '{router.name}' has been removed.",
            notification_type="warning"
        )

        SocketEmitter.notification(notification)

        # return True
        RouterRepository.delete(router)

        SocketEmitter.topology(
            TopologyService.generate()
        )