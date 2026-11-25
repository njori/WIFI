from datetime import datetime

from app.extensions import db


class Network(db.Model):
    __tablename__ = "networks"

    id = db.Column(db.Integer, primary_key=True)

    router_id = db.Column(
        db.Integer,
        db.ForeignKey("routers.id"),
        nullable=False
    )

    ssid = db.Column(db.String(100), nullable=False)

    bssid = db.Column(db.String(17), unique=True)

    password = db.Column(db.String(255))

    security_type = db.Column(
        db.String(30),
        default="WPA2"
    )

    channel = db.Column(db.Integer)

    band = db.Column(
        db.String(20),
        default="2.4GHz"
    )

    vlan = db.Column(db.Integer)

    max_clients = db.Column(
        db.Integer,
        default=50
    )

    bandwidth_limit = db.Column(db.Integer)

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    last_seen = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    description = db.Column(db.Text)

    # Relationships

    router = db.relationship(
        "Router",
        back_populates="networks"
    )

    devices = db.relationship(
        "Device",
        back_populates="network",
        lazy=True,
        cascade="all, delete-orphan"
    )

    logs = db.relationship(
        "Log",
        back_populates="network",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "router_id": self.router_id,
            "ssid": self.ssid,
            "bssid": self.bssid,
            "password": self.password,
            "security_type": self.security_type,
            "channel": self.channel,
            "band": self.band,
            "vlan": self.vlan,
            "max_clients": self.max_clients,
            "bandwidth_limit": self.bandwidth_limit,
            "is_active": self.is_active,
            "description": self.description,
            "last_seen": self.last_seen.isoformat() if self.last_seen else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "router_name": self.router.name if self.router else None,
            "device_count": len(self.devices)
        }