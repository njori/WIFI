from datetime import datetime

from app.models.router import Router
from app.models.network import Network
from app.models.device import Device
from app.models.traffic import Traffic
from app.models.log import Log

from app.services.analytics_service import AnalyticsService


class ReportManager:

    ###########################################################
    # Complete Report
    ###########################################################

    @staticmethod
    def generate():

        return {

            "generated_at": datetime.utcnow().isoformat(),

            "analytics":

                AnalyticsService.dashboard(),

            "routers":

                [

                    router.to_dict()

                    for router in Router.query.all()

                ],

            "networks":

                [

                    network.to_dict()

                    for network in Network.query.all()

                ],

            "devices":

                [

                    device.to_dict()

                    for device in Device.query.all()

                ],

            "traffic":

                [

                    traffic.to_dict()

                    for traffic in Traffic.query.all()

                ],

            "logs":

                [

                    log.to_dict()

                    for log in Log.query.limit(500).all()

                ]

        }