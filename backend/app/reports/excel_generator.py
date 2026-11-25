import os
from datetime import datetime

from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.styles import PatternFill

from app.reports.report_manager import ReportManager


class ExcelGenerator:

    REPORT_FOLDER = "reports"

    HEADER_FILL = PatternFill(

        fill_type="solid",

        fgColor="1F4E78"

    )

    HEADER_FONT = Font(

        bold=True,

        color="FFFFFF"

    )

    ###########################################################
    # GENERATE
    ###########################################################

    @classmethod
    def generate(cls):

        os.makedirs(

            cls.REPORT_FOLDER,

            exist_ok=True

        )

        filename = (

            f"wifi_report_"

            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

        )

        filepath = os.path.join(

            cls.REPORT_FOLDER,

            filename

        )

        report = ReportManager.generate()

        workbook = Workbook()

        cls.summary_sheet(

            workbook,

            report

        )

        cls.router_sheet(

            workbook,

            report

        )

        cls.network_sheet(

            workbook,

            report

        )

        cls.device_sheet(

            workbook,

            report

        )

        cls.traffic_sheet(

            workbook,

            report

        )

        cls.log_sheet(

            workbook,

            report

        )

        workbook.save(filepath)

        return {

            "filename": filename,

            "path": filepath

        }

    ###########################################################
    # STYLE
    ###########################################################

    @classmethod
    def style(cls, sheet):

        for cell in sheet[1]:

            cell.fill = cls.HEADER_FILL

            cell.font = cls.HEADER_FONT

    ###########################################################
    # SUMMARY
    ###########################################################

    @classmethod
    def summary_sheet(cls, workbook, report):

        sheet = workbook.active

        sheet.title = "Summary"

        sheet.append([

            "Metric",

            "Value"

        ])

        cls.style(sheet)

        for key, value in report["analytics"]["summary"].items():

            sheet.append([

                key.replace("_", " ").title(),

                value

            ])

    ###########################################################
    # ROUTERS
    ###########################################################

    @classmethod
    def router_sheet(cls, workbook, report):

        sheet = workbook.create_sheet("Routers")

        sheet.append([

            "Name",

            "IP Address",

            "CPU",

            "Memory",

            "Online"

        ])

        cls.style(sheet)

        for router in report["routers"]:

            sheet.append([

                router.get("name"),

                router.get("ip_address"),

                router.get("cpu_usage"),

                router.get("memory_usage"),

                router.get("is_online")

            ])

    ###########################################################
    # NETWORKS
    ###########################################################

    @classmethod
    def network_sheet(cls, workbook, report):

        sheet = workbook.create_sheet("Networks")

        sheet.append([

            "SSID",

            "Router",

            "Channel",

            "Band"

        ])

        cls.style(sheet)

        for network in report["networks"]:

            sheet.append([

                network.get("ssid"),

                network.get("router_name"),

                network.get("channel"),

                network.get("band")

            ])

    ###########################################################
    # DEVICES
    ###########################################################

    @classmethod
    def device_sheet(cls, workbook, report):

        sheet = workbook.create_sheet("Devices")

        sheet.append([

            "Hostname",

            "IP Address",

            "MAC",

            "Type"

        ])

        cls.style(sheet)

        for device in report["devices"]:

            sheet.append([

                device.get("hostname"),

                device.get("ip_address"),

                device.get("mac_address"),

                device.get("device_type")

            ])

    ###########################################################
    # TRAFFIC
    ###########################################################

    @classmethod
    def traffic_sheet(cls, workbook, report):

        sheet = workbook.create_sheet("Traffic")

        sheet.append([

            "Router",

            "Upload",

            "Download",

            "Utilization"

        ])

        cls.style(sheet)

        for row in report["traffic"]:

            sheet.append([

                row.get("router_id"),

                row.get("upload"),

                row.get("download"),

                row.get("utilization")

            ])

    ###########################################################
    # LOGS
    ###########################################################

    @classmethod
    def log_sheet(cls, workbook, report):

        sheet = workbook.create_sheet("Logs")

        sheet.append([

            "Module",

            "Action",

            "Status",

            "Time"

        ])

        cls.style(sheet)

        for log in report["logs"]:

            sheet.append([

                log.get("module"),

                log.get("action"),

                log.get("status"),

                log.get("created_at")

            ])