from datetime import datetime

from app.extensions import db


class AutomationLog(db.Model):

    __tablename__ = "automation_logs"

    id = db.Column(

        db.Integer,

        primary_key=True

    )

    router_id = db.Column(

        db.Integer,

        db.ForeignKey("routers.id")

    )

    command = db.Column(

        db.Text

    )

    output = db.Column(

        db.Text

    )

    executed_at = db.Column(

        db.DateTime,

        default=datetime.utcnow

    )

    router = db.relationship(

        "Router",

        backref="automation_logs"

    )

    def to_dict(self):

        return {

            "id": self.id,

            "router_id": self.router_id,

            "command": self.command,

            "output": self.output,

            "executed_at": self.executed_at.isoformat()

        }