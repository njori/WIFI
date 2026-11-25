import os
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)

from app.reports.report_manager import ReportManager


class PDFGenerator:

    REPORT_FOLDER = "reports"

    @classmethod
    def generate(cls):

        os.makedirs(cls.REPORT_FOLDER, exist_ok=True)

        filename = f"wifi_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

        filepath = os.path.join(

            cls.REPORT_FOLDER,

            filename

        )

        report = ReportManager.generate()

        doc = SimpleDocTemplate(filepath)

        styles = getSampleStyleSheet()

        elements = []

        ####################################################
        # Title
        ####################################################

        elements.append(

            Paragraph(

                "<b>WiFi Management System Report</b>",

                styles["Title"]

            )

        )

        elements.append(

            Paragraph(

                f"Generated: {report['generated_at']}",

                styles["Normal"]

            )

        )

        elements.append(

            Spacer(1, 0.3 * inch)

        )

        ####################################################
        # Summary
        ####################################################

        summary = report["analytics"]["summary"]

        data = [

            ["Metric", "Value"],

            ["Routers", summary["routers"]],

            ["Online Routers", summary["online_routers"]],

            ["Offline Routers", summary["offline_routers"]],

            ["Networks", summary["networks"]],

            ["Devices", summary["devices"]],

            ["Connected Devices", summary["connected_devices"]],

            ["Disconnected Devices", summary["disconnected_devices"]]

        ]

        table = Table(data)

        table.setStyle(

            TableStyle([

                ("BACKGROUND", (0,0), (-1,0), colors.darkblue),

                ("TEXTCOLOR", (0,0), (-1,0), colors.white),

                ("GRID", (0,0), (-1,-1), 1, colors.grey),

                ("BACKGROUND", (0,1), (-1,-1), colors.beige),

                ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

                ("BOTTOMPADDING", (0,0), (-1,0), 8)

            ])

        )

        elements.append(table)

        elements.append(Spacer(1, 0.4 * inch))

        ####################################################
        # Router Table
        ####################################################

        elements.append(

            Paragraph(

                "<b>Routers</b>",

                styles["Heading2"]

            )

        )

        router_table = [

            [

                "Name",

                "IP",

                "CPU",

                "Memory",

                "Online"

            ]

        ]

        for router in report["routers"]:

            router_table.append([

                router["name"],

                router["ip_address"],

                f"{router['cpu_usage']}%",

                f"{router['memory_usage']}%",

                "Yes" if router["is_online"] else "No"

            ])

        table = Table(router_table)

        table.setStyle(

            TableStyle([

                ("GRID",(0,0),(-1,-1),1,colors.grey),

                ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),

                ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")

            ])

        )

        elements.append(table)

        elements.append(Spacer(1, 0.4 * inch))

        ####################################################
        # Networks
        ####################################################

        elements.append(

            Paragraph(

                "<b>Networks</b>",

                styles["Heading2"]

            )

        )

        network_table = [

            [

                "SSID",

                "Router",

                "Channel",

                "Band",

                "Clients"

            ]

        ]

        for network in report["networks"]:

            network_table.append([

                network["ssid"],

                network["router_name"],

                network["channel"],

                network["band"],

                network["device_count"]

            ])

        table = Table(network_table)

        table.setStyle(

            TableStyle([

                ("GRID",(0,0),(-1,-1),1,colors.grey),

                ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),

                ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")

            ])

        )

        elements.append(table)

        elements.append(Spacer(1, 0.4 * inch))

        ####################################################
        # Devices
        ####################################################

        elements.append(

            Paragraph(

                "<b>Connected Devices</b>",

                styles["Heading2"]

            )

        )

        device_table = [

            [

                "Hostname",

                "IP",

                "MAC",

                "Type",

                "Connected"

            ]

        ]

        for device in report["devices"]:

            device_table.append([

                device["hostname"],

                device["ip_address"],

                device["mac_address"],

                device["device_type"],

                "Yes" if device["is_connected"] else "No"

            ])

        table = Table(device_table)

        table.setStyle(

            TableStyle([

                ("GRID",(0,0),(-1,-1),1,colors.grey),

                ("BACKGROUND",(0,0),(-1,0),colors.lightgrey),

                ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold")

            ])

        )

        elements.append(table)

        ####################################################
        # Footer
        ####################################################

        elements.append(

            Spacer(1,0.5*inch)

        )

        elements.append(

            Paragraph(

                "Generated automatically by WiFi Management System",

                styles["Italic"]

            )

        )

        doc.build(elements)

        return {

            "filename": filename,

            "path": filepath

        }