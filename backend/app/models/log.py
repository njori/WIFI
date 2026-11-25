from datetime import datetime, timezone
from app.extensions import db


def utcnow():
    return datetime.now(timezone.utc)


class Log(db.Model):
    __tablename__ = "logs"

    id = db.Column(db.Integer, primary_key=True)

    module = db.Column(db.String(50), nullable=False)

    action = db.Column(db.String(50), nullable=False)

    message = db.Column(db.Text)

    status = db.Column(db.String(20), default="success")

    ip_address = db.Column(db.String(45))

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    router_id = db.Column(
        db.Integer,
        db.ForeignKey("routers.id")
    )

    network_id = db.Column(
        db.Integer,
        db.ForeignKey("networks.id")
    )

    device_id = db.Column(
        db.Integer,
        db.ForeignKey("devices.id")
    )

    created_at = db.Column(
        db.DateTime,
        default=utcnow,
        index=True
    )

    user = db.relationship(
        "User",
        back_populates="logs"
    )

    router = db.relationship(
        "Router",
        back_populates="logs"
    )

    network = db.relationship(
        "Network",
        back_populates="logs"
    )

    device = db.relationship(
        "Device",
        back_populates="logs"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "module": self.module,
            "action": self.action,
            "message": self.message,
            "status": self.status,
            "ip_address": self.ip_address,
            "user_id": self.user_id,
            "router_id": self.router_id,
            "network_id": self.network_id,
            "device_id": self.device_id,
            "created_at": self.created_at.isoformat(),
        }