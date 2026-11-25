from datetime import datetime

from app.repositories.router_repository import RouterRepository

from app.services.traffic_service import TrafficService
from app.services.intrusion_service import IntrusionService
from app.services.dashboard_service import DashboardService
from app.services.topology_service import TopologyService
from app.services.email_service import EmailService
from app.services.analytics_service import AnalyticsService


from app.snmp.monitor import SNMPMonitor

from app.sockets.emitter import SocketEmitter


class MonitoringService:

    @staticmethod
    def monitor():

        routers = RouterRepository.get_all()

        if not routers:
            return False

        for router in routers:

            previous_status = router.is_online

            try:

                ####################################################
                # Read SNMP Information
                ####################################################

                router.name = SNMPMonitor.get_hostname(
                    router.ip_address
                )

                router.uptime = int(
                    SNMPMonitor.get_uptime(
                        router.ip_address
                    )
                )

                router.cpu_usage = float(
                    SNMPMonitor.get_cpu(
                        router.ip_address
                    )
                )

                router.memory_usage = float(
                    SNMPMonitor.get_memory(
                        router.ip_address
                    )
                )

                router.firmware_version = (
                    SNMPMonitor.get_description(
                        router.ip_address
                    )
                )

                router.last_seen = datetime.utcnow()
                router.is_online = True

                RouterRepository.update(router)

                ####################################################
                # Router came online
                ####################################################

                if not previous_status:

                    EmailService.router_online(router)

                    SocketEmitter.router_online(
                        router.to_dict()
                    )

                ####################################################
                # Interface Traffic
                ####################################################

                traffic = SNMPMonitor.get_interface_statistics(
                    router.ip_address
                )

                if traffic:

                    TrafficService.save(
                        router=router,
                        interface=traffic["interface"],
                        bytes_in=traffic["bytes_in"],
                        bytes_out=traffic["bytes_out"],
                        packets_in=traffic["packets_in"],
                        packets_out=traffic["packets_out"],
                        upload=traffic["upload"],
                        download=traffic["download"],
                        utilization=traffic["utilization"]
                    )

                ####################################################
                # Intrusion / Threshold Checks
                ####################################################

                if router.cpu_usage >= 90:
                    IntrusionService.high_cpu(router)

                if router.memory_usage >= 90:
                    IntrusionService.high_memory(router)

                ####################################################
                # Live Update
                ####################################################

                SocketEmitter.router_update(
                    router.to_dict()
                )

            except Exception as e:

                router.is_online = False
                router.last_seen = datetime.utcnow()

                RouterRepository.update(router)

                ####################################################
                # Router went offline
                ####################################################

                if previous_status:

                    IntrusionService.router_offline(router)

                    EmailService.router_offline(router)

                SocketEmitter.router_offline(
                    router.to_dict()
                )

                print(
                    f"[Monitoring] {router.ip_address}: {e}"
                )

        ####################################################
        # Refresh Dashboard
        ####################################################

        SocketEmitter.dashboard(
            DashboardService.overview()
        )

        SocketEmitter.analytics(
            AnalyticsService.dashboard()
        )

        ####################################################
        # Refresh Network Topology
        ####################################################

        SocketEmitter.topology(
            TopologyService.generate()
        )

        ####################################################
        # Monitoring Finished
        ####################################################

        return True