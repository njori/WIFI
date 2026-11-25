from datetime import datetime

from app.extensions import db


class Router(db.Model):
    __tablename__ = "routers"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(100),
        nullable=False
    )

    ip_address = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    mac_address = db.Column(
        db.String(50),
        unique=True
    )

    manufacturer = db.Column(db.String(50))

    model = db.Column(db.String(100))

    firmware_version = db.Column(db.String(100))

    serial_number = db.Column(db.String(100))

    location = db.Column(db.String(255))

    uptime = db.Column(
        db.Integer,
        default=0
    )

    cpu_usage = db.Column(
        db.Float,
        default=0
    )

    memory_usage = db.Column(
        db.Float,
        default=0
    )

    is_online = db.Column(
        db.Boolean,
        default=False
    )

    last_seen = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
    username = db.Column(

        db.String(100)

    )

    password = db.Column(

        db.String(255)

    )

    ssh_port = db.Column(

        db.Integer,

        default=22

    )

    # Relationships

    networks = db.relationship(
        "Network",
        back_populates="router",
        lazy=True,
        cascade="all, delete-orphan"
    )

    devices = db.relationship(
        "Device",
        back_populates="router",
        lazy=True,
        cascade="all, delete-orphan"
    )

    logs = db.relationship(
        "Log",
        back_populates="router",
        lazy=True,
        cascade="all, delete-orphan"
    )
    traffic = db.relationship(
        "Traffic",
        back_populates="router",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "ip_address": self.ip_address,
            "mac_address": self.mac_address,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "firmware_version": self.firmware_version,
            "serial_number": self.serial_number,
            "location": self.location,
            "uptime": self.uptime,
            "cpu_usage": self.cpu_usage,
            "memory_usage": self.memory_usage,
            "is_online": self.is_online,
            "last_seen": self.last_seen.isoformat() if self.last_seen else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }