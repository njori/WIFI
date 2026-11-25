from datetime import datetime, timedelta
import secrets

from app.extensions import db


############################################################
# Many-to-Many Role <-> Permission
############################################################

role_permissions = db.Table(
    "role_permissions",

    db.Column(
        "role_id",
        db.Integer,
        db.ForeignKey("roles.id"),
        primary_key=True
    ),

    db.Column(
        "permission_id",
        db.Integer,
        db.ForeignKey("permissions.id"),
        primary_key=True
    )
)


############################################################
# Role
############################################################

class Role(db.Model):

    __tablename__ = "roles"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    permissions = db.relationship(
        "Permission",
        secondary=role_permissions,
        lazy="joined",
        back_populates="roles"
    )

    def to_dict(self):

        return {

            "id": self.id,

            "name": self.name,

            "description": self.description,

            "permissions": [

                permission.name

                for permission in self.permissions

            ]
        }


############################################################
# Permission
############################################################

class Permission(db.Model):

    __tablename__ = "permissions"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    module = db.Column(
        db.String(100),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    roles = db.relationship(
        "Role",
        secondary=role_permissions,
        back_populates="permissions"
    )

    def to_dict(self):

        return {

            "id": self.id,

            "name": self.name,

            "module": self.module,

            "description": self.description
        }


############################################################
# Audit Log
############################################################

class AuditLog(db.Model):

    __tablename__ = "audit_logs"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    action = db.Column(
        db.String(255),
        nullable=False
    )

    module = db.Column(
        db.String(100)
    )

    description = db.Column(
        db.Text
    )

    ip_address = db.Column(
        db.String(50)
    )

    user_agent = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):

        return {

            "id": self.id,

            "user_id": self.user_id,

            "action": self.action,

            "module": self.module,

            "description": self.description,

            "ip_address": self.ip_address,

            "user_agent": self.user_agent,

            "created_at": self.created_at.isoformat()
        }


############################################################
# User Session
############################################################

class UserSession(db.Model):

    __tablename__ = "user_sessions"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    token = db.Column(
        db.String(500),
        unique=True,
        nullable=False
    )

    ip_address = db.Column(
        db.String(50)
    )

    device = db.Column(
        db.String(255)
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    expires_at = db.Column(
        db.DateTime,
        default=lambda: datetime.utcnow() + timedelta(days=7)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):

        return {

            "id": self.id,

            "user_id": self.user_id,

            "ip_address": self.ip_address,

            "device": self.device,

            "is_active": self.is_active,

            "expires_at": self.expires_at.isoformat(),

            "created_at": self.created_at.isoformat()
        }


############################################################
# API Key
############################################################

class ApiKey(db.Model):

    __tablename__ = "api_keys"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    name = db.Column(
        db.String(100)
    )

    key = db.Column(
        db.String(128),
        unique=True,
        default=lambda: secrets.token_hex(32)
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    expires_at = db.Column(
        db.DateTime
    )

    def to_dict(self):

        return {

            "id": self.id,

            "name": self.name,

            "key": self.key,

            "is_active": self.is_active,

            "expires_at": self.expires_at.isoformat()
            if self.expires_at else None
        }


############################################################
# Login Attempts
############################################################

class LoginAttempt(db.Model):

    __tablename__ = "login_attempts"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100)
    )

    ip_address = db.Column(
        db.String(50)
    )

    success = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):

        return {

            "username": self.username,

            "ip_address": self.ip_address,

            "success": self.success,

            "created_at": self.created_at.isoformat()
        }


############################################################
# Password Reset Tokens
############################################################

class PasswordResetToken(db.Model):

    __tablename__ = "password_reset_tokens"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    token = db.Column(
        db.String(255),
        unique=True,
        default=lambda: secrets.token_urlsafe(32)
    )

    used = db.Column(
        db.Boolean,
        default=False
    )

    expires_at = db.Column(
        db.DateTime,
        default=lambda: datetime.utcnow() + timedelta(hours=1)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


############################################################
# Two-Factor Authentication
############################################################

class TwoFactorSecret(db.Model):

    __tablename__ = "two_factor_secrets"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    secret = db.Column(
        db.String(255),
        nullable=False
    )

    enabled = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):

        return {

            "user_id": self.user_id,

            "enabled": self.enabled
        }


############################################################
# IP Whitelist
############################################################

class IPWhitelist(db.Model):

    __tablename__ = "ip_whitelist"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    ip_address = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    description = db.Column(
        db.String(255)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


############################################################
# IP Blacklist
############################################################

class IPBlacklist(db.Model):

    __tablename__ = "ip_blacklist"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    ip_address = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    reason = db.Column(
        db.String(255)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )