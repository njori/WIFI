import os
from datetime import datetime

from app.services.report_service import ReportService
from app.services.email_service import EmailService


class ScheduledReportService:

    REPORT_FOLDER = "reports"

    ############################################################
    # Daily Report
    ############################################################

    @classmethod
    def daily(cls):

        report = ReportService.generate_pdf()

        EmailService.send_report(

            subject="Daily WiFi Network Report",

            body="Attached is today's network report.",

            attachment=report["path"]

        )

        return report

    ############################################################
    # Weekly Report
    ############################################################

    @classmethod
    def weekly(cls):

        report = ReportService.generate_excel()

        EmailService.send_report(

            subject="Weekly WiFi Network Report",

            body="Attached is the weekly report.",

            attachment=report["path"]

        )

        return report

    ############################################################
    # Monthly Report
    ############################################################

    @classmethod
    def monthly(cls):

        report = ReportService.generate_pdf()

        EmailService.send_report(

            subject="Monthly WiFi Network Report",

            body="Attached is the monthly report.",

            attachment=report["path"]

        )

        return report

    ############################################################
    # Cleanup Old Reports
    ############################################################

    @classmethod
    def cleanup(cls, keep_days=30):

        if not os.path.exists(cls.REPORT_FOLDER):

            return

        now = datetime.now()

        for file in os.listdir(cls.REPORT_FOLDER):

            path = os.path.join(

                cls.REPORT_FOLDER,

                file

            )

            if not os.path.isfile(path):

                continue

            age = (

                now -

                datetime.fromtimestamp(

                    os.path.getmtime(path)

                )

            ).days

            if age > keep_days:

                os.remove(path)