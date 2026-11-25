import random


class SNMPClient:

    def __init__(self, host, community="public", port=161):
        self.host = host

    def get(self, oid):

        # 10% chance the router is offline
        if random.randint(1, 10) == 1:
            raise Exception("Router Offline")

        fake_data = {
            "1.3.6.1.2.1.1.5.0":
                f"Router-{self.host.split('.')[-1]}",

            "1.3.6.1.2.1.1.1.0":
                "MikroTik RouterOS 7.18",

            "1.3.6.1.2.1.1.3.0":
                random.randint(10000, 900000),

            "1.3.6.1.4.1.2021.11.11.0":
                random.randint(5, 95),

            "1.3.6.1.4.1.2021.4.6.0":
                random.randint(20, 95),
        }

        return fake_data[oid]