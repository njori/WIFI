from flask import Blueprint

from flask_jwt_extended import jwt_required

from app.services.dashboard_service import DashboardService
from app.utils.responses import success

dashboard_bp = Blueprint(
    "dashboard",
    __name__,
    url_prefix="/api/dashboard"
)


@dashboard_bp.get("/overview")
@jwt_required()
def overview():

    data = DashboardService.overview()

    return success(
        "Dashboard loaded successfully.",
        data
    )