import json
import os


class VendorLookup:

    def __init__(self):

        file_path = os.path.join(
            os.path.dirname(__file__),
            "vendors.json"
        )

        with open(file_path, "r", encoding="utf-8") as file:
            self.vendors = json.load(file)

    def lookup(self, mac):

        if not mac:
            return "Unknown"

        prefix = mac.upper().replace(":", "")[:6]

        return self.vendors.get(
            prefix,
            "Unknown"
        )