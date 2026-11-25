from app.repositories.router_repository import RouterRepository
from app.repositories.network_repository import NetworkRepository
from app.repositories.device_repository import DeviceRepository


class TopologyService:

    @staticmethod
    def generate():

        nodes = []
        edges = []

        # -----------------------
        # Routers
        # -----------------------

        routers = RouterRepository.get_all()

        for router in routers:

            nodes.append({
                "id": f"router-{router.id}",
                "label": router.name,
                "type": "router",
                "ip": router.ip_address,
                "online": router.is_online
            })

        # -----------------------
        # Networks
        # -----------------------

        networks = NetworkRepository.get_all()

        for network in networks:

            nodes.append({
                "id": f"network-{network.id}",
                "label": "network.ssid",
                "type": "network",
                "cidr": network.cidr
            })

            if network.router_id:

                edges.append({
                    "source": f"router-{network.router_id}",
                    "target": f"network-{network.id}"
                })

        # -----------------------
        # Devices
        # -----------------------

        devices = DeviceRepository.get_all()

        for device in devices:

            nodes.append({
                "id": f"device-{device.id}",
                "label": device.hostname or device.ip_address,
                "type": "device",
                "manufacturer": device.manufacturer,
                "device_type": device.device_type,
                "online": device.is_connected
            })

            if device.network_id:

                edges.append({
                    "source": f"network-{device.network_id}",
                    "target": f"device-{device.id}"
                })

        return {
            "nodes": nodes,
            "edges": edges
        }