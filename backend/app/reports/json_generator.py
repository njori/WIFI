import json
import os
from datetime import datetime

from app.reports.report_manager import ReportManager


class JSONGenerator:

    REPORT_FOLDER = "reports"

    @classmethod
    def generate(cls):

        os.makedirs(cls.REPORT_FOLDER, exist_ok=True)

        filename = (
            f"wifi_report_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )

        filepath = os.path.join(
            cls.REPORT_FOLDER,
            filename
        )

        report = ReportManager.generate()

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(

                report,

                f,

                indent=4

            )

        return {

            "filename": filename,

            "path": filepath

        }