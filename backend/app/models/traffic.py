from datetime import datetime

from app.extensions import db


class Traffic(db.Model):
    __tablename__ = "traffic"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    router_id = db.Column(
        db.Integer,
        db.ForeignKey("routers.id"),
        nullable=False
    )

    interface = db.Column(
        db.String(100),
        nullable=False
    )

    bytes_in = db.Column(
        db.BigInteger,
        default=0
    )

    bytes_out = db.Column(
        db.BigInteger,
        default=0
    )

    packets_in = db.Column(
        db.BigInteger,
        default=0
    )

    packets_out = db.Column(
        db.BigInteger,
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

    utilization = db.Column(
        db.Float,
        default=0
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    router = db.relationship(
        "Router",
        back_populates="traffic"
    )

    def to_dict(self):

        return {

            "id": self.id,

            "router_id": self.router_id,

            "interface": self.interface,

            "bytes_in": self.bytes_in,

            "bytes_out": self.bytes_out,

            "packets_in": self.packets_in,

            "packets_out": self.packets_out,

            "upload": self.upload,

            "download": self.download,

            "utilization": self.utilization,

            "created_at": self.created_at.isoformat()
        }