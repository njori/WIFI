from datetime import datetime
from app.extensions import db


class Notification(db.Model):

    __tablename__ = "notifications"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(150),
        nullable=False
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    category = db.Column(
        db.String(50),
        default="System"
    )

    priority = db.Column(
        db.String(20),
        default="info"
    )

    is_read = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=True
    )

    def to_dict(self):

        return {

            "id": self.id,

            "title": self.title,

            "message": self.message,

            "category": self.category,

            "priority": self.priority,

            "is_read": self.is_read,

            "user_id": self.user_id,

            "created_at": self.created_at.isoformat()

        }