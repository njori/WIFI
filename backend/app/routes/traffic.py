from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.services.traffic_service import TrafficService

traffic_bp = Blueprint(
    "traffic",
    __name__,
    url_prefix="/api/traffic"
)


@traffic_bp.get("")
@jwt_required()
def latest():

    traffic = TrafficService.latest()

    return [

        item.to_dict()

        for item in traffic

    ]


@traffic_bp.get("/router/<int:router_id>")
@jwt_required()
def history(router_id):

    history = TrafficService.router_history(
        router_id
    )

    return [

        item.to_dict()

        for item in history

    ]