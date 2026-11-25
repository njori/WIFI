from datetime import datetime

from app.services.analytics_service import AnalyticsService
from app.services.notification_service import NotificationService
from app.services.report_service import ReportService

from app.models.router import Router
from app.models.device import Device
from app.models.network import Network
from app.models.log import Log


class DashboardService:

    ###########################################################
    # Dashboard Overview
    ###########################################################

    @staticmethod
    def overview():

        return {

            "generated_at": datetime.utcnow().isoformat(),

            "summary":
                AnalyticsService.summary(),

            "cpu":
                AnalyticsService.cpu(),

            "memory":
                AnalyticsService.memory(),

            "bandwidth":
                AnalyticsService.bandwidth(),

            "health":
                AnalyticsService.health(),

            "device_types":
                AnalyticsService.device_types(),

            "top_routers":
                AnalyticsService.top_routers(),

            "top_devices":
                AnalyticsService.top_devices(),

            "top_networks":
                AnalyticsService.top_networks(),

            "latest_traffic":
                AnalyticsService.latest_traffic(),

            "traffic_history":
                AnalyticsService.traffic_history(),

            "notifications":
                DashboardService.notifications(),

            "recent_logs":
                DashboardService.logs(),

            "reports":
                DashboardService.reports(),

            "system":
                DashboardService.system_information()

        }

    ###########################################################
    # Notifications
    ###########################################################

    @staticmethod
    def notifications(limit=10):

        try:

            notifications = NotificationService.unread()

            return [

                notification.to_dict()

                for notification in notifications[:limit]

            ]

        except Exception:

            return []

    ###########################################################
    # Recent Logs
    ###########################################################

    @staticmethod
    def logs(limit=20):

        logs = Log.query.order_by(

            Log.created_at.desc()

        ).limit(limit).all()

        return [

            log.to_dict()

            for log in logs

        ]

    ###########################################################
    # Reports
    ###########################################################

    @staticmethod
    def reports():

        try:

            return ReportService.available_reports()

        except Exception:

            return []

    ###########################################################
    # System Information
    ###########################################################

    @staticmethod
    def system_information():

        return {

            "routers":

                Router.query.count(),

            "devices":

                Device.query.count(),

            "networks":

                Network.query.count(),

            "logs":

                Log.query.count(),

            "server_time":

                datetime.utcnow().isoformat(),

            "backend":

                "Running"

        }

    ###########################################################
    # Dashboard Refresh
    ###########################################################

    @staticmethod
    def refresh():

        return DashboardService.overview()