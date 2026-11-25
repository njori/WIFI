from flask import Blueprint, request

from flask_jwt_extended import jwt_required

from app.services.network_service import NetworkService
from app.utils.responses import success

network_bp = Blueprint(
    "network",
    __name__,
    url_prefix="/api/networks"
)


@network_bp.get("")
@jwt_required()
def get_networks():

    return success(
        data=NetworkService.all()
    )


@network_bp.post("")
@jwt_required()
def create_network():

    network = NetworkService.create(
        request.json
    )

    return success(
        "Network created successfully.",
        network.to_dict(),
        201
    )