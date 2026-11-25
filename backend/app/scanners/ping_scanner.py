import platform
import subprocess


class PingScanner:

    @staticmethod
    def ping(ip):

        if platform.system().lower() == "windows":

            command = [
                "ping",
                "-n",
                "1",
                "-w",
                "500",
                ip
            ]

        else:

            command = [
                "ping",
                "-c",
                "1",
                "-W",
                "1",
                ip
            ]

        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return result.returncode == 0