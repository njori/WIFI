from sqlalchemy import desc

from app.models.router import Router
from app.models.device import Device
from app.models.network import Network
from app.models.traffic import Traffic

from app.utils.statistics import Statistics


class AnalyticsService:

    ############################################################
    # DASHBOARD SUMMARY
    ############################################################

    @staticmethod
    def summary():

        return {

            "routers": Statistics.total_routers(),

            "online_routers": Statistics.online_routers(),

            "offline_routers": Statistics.offline_routers(),

            "devices": Statistics.total_devices(),

            "connected_devices": Statistics.connected_devices(),

            "disconnected_devices": Statistics.disconnected_devices(),

            "networks": Statistics.total_networks()

        }

    ############################################################
    # CPU
    ############################################################

    @staticmethod
    def cpu():

        return {

            "average": Statistics.average_cpu(),

            "highest": Statistics.highest_cpu()

        }

    ############################################################
    # MEMORY
    ############################################################

    @staticmethod
    def memory():

        return {

            "average": Statistics.average_memory(),

            "highest": Statistics.highest_memory()

        }

    ############################################################
    # BANDWIDTH
    ############################################################

    @staticmethod
    def bandwidth():

        return {

            "upload": Statistics.total_upload(),

            "download": Statistics.total_download(),

            "utilization": Statistics.average_utilization()

        }

    ############################################################
    # NETWORK HEALTH
    ############################################################

    @staticmethod
    def health():

        return {

            "availability": Statistics.router_availability(),

            "online": Statistics.online_routers(),

            "offline": Statistics.offline_routers()

        }

    ############################################################
    # DEVICE TYPES
    ############################################################

    @staticmethod
    def device_types():

        return Statistics.device_types()

    ############################################################
    # TOP ROUTERS
    ############################################################

    @staticmethod
    def top_routers(limit=5):

        routers = Router.query.order_by(

            desc(Router.cpu_usage)

        ).limit(limit).all()

        return [

            router.to_dict()

            for router in routers

        ]

    ############################################################
    # TOP DEVICES
    ############################################################

    @staticmethod
    def top_devices(limit=10):

        devices = Device.query.order_by(

            desc(Device.download_speed)

        ).limit(limit).all()

        return [

            device.to_dict()

            for device in devices

        ]

    ############################################################
    # TOP NETWORKS
    ############################################################

    @staticmethod
    def top_networks():

        networks = Network.query.all()

        result = []

        for network in networks:

            result.append({

                "id": network.id,

                "ssid": network.ssid,

                "clients": len(network.devices),

                "channel": network.channel,

                "band": network.band,

                "router": network.router.name
                if network.router else None

            })

        return sorted(

            result,

            key=lambda x: x["clients"],

            reverse=True

        )

    ############################################################
    # LATEST TRAFFIC
    ############################################################

    @staticmethod
    def latest_traffic(limit=20):

        traffic = Traffic.query.order_by(

            desc(Traffic.created_at)

        ).limit(limit).all()

        return [

            record.to_dict()

            for record in traffic

        ]

    ############################################################
    # TRAFFIC HISTORY
    ############################################################

    @staticmethod
    def traffic_history(limit=50):

        history = Traffic.query.order_by(

            desc(Traffic.created_at)

        ).limit(limit).all()

        history.reverse()

        return [

            {

                "time": record.created_at.isoformat(),

                "upload": record.upload,

                "download": record.download,

                "utilization": record.utilization

            }

            for record in history

        ]

    ############################################################
    # DASHBOARD
    ############################################################

    @staticmethod
    def dashboard():

        return {

            "summary": AnalyticsService.summary(),

            "cpu": AnalyticsService.cpu(),

            "memory": AnalyticsService.memory(),

            "bandwidth": AnalyticsService.bandwidth(),

            "health": AnalyticsService.health(),

            "device_types": AnalyticsService.device_types(),

            "top_routers": AnalyticsService.top_routers(),

            "top_devices": AnalyticsService.top_devices(),

            "top_networks": AnalyticsService.top_networks(),

            "latest_traffic": AnalyticsService.latest_traffic(),

            "traffic_history": AnalyticsService.traffic_history()

        }