from app.models.log import Log
from app.repositories.log_repository import LogRepository


class LogService:

    @staticmethod
    def write(
        module,
        action,
        message,
        user_id=None,
        router_id=None,
        network_id=None,
        device_id=None,
        ip_address=None,
        status="success",
    ):

        log = Log(
            module=module,
            action=action,
            message=message,
            user_id=user_id,
            router_id=router_id,
            network_id=network_id,
            device_id=device_id,
            ip_address=ip_address,
            status=status,
        )

        return LogRepository.create(log)

    @staticmethod
    def all():
        return LogRepository.get_all()

    @staticmethod
    def recent():
        return LogRepository.get_recent()