class RouterCommands:

    @staticmethod
    def reboot():

        return "system reboot"

    @staticmethod
    def backup():

        return "export"

    @staticmethod
    def interfaces():

        return "interface print"

    @staticmethod
    def ip_addresses():

        return "ip address print"

    @staticmethod
    def routes():

        return "ip route print"

    @staticmethod
    def users():

        return "user print"

    @staticmethod
    def firewall():

        return "ip firewall filter print"

    @staticmethod
    def version():

        return "system resource print"