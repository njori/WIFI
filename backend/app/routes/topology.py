from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from app.services.topology_service import TopologyService

topology_bp = Blueprint(
    "topology",
    __name__,
    url_prefix="/api/topology"
)


@topology_bp.get("/")
@jwt_required()
def topology():

    return jsonify(
        TopologyService.generate()
    )