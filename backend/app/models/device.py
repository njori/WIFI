from datetime import datetime, timezone

from app.extensions import db


def utcnow():
    return datetime.now(timezone.utc)


class Device(db.Model):
    __tablename__ = "devices"

    id = db.Column(db.Integer, primary_key=True)

    mac_address = db.Column(
        db.String(17),
        unique=True,
        nullable=False,
        index=True
    )

    ip_address = db.Column(
        db.String(45),
        nullable=False
    )

    hostname = db.Column(db.String(100))

    device_name = db.Column(db.String(100))

    manufacturer = db.Column(db.String(100))

    operating_system = db.Column(db.String(100))

    device_type = db.Column(db.String(50))

    signal_strength = db.Column(db.Integer)

    connection_speed = db.Column(db.Float)

    upload_speed = db.Column(
        db.Float,
        default=0
    )

    download_speed = db.Column(
        db.Float,
        default=0
    )

    bytes_sent = db.Column(
        db.BigInteger,
        default=0
    )

    bytes_received = db.Column(
        db.BigInteger,
        default=0
    )

    is_connected = db.Column(
        db.Boolean,
        default=True
    )

    network_id = db.Column(
        db.Integer,
        db.ForeignKey("networks.id"),
        nullable=False
    )

    router_id = db.Column(
        db.Integer,
        db.ForeignKey("routers.id")
    )

    last_seen = db.Column(
        db.DateTime,
        default=utcnow
    )

    created_at = db.Column(
        db.DateTime,
        default=utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=utcnow,
        onupdate=utcnow
    )

    # Relationships

    network = db.relationship(
        "Network",
        back_populates="devices"
    )

    router = db.relationship(
        "Router",
        back_populates="devices"
    )

    logs = db.relationship(
        "Log",
        back_populates="device",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "mac_address": self.mac_address,
            "ip_address": self.ip_address,
            "hostname": self.hostname,
            "device_name": self.device_name,
            "manufacturer": self.manufacturer,
            "operating_system": self.operating_system,
            "device_type": self.device_type,
            "signal_strength": self.signal_strength,
            "connection_speed": self.connection_speed,
            "upload_speed": self.upload_speed,
            "download_speed": self.download_speed,
            "bytes_sent": self.bytes_sent,
            "bytes_received": self.bytes_received,
            "is_connected": self.is_connected,
            "network_id": self.network_id,
            "router_id": self.router_id,
            "last_seen": self.last_seen.isoformat() if self.last_seen else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }