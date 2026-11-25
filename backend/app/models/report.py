from datetime import datetime

from app.extensions import db


class Report(db.Model):
    __tablename__ = "reports"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    report_type = db.Column(
        db.String(50),
        nullable=False
    )

    file_name = db.Column(
        db.String(255)
    )

    generated_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user = db.relationship(
        "User",
        back_populates="reports"
    )

    def to_dict(self):

        return {

            "id": self.id,

            "title": self.title,

            "report_type": self.report_type,

            "file_name": self.file_name,

            "generated_by": self.generated_by,

            "created_at": self.created_at.isoformat()
        }