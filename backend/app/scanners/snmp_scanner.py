import random


class SNMPScanner:

    @staticmethod
    def scan(ip):

        return {
            "ip_address": ip,
            "hostname": f"Router-{ip.split('.')[-1]}",
            "manufacturer": random.choice([
                "MikroTik",
                "Cisco",
                "Ubiquiti",
                "TP-Link"
            ]),
            "model": random.choice([
                "RB4011",
                "CCR1009",
                "EdgeRouter X",
                "Archer C80"
            ]),
            "status": "online"
        }