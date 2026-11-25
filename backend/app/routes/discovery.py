from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from app.services.discovery_service import DiscoveryService

discovery_bp = Blueprint(
    "discovery",
    __name__,
    url_prefix="/api/discovery"
)


@discovery_bp.post("/scan")
@jwt_required()
def scan():

    result = DiscoveryService.scan(
        "192.168.0.0/24"
    )

    return jsonify(result), 200