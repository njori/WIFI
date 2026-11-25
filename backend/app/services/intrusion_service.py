from app.models.intrusion import Intrusion

from app.repositories.intrusion_repository import IntrusionRepository

from app.services.notification_service import NotificationService
from app.services.email_service import EmailService

from app.sockets.emitter import SocketEmitter


class IntrusionService:

    @staticmethod
    def create(
        router,
        attack,
        message,
        severity="warning"
    ):

        intrusion = Intrusion(

            router_id=router.id,

            severity=severity,

            attack_type=attack,

            message=message

        )

        intrusion = IntrusionRepository.create(
            intrusion
        )

        NotificationService.send(

            title=attack,

            message=message,

            type=severity

        )

        EmailService.security_alert(
            intrusion
        )

        SocketEmitter.security_alert(
            intrusion.to_dict()
        )

        return intrusion

    @staticmethod
    def high_cpu(router):

        return IntrusionService.create(

            router,

            "High CPU",

            f"{router.name} CPU reached {router.cpu_usage}%",

            "danger"

        )

    @staticmethod
    def high_memory(router):

        return IntrusionService.create(

            router,

            "High Memory",

            f"{router.name} memory reached {router.memory_usage}%",

            "danger"

        )

    @staticmethod
    def router_offline(router):

        return IntrusionService.create(

            router,

            "Router Offline",

            f"{router.name} is offline.",

            "danger"

        )

    @staticmethod
    def rogue_device(device):

        return IntrusionService.create(

            device.router,

            "Unknown Device",

            f"{device.mac_address} joined the network.",

            "warning"

        )

    @staticmethod
    def port_scan(router):

        return IntrusionService.create(

            router,

            "Port Scan",

            "Possible port scan detected.",

            "danger"

        )