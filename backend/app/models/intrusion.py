from datetime import datetime

from app.extensions import db


class Intrusion(db.Model):
    __tablename__ = "intrusions"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    router_id = db.Column(
        db.Integer,
        db.ForeignKey("routers.id")
    )

    device_id = db.Column(
        db.Integer,
        db.ForeignKey("devices.id")
    )

    severity = db.Column(
        db.String(20),
        default="warning"
    )

    attack_type = db.Column(
        db.String(100)
    )

    message = db.Column(
        db.Text
    )

    resolved = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    router = db.relationship(
        "Router",
        backref="intrusions"
    )

    device = db.relationship(
        "Device",
        backref="intrusions"
    )

    def to_dict(self):

        return {

            "id": self.id,

            "router_id": self.router_id,

            "device_id": self.device_id,

            "severity": self.severity,

            "attack_type": self.attack_type,

            "message": self.message,

            "resolved": self.resolved,

            "created_at": self.created_at.isoformat()
        }