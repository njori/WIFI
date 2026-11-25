from app.automation.ssh_client import SSHClient

from app.models.automation_log import AutomationLog

from app.repositories.automation_repository import AutomationRepository

from app.repositories.router_repository import RouterRepository


class AutomationService:

    @staticmethod
    def execute(

        router_id,

        command

    ):

        router = RouterRepository.get_by_id(

            router_id

        )

        if not router:

            raise Exception(

                "Router not found."

            )

        ssh = SSHClient(

            host=router.ip_address,

            username=router.username,

            password=router.password

        )

        ssh.connect()

        result = ssh.execute(command)

        ssh.close()

        log = AutomationLog(

            router_id=router.id,

            command=command,

            output=result["output"]

        )

        AutomationRepository.create(log)

        return result