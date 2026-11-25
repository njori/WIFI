from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from app.services.log_service import LogService

log_bp = Blueprint(
    "logs",
    __name__,
    url_prefix="/api/logs"
)

@log_bp.get("")
@jwt_required()
def get_logs():

    logs = LogService.all()

    return jsonify([
        log.to_dict()
        for log in logs
    ])

@log_bp.get("/recent")
@jwt_required()
def recent_logs():

    logs = LogService.recent()

    return jsonify([
        log.to_dict()
        for log in logs
    ])