from app.core.base_service import BaseService
from app.models.network import Network
from app.repositories.network_repository import NetworkRepository
from app.services.topology_service import TopologyService
from app.sockets.emitter import SocketEmitter
from app.services.notification_service import NotificationService


class NetworkService(BaseService):

    repository = NetworkRepository

    @classmethod
    def create(cls, data):

        if cls.repository.get_by_ssid(data["ssid"]):
            raise Exception("SSID already exists.")

        network = Network(
            ssid=data["ssid"],
            bssid=data.get("bssid"),
            password=data.get("password"),
            security_type=data.get("security_type", "WPA2"),
            channel=data.get("channel"),
            band=data.get("band", "2.4GHz"),
            vlan=data.get("vlan"),
            max_clients=data.get("max_clients", 50),
            bandwidth_limit=data.get("bandwidth_limit"),
            description=data.get("description"),
            router_id=data["router_id"]
        )

        network = cls.repository.create(network)

        SocketEmitter.topology(
            TopologyService.generate()
        )

        NotificationService.send(
            title="Network Created",
            message=f"{network.ssid} has been created.",
            type="success"
        )

        return network.to_dict()

    @classmethod
    def update(cls, network_id, data):

        network = cls.repository.get_by_id(network_id)

        if not network:
            raise Exception("Network not found.")

        network.router_id = data.get(
            "router_id",
            network.router_id
        )

        network.ssid = data.get(
            "ssid",
            network.ssid
        )

        network.bssid = data.get(
            "bssid",
            network.bssid
        )

        network.password = data.get(
            "password",
            network.password
        )

        network.security_type = data.get(
            "security_type",
            network.security_type
        )

        network.channel = data.get(
            "channel",
            network.channel
        )

        network.band = data.get(
            "band",
            network.band
        )

        network.vlan = data.get(
            "vlan",
            network.vlan
        )

        network.max_clients = data.get(
            "max_clients",
            network.max_clients
        )

        network.bandwidth_limit = data.get(
            "bandwidth_limit",
            network.bandwidth_limit
        )

        network.description = data.get(
            "description",
            network.description
        )

        network.is_active = data.get(
            "is_active",
            network.is_active
        )

        cls.repository.update()

        SocketEmitter.topology(
            TopologyService.generate()
        )

        return network

    @classmethod
    def delete(cls, network_id):

        network = cls.repository.get_by_id(network_id)

        if not network:
            raise Exception("Network not found.")

        cls.repository.delete(network)

        SocketEmitter.dashboard(

            DashboardService.overview()

        )

        SocketEmitter.traffic(

            AnalyticsService.bandwidth()

        )

        SocketEmitter.topology(

            TopologyService.generate()

        )

        NotificationService.send(
            title="Network Deleted",
            message=f"{network.ssid} has been deleted.",
            type="warning"
        )

        return {
            "message": "Network deleted successfully."
        }