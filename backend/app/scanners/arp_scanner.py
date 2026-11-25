from scapy.all import ARP, Ether, srp


class ARPScanner:

    @staticmethod
    def scan(network):

        packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(
            pdst=network
        )

        answered, unanswered = srp(
            packet,
            timeout=2,
            verbose=False
        )

        devices = []

        for sent, received in answered:

            devices.append({
                "ip_address": received.psrc,
                "mac_address": received.hwsrc
            })

        return devices