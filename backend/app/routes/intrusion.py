from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from app.repositories.intrusion_repository import IntrusionRepository

intrusion_bp = Blueprint(
    "intrusions",
    __name__,
    url_prefix="/api/intrusions"
)


@intrusion_bp.get("")
@jwt_required()
def all_intrusions():

    return jsonify([
        intrusion.to_dict()
        for intrusion in IntrusionRepository.get_all()
    ])


@intrusion_bp.get("/unresolved")
@jwt_required()
def unresolved():

    return jsonify([
        intrusion.to_dict()
        for intrusion in IntrusionRepository.unresolved()
    ])