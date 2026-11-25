from flask import Blueprint
from flask import jsonify

from flask_jwt_extended import jwt_required

from app.services.analytics_service import AnalyticsService
from app.services.dashboard_service import DashboardService

analytics_bp = Blueprint(
    "analytics",
    __name__,
    url_prefix="/api/analytics"
)

##############################################################
# Dashboard Overview
##############################################################

@analytics_bp.get("/dashboard")
@jwt_required()
def dashboard():

    return jsonify(

        DashboardService.overview()

    )

##############################################################
# Dashboard Summary
##############################################################

@analytics_bp.get("/summary")
@jwt_required()
def summary():

    return jsonify(

        AnalyticsService.summary()

    )

##############################################################
# CPU
##############################################################

@analytics_bp.get("/cpu")
@jwt_required()
def cpu():

    return jsonify(

        AnalyticsService.cpu()

    )

##############################################################
# Memory
##############################################################

@analytics_bp.get("/memory")
@jwt_required()
def memory():

    return jsonify(

        AnalyticsService.memory()

    )

##############################################################
# Network Health
##############################################################

@analytics_bp.get("/health")
@jwt_required()
def health():

    return jsonify(

        AnalyticsService.health()

    )

##############################################################
# Bandwidth
##############################################################

@analytics_bp.get("/bandwidth")
@jwt_required()
def bandwidth():

    return jsonify(

        AnalyticsService.bandwidth()

    )

##############################################################
# Top Routers
##############################################################

@analytics_bp.get("/routers")
@jwt_required()
def top_routers():

    return jsonify(

        AnalyticsService.top_routers()

    )

##############################################################
# Top Devices
##############################################################

@analytics_bp.get("/devices")
@jwt_required()
def top_devices():

    return jsonify(

        AnalyticsService.top_devices()

    )

##############################################################
# Top Networks
##############################################################

@analytics_bp.get("/networks")
@jwt_required()
def top_networks():

    return jsonify(

        AnalyticsService.top_networks()

    )

##############################################################
# Latest Traffic
##############################################################

@analytics_bp.get("/traffic")
@jwt_required()
def latest_traffic():

    return jsonify(

        AnalyticsService.latest_traffic()

    )

##############################################################
# Historical Traffic
##############################################################

@analytics_bp.get("/traffic/history")
@jwt_required()
def traffic_history():

    return jsonify(

        AnalyticsService.traffic_history()

    )

##############################################################
# Device Types
##############################################################

@analytics_bp.get("/device-types")
@jwt_required()
def device_types():

    return jsonify(

        AnalyticsService.device_types()

    )