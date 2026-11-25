from flask import Blueprint, request

from flask_jwt_extended import jwt_required

from app.services.router_service import RouterService
from app.utils.responses import success
from app.middleware.roles import roles_required
from app.utils.roles import UserRole

router_bp = Blueprint(
    "router",
    __name__,
    url_prefix="/api/routers"
)


@router_bp.get("")
@jwt_required()
def get_routers():

    return success(
        data=RouterService.all()
    )


@router_bp.post("")
@jwt_required()
@roles_required(
    UserRole.ADMIN.value,
    UserRole.MANAGER.value,
    UserRole.TECHNICIAN.value
)
def create_router():

    router = RouterService.create(
        request.json
    )

    return success(
        "Router created successfully.",
        router.to_dict(),
        201
    )