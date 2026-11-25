class DeviceClassifier:

    ROUTERS = [
        "Cisco",
        "MikroTik",
        "TP-Link",
        "Ubiquiti",
        "Huawei"
    ]

    @staticmethod
    def classify(manufacturer):

        if manufacturer in DeviceClassifier.ROUTERS:
            return "Router"

        if manufacturer == "Apple":
            return "Phone"

        if manufacturer == "Dell":
            return "Computer"

        if manufacturer == "HP":
            return "Printer"

        if manufacturer == "Samsung":
            return "Phone"

        return "Unknown"