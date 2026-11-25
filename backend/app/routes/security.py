from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

security_bp = Blueprint(
    "security",
    __name__,
    url_prefix="/api/security"
)


@security_bp.get("/settings")
def settings():
    return jsonify({
        "status": "healthy",
        "module": "Enterprise Security",
        "version": "1.0",
        "settings": {
            "alerts_enabled": True,
            "threat_detection": True,
            "auto_block": True,
        }
    })


@security_bp.get("/status")
@jwt_required()
def status():

    return jsonify({

        "status": "Intrusion Detection Active",

        "checks": [

            "Unknown Devices",

            "Duplicate IP",

            "Duplicate MAC",

            "Router Offline",

            "High CPU",

            "High Memory",

            "Bandwidth Monitoring"

        ]

    })