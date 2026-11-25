import ipaddress
from concurrent.futures import ThreadPoolExecutor, as_completed

from app.scanners.ping_scanner import PingScanner


class NetworkScanner:

    MAX_THREADS = 100

    @classmethod
    def scan(cls, network):

        subnet = ipaddress.ip_network(network, strict=False)

        online_hosts = []

        with ThreadPoolExecutor(max_workers=cls.MAX_THREADS) as executor:

            futures = {
                executor.submit(
                    PingScanner.ping,
                    str(ip)
                ): str(ip)
                for ip in subnet.hosts()
            }

            for future in as_completed(futures):

                ip = futures[future]

                try:

                    if future.result():

                        online_hosts.append(ip)

                except Exception as e:

                    print(f"Error scanning {ip}: {e}")

        return sorted(online_hosts)