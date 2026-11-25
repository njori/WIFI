from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from app.services.router_monitor_service import RouterMonitorService

monitor_bp = Blueprint(
    "monitor",
    __name__,
    url_prefix="/api/monitor"
)


@monitor_bp.get("/routers")
@jwt_required()
def monitor():

    return jsonify(

        RouterMonitorService.monitor()

    )