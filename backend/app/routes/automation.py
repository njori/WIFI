from flask import Blueprint
from flask import jsonify
from flask import request

from flask_jwt_extended import jwt_required

from app.services.automation_service import AutomationService

automation_bp = Blueprint(

    "automation",

    __name__,

    url_prefix="/api/automation"

)


@automation_bp.post("/execute")
@jwt_required()
def execute():

    data = request.json

    result = AutomationService.execute(

        data["router_id"],

        data["command"]

    )

    return jsonify(result)