
class DeviceClassifier:
    """
    Classifies a device based on hostname and manufacturer.
    """

    @staticmethod
    def classify(hostname=None, manufacturer=None):

        hostname = (hostname or "").lower()
        manufacturer = (manufacturer or "").lower()

        # Routers
        if any(word in hostname for word in [
            "router", "gateway", "mikrotik", "ubnt", "ubiquiti", "tp-link"
        ]):
            return "Router"

        # Switches
        if any(word in hostname for word in [
            "switch", "cisco", "hp", "aruba"
        ]):
            return "Switch"

        # Access Points
        if any(word in hostname for word in [
            "ap", "accesspoint", "wifi", "wireless"
        ]):
            return "Access Point"

        # Printers
        if any(word in hostname for word in [
            "printer", "hp", "epson", "canon", "brother"
        ]):
            return "Printer"

        # Phones
        if any(word in manufacturer for word in [
            "apple", "samsung", "xiaomi", "huawei", "oppo", "tecno", "infinix"
        ]):
            return "Phone"

        # Computers
        if any(word in manufacturer for word in [
            "dell", "hp", "lenovo", "asus", "acer", "msi"
        ]):
            return "Computer"

        # Virtual Machines
        if any(word in manufacturer for word in [
            "vmware", "virtualbox", "oracle"
        ]):
            return "Virtual Machine"

        return "Unknown"