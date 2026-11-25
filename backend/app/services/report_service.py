import os

from app.models.report import Report
from app.repositories.report_repository import ReportRepository

from app.reports.report_manager import ReportManager
from app.reports.pdf_generator import PDFGenerator
from app.reports.excel_generator import ExcelGenerator
from app.reports.csv_generator import CSVGenerator
from app.reports.json_generator import JSONGenerator


class ReportService:

    REPORT_FOLDER = "reports"

    ###########################################################
    # DASHBOARD REPORT
    ###########################################################

    @staticmethod
    def dashboard_report():

        return ReportManager.generate()

    ###########################################################
    # PDF
    ###########################################################

    @staticmethod
    def generate_pdf():

        result = PDFGenerator.generate()

        return ReportService.save_report(
            "PDF Network Report",
            "pdf",
            result
        )

    ###########################################################
    # EXCEL
    ###########################################################

    @staticmethod
    def generate_excel():

        result = ExcelGenerator.generate()

        return ReportService.save_report(
            "Excel Network Report",
            "excel",
            result
        )

    ###########################################################
    # CSV
    ###########################################################

    @staticmethod
    def generate_csv():

        result = CSVGenerator.generate()

        return ReportService.save_report(
            "CSV Network Report",
            "csv",
            result
        )

    ###########################################################
    # JSON
    ###########################################################

    @staticmethod
    def generate_json():

        result = JSONGenerator.generate()

        return ReportService.save_report(
            "JSON Network Report",
            "json",
            result
        )

    ###########################################################
    # GENERIC REPORT
    ###########################################################

    @staticmethod
    def generate(report_type):

        report_type = report_type.lower()

        if report_type == "pdf":
            return ReportService.generate_pdf()

        elif report_type == "excel":
            return ReportService.generate_excel()

        elif report_type == "csv":
            return ReportService.generate_csv()

        elif report_type == "json":
            return ReportService.generate_json()

        raise Exception("Unsupported report type.")

    ###########################################################
    # SAVE REPORT
    ###########################################################

    @staticmethod
    def save_report(title, report_type, result):

        report = Report(

            title=title,

            report_type=report_type,

            file_name=result["filename"]

        )

        ReportRepository.create(report)

        return {

            "message": f"{report_type.upper()} report generated successfully.",

            "report": report.to_dict(),

            "file": result

        }

    ###########################################################
    # HISTORY
    ###########################################################

    @staticmethod
    def history():

        reports = ReportRepository.latest()

        return [

            report.to_dict()

            for report in reports

        ]

    ###########################################################
    # AVAILABLE REPORTS
    ###########################################################

    @staticmethod
    def available_reports():

        if not os.path.exists(

            ReportService.REPORT_FOLDER

        ):

            return []

        reports = []

        for filename in os.listdir(

            ReportService.REPORT_FOLDER

        ):

            reports.append({

                "name": filename,

                "path": os.path.join(

                    ReportService.REPORT_FOLDER,

                    filename

                )

            })

        return reports