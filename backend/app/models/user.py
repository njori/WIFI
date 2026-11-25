from datetime import datetime

from app.extensions import db, bcrypt


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(80),
        unique=True,
        nullable=False,
        index=True
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))

    role = db.Column(

    db.Enum(

        "admin",

        "manager",

        "technician",

        "viewer",

        name="user_roles"

    ),

    default="viewer",

    nullable=False

    )
    logs = db.relationship(
    "Log",
    back_populates="user",
    lazy=True
    )
    notifications = db.relationship(
    "Notification",
    backref="user",
    lazy=True,
    cascade="all, delete-orphan"
    )
    reports = db.relationship(
    "Report",
    back_populates="user",
    lazy=True
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    last_login = db.Column(db.DateTime, nullable=True)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    def set_password(self, password: str):
        self.password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def check_password(self, password: str):
        return bcrypt.check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "full_name": f"{self.first_name or ''} {self.last_name or ''}".strip(),
            "role": self.role,
            "is_active": self.is_active,
            "status": "Active" if self.is_active else "Inactive",
            "last_login": self.last_login.isoformat() if self.last_login else None,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }