class VendorService:
    """
    Simple vendor lookup service.
    Replace this later with a real IEEE OUI lookup.
    """

    OUI_DATABASE = {
        "00:50:56": "VMware",
        "00:1A:2B": "Cisco",
        "00:0C:29": "VMware",
        "3C:52:82": "Apple",
        "B8:27:EB": "Raspberry Pi",
        "FC:FB:FB": "Google",
        "F4:F5:D8": "Ubiquiti",
        "D8:47:32": "TP-Link",
        "A4:2B:B0": "MikroTik",
    }

    @classmethod
    def lookup(cls, mac_address):

        if not mac_address:
            return "Unknown"

        prefix = mac_address.upper().replace("-", ":")[:8]

        return cls.OUI_DATABASE.get(prefix, "Unknown")