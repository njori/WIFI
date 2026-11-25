from app.snmp.client import SNMPClient
from app.snmp import oids


class SNMPMonitor:

    @staticmethod
    def get_hostname(ip):
        return SNMPClient(ip).get(oids.SYS_NAME)

    @staticmethod
    def get_description(ip):
        return SNMPClient(ip).get(oids.SYS_DESCRIPTION)

    @staticmethod
    def get_uptime(ip):
        return int(SNMPClient(ip).get(oids.SYS_UPTIME))

    @staticmethod
    def get_cpu(ip):
        return float(SNMPClient(ip).get(oids.CPU_USAGE))

    @staticmethod
    def get_memory(ip):
        return float(SNMPClient(ip).get(oids.MEMORY_USAGE))

    @staticmethod
    def get_interface_statistics(ip):

        import random

        return {

            "interface": "ether1",

            "bytes_in": random.randint(1000000, 5000000),

            "bytes_out": random.randint(1000000, 5000000),

            "packets_in": random.randint(10000, 50000),

            "packets_out": random.randint(10000, 50000),

            "upload": round(random.uniform(5, 100), 2),

            "download": round(random.uniform(5, 100), 2),

            "utilization": round(random.uniform(10, 95), 2)

        }