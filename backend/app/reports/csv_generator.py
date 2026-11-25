import csv
import os
from datetime import datetime

from app.reports.report_manager import ReportManager


class CSVGenerator:

    REPORT_FOLDER = "reports"

    @classmethod
    def generate(cls):

        os.makedirs(cls.REPORT_FOLDER, exist_ok=True)

        filename = (
            f"wifi_report_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )

        filepath = os.path.join(
            cls.REPORT_FOLDER,
            filename
        )

        report = ReportManager.generate()

        with open(
            filepath,
            "w",
            newline="",
            encoding="utf-8"
        ) as csvfile:

            writer = csv.writer(csvfile)

            ####################################################
            # SUMMARY
            ####################################################

            writer.writerow(["SYSTEM SUMMARY"])
            writer.writerow([])

            writer.writerow(["Metric", "Value"])

            summary = report["analytics"]["summary"]

            for key, value in summary.items():

                writer.writerow([key, value])

            writer.writerow([])
            writer.writerow([])

            ####################################################
            # ROUTERS
            ####################################################

            writer.writerow(["ROUTERS"])

            writer.writerow([
                "Name",
                "IP",
                "CPU",
                "Memory",
                "Online"
            ])

            for router in report["routers"]:

                writer.writerow([

                    router["name"],

                    router["ip_address"],

                    router["cpu_usage"],

                    router["memory_usage"],

                    router["is_online"]

                ])

            writer.writerow([])
            writer.writerow([])

            ####################################################
            # NETWORKS
            ####################################################

            writer.writerow(["NETWORKS"])

            writer.writerow([

                "SSID",

                "Router",

                "Band",

                "Channel",

                "Clients"

            ])

            for network in report["networks"]:

                writer.writerow([

                    network["ssid"],

                    network["router_name"],

                    network["band"],

                    network["channel"],

                    network["device_count"]

                ])

            writer.writerow([])
            writer.writerow([])

            ####################################################
            # DEVICES
            ####################################################

            writer.writerow(["DEVICES"])

            writer.writerow([

                "Hostname",

                "IP",

                "MAC",

                "Type",

                "Connected"

            ])

            for device in report["devices"]:

                writer.writerow([

                    device["hostname"],

                    device["ip_address"],

                    device["mac_address"],

                    device["device_type"],

                    device["is_connected"]

                ])

        return {

            "filename": filename,

            "path": filepath

        }