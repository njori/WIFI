from app.services.discovery_service import DiscoveryService
from app.services.router_monitor_service import RouterMonitorService
from app.repositories.network_repository import NetworkRepository


def discovery_job():

    networks = NetworkRepository.get_all()

    for network in networks:

        DiscoveryService.scan(
            network.cidr
        )


def router_monitor_job():

    RouterMonitorService.monitor()