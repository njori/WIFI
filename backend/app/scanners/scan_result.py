from datetime import datetime


class ScanResult:

    def __init__(self):

        self.started = datetime.utcnow()
        self.finished = None
        self.total_hosts = 0
        self.online_hosts = 0
        self.offline_hosts = 0
        self.devices = []

    def finish(self):

        self.finished = datetime.utcnow()

    @property
    def duration(self):

        if self.finished:

            return (
                self.finished - self.started
            ).total_seconds()

        return 0

    def to_dict(self):

        return {
            "started": self.started.isoformat(),
            "finished": self.finished.isoformat()
            if self.finished else None,
            "duration": self.duration,
            "total_hosts": self.total_hosts,
            "online_hosts": self.online_hosts,
            "offline_hosts": self.offline_hosts,
            "devices": self.devices
        }