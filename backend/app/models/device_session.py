from datetime import datetime
from app.extensions import db


class DeviceSession(db.Model):

    __tablename__ = "device_sessions"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    device_id = db.Column(
        db.Integer,
        db.ForeignKey("devices.id"),
        nullable=False
    )

    login_time = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    logout_time = db.Column(
        db.DateTime
    )

    duration = db.Column(
        db.Integer,
        default=0
    )

    upload = db.Column(
        db.Float,
        default=0
    )

    download = db.Column(
        db.Float,
        default=0
    )

    signal_strength = db.Column(
        db.Integer,
        default=0
    )

    connection_speed = db.Column(
        db.Float,
        default=0
    )

    device = db.relationship(
        "Device",
        backref="sessions"
    )

    def to_dict(self):

        return {

            "id": self.id,

            "device_id": self.device_id,

            "login_time": self.login_time.isoformat(),

            "logout_time": self.logout_time.isoformat()
            if self.logout_time else None,

            "duration": self.duration,

            "upload": self.upload,

            "download": self.download,

            "signal_strength": self.signal_strength,

            "connection_speed": self.connection_speed

        }