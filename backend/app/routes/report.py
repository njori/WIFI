from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from app.services.report_service import ReportService
from app.services.scheduled_report_service import ScheduledReportService


report_bp = Blueprint(
    "reports",
    __name__,
    url_prefix="/api/reports"
)


@report_bp.get("/pdf")
@jwt_required()
def generate_pdf():

    return jsonify(

        ReportService.generate_pdf()

    )


@report_bp.get("/excel")
@jwt_required()
def generate_excel():

    return jsonify(

        ReportService.generate_excel()

    )

@report_bp.post("/daily")
@jwt_required()
def run_daily():

    return jsonify(

        ScheduledReportService.daily()

    )


@report_bp.post("/weekly")
@jwt_required()
def run_weekly():

    return jsonify(

        ScheduledReportService.weekly()

    )


@report_bp.post("/monthly")
@jwt_required()
def run_monthly():

    return jsonify(

        ScheduledReportService.monthly()

    )