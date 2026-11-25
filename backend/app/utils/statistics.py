from datetime import datetime, timedelta

from sqlalchemy import func

from app.models.router import Router
from app.models.device import Device
from app.models.network import Network
from app.models.traffic import Traffic
from app.extensions import db

class Statistics:

    ##########################################################
    # ROUTERS
    ##########################################################

    @staticmethod
    def total_routers():

        return Router.query.count()

    @staticmethod
    def online_routers():

        return Router.query.filter_by(

            is_online=True

        ).count()

    @staticmethod
    def offline_routers():

        return Router.query.filter_by(

            is_online=False

        ).count()

    ##########################################################
    # DEVICES
    ##########################################################

    @staticmethod
    def total_devices():

        return Device.query.count()

    @staticmethod
    def connected_devices():

        return Device.query.filter_by(

            is_connected=True

        ).count()

    @staticmethod
    def disconnected_devices():

        return Device.query.filter_by(

            is_connected=False

        ).count()

    ##########################################################
    # NETWORKS
    ##########################################################

    @staticmethod
    def total_networks():

        return Network.query.count()

    ##########################################################
    # CPU
    ##########################################################

    @staticmethod
    def average_cpu():

        cpu = Router.query.with_entities(

            func.avg(

                Router.cpu_usage

            )

        ).scalar()

        return round(cpu or 0, 2)

    @staticmethod
    def highest_cpu():

        router = Router.query.order_by(

            Router.cpu_usage.desc()

        ).first()

        if router:

            return {

                "router": router.name,

                "cpu": router.cpu_usage

            }

        return None

    ##########################################################
    # MEMORY
    ##########################################################

    @staticmethod
    def average_memory():

        memory = Router.query.with_entities(

            func.avg(

                Router.memory_usage

            )

        ).scalar()

        return round(memory or 0, 2)

    @staticmethod
    def highest_memory():

        router = Router.query.order_by(

            Router.memory_usage.desc()

        ).first()

        if router:

            return {

                "router": router.name,

                "memory": router.memory_usage

            }

        return None

    ##########################################################
    # BANDWIDTH
    ##########################################################

    @staticmethod
    def total_upload():

        upload = Traffic.query.with_entities(

            func.sum(

                Traffic.upload

            )

        ).scalar()

        return round(upload or 0, 2)

    @staticmethod
    def total_download():

        download = Traffic.query.with_entities(

            func.sum(

                Traffic.download

            )

        ).scalar()

        return round(download or 0, 2)

    @staticmethod
    def average_utilization():

        utilization = Traffic.query.with_entities(

            func.avg(

                Traffic.utilization

            )

        ).scalar()

        return round(utilization or 0, 2)

    ##########################################################
    # TRAFFIC
    ##########################################################

    @staticmethod
    def total_bytes_in():

        total = Traffic.query.with_entities(

            func.sum(

                Traffic.bytes_in

            )

        ).scalar()

        return total or 0

    @staticmethod
    def total_bytes_out():

        total = Traffic.query.with_entities(

            func.sum(

                Traffic.bytes_out

            )

        ).scalar()

        return total or 0

    ##########################################################
    # TODAY'S TRAFFIC
    ##########################################################

    @staticmethod
    def today_upload():

        today = datetime.utcnow().date()

        upload = Traffic.query.filter(

            func.date(

                Traffic.created_at

            ) == today

        ).with_entities(

            func.sum(

                Traffic.upload

            )

        ).scalar()

        return round(upload or 0, 2)

    @staticmethod
    def today_download():

        today = datetime.utcnow().date()

        download = Traffic.query.filter(

            func.date(

                Traffic.created_at

            ) == today

        ).with_entities(

            func.sum(

                Traffic.download

            )

        ).scalar()

        return round(download or 0, 2)

    ##########################################################
    # LAST 24 HOURS
    ##########################################################

    @staticmethod
    def last_24_hours():

        yesterday = datetime.utcnow() - timedelta(hours=24)

        return Traffic.query.filter(

            Traffic.created_at >= yesterday

        ).count()

    ##########################################################
    # DEVICE TYPES
    ##########################################################

    @staticmethod
    def device_types():

        rows = db.session.query(

            Device.device_type,

            func.count(Device.id)

        ).group_by(

            Device.device_type

        ).all()

        result = []

        for row in rows:

            result.append({

                "type": row[0],

                "count": row[1]

            })

        return result

    ##########################################################
    # ONLINE PERCENTAGE
    ##########################################################

    @staticmethod
    def router_availability():

        total = Statistics.total_routers()

        if total == 0:

            return 0

        online = Statistics.online_routers()

        return round(

            (online / total) * 100,

            2

        )