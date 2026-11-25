from app.repositories.router_repository import RouterRepository
from app.scanners.snmp_scanner import SNMPScanner


class RouterMonitorService:

    @staticmethod
    def monitor():

        routers = RouterRepository.get_all()

        results = []

        for router in routers:

            info = SNMPScanner.discover(
                router.ip_address
            )

            if info["hostname"]:
                router.name = info["hostname"]

            if info["location"]:
                router.location = info["location"]

            RouterRepository.update()

            results.append({

                "router": router.to_dict(),

                "snmp": info

            })

        return results