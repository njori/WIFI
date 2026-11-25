from datetime import datetime
from app.extensions import db


class Permission(db.Model):

    __tablename__ = "permissions"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    role = db.Column(
        db.String(50),
        nullable=False
    )

    resource = db.Column(
        db.String(100),
        nullable=False
    )

    action = db.Column(
        db.String(50),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):

        return {

            "id": self.id,

            "role": self.role,

            "resource": self.resource,

            "action": self.action

        }