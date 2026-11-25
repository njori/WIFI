from datetime import datetime
import secrets
import hashlib

from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

from app.security.models import (
    Role,
    Permission,
    AuditLog,
    LoginAttempt,
    UserSession,
    ApiKey,
    PasswordResetToken,
    TwoFactorSecret,
    IPWhitelist,
    IPBlacklist
)

from app.security.repository import SecurityRepository


class SecurityService:

    ###############################################################
    # ROLE MANAGEMENT
    ###############################################################

    @staticmethod
    def create_role(data):

        if SecurityRepository.get_role_by_name(data["name"]):

            raise Exception("Role already exists.")

        role = Role(

            name=data["name"],

            description=data.get("description")

        )

        SecurityRepository.create_role(role)

        SecurityService.audit(

            action="CREATE_ROLE",

            module="Security",

            description=f"Role '{role.name}' created."

        )

        return role.to_dict()

    ###############################################################

    @staticmethod
    def update_role(role_id, data):

        role = SecurityRepository.get_role(role_id)

        if role is None:

            raise Exception("Role not found.")

        role.name = data.get(

            "name",

            role.name

        )

        role.description = data.get(

            "description",

            role.description

        )

        SecurityRepository.update_role()

        SecurityService.audit(

            action="UPDATE_ROLE",

            module="Security",

            description=f"Role '{role.name}' updated."

        )

        return role.to_dict()

    ###############################################################

    @staticmethod
    def delete_role(role_id):

        role = SecurityRepository.get_role(role_id)

        if role is None:

            raise Exception("Role not found.")

        SecurityRepository.delete_role(role)

        SecurityService.audit(

            action="DELETE_ROLE",

            module="Security",

            description=f"Role '{role.name}' deleted."

        )

        return {

            "message": "Role deleted successfully."

        }

    ###############################################################
    # PERMISSION MANAGEMENT
    ###############################################################

    @staticmethod
    def create_permission(data):

        if SecurityRepository.get_permission_by_name(

            data["name"]

        ):

            raise Exception(

                "Permission already exists."

            )

        permission = Permission(

            name=data["name"],

            module=data["module"],

            description=data.get("description")

        )

        SecurityRepository.create_permission(

            permission

        )

        SecurityService.audit(

            action="CREATE_PERMISSION",

            module="Security",

            description=f"Permission '{permission.name}' created."

        )

        return permission.to_dict()

    ###############################################################

    @staticmethod
    def assign_permission(

        role_id,

        permission_id

    ):

        role = SecurityRepository.get_role(

            role_id

        )

        permission = SecurityRepository.get_permission(

            permission_id

        )

        if role is None:

            raise Exception(

                "Role not found."

            )

        if permission is None:

            raise Exception(

                "Permission not found."

            )

        SecurityRepository.assign_permission(

            role,

            permission

        )

        SecurityService.audit(

            action="ASSIGN_PERMISSION",

            module="Security",

            description=f"Permission '{permission.name}' assigned to '{role.name}'."

        )

        return role.to_dict()

    ###############################################################

    @staticmethod
    def revoke_permission(

        role_id,

        permission_id

    ):

        role = SecurityRepository.get_role(

            role_id

        )

        permission = SecurityRepository.get_permission(

            permission_id

        )

        if role is None:

            raise Exception(

                "Role not found."

            )

        if permission is None:

            raise Exception(

                "Permission not found."

            )

        SecurityRepository.revoke_permission(

            role,

            permission

        )

        SecurityService.audit(

            action="REVOKE_PERMISSION",

            module="Security",

            description=f"Permission '{permission.name}' removed from '{role.name}'."

        )

        return role.to_dict()

    ###############################################################
    # AUDIT LOGGING
    ###############################################################

    @staticmethod
    def audit(

        action,

        module,

        description

    ):

        try:

            from flask_jwt_extended import get_jwt_identity

            user = get_jwt_identity()

        except:

            user = None

        log = AuditLog(

            user_id=user,

            action=action,

            module=module,

            description=description,

            ip_address=request.remote_addr,

            user_agent=request.headers.get(

                "User-Agent"

            )

        )

        SecurityRepository.save_audit(

            log

        )

    ###############################################################

    @staticmethod
    def get_audits():

        logs = SecurityRepository.get_audits()

        return [

            log.to_dict()

            for log in logs

        ]

    ###############################################################

    @staticmethod
    def get_user_audits(user_id):

        logs = SecurityRepository.get_user_audits(

            user_id

        )

        return [

            log.to_dict()

            for log in logs

        ]

    ###############################################################
    # LOGIN ATTEMPTS
    ###############################################################

    @staticmethod
    def record_login(

        username,

        success

    ):

        attempt = LoginAttempt(

            username=username,

            success=success,

            ip_address=request.remote_addr

        )

        SecurityRepository.save_login_attempt(

            attempt

        )

    ###############################################################

    @staticmethod
    def login_attempts(username):

        return SecurityRepository.failed_attempts(

            username

        )

    ###############################################################

    @staticmethod
    def clear_login_attempts(

        username

    ):

        SecurityRepository.clear_attempts(

            username

        )

    ###############################################################
    # PASSWORD HASHING
    ###############################################################

    @staticmethod
    def hash_password(password):

        return generate_password_hash(password)

    ###############################################################

    @staticmethod
    def verify_password(

        password,

        hashed

    ):

        return check_password_hash(

            hashed,

            password

        )

    ###############################################################
    # TOKEN HASHING
    ###############################################################

    @staticmethod
    def hash_token(token):

        return hashlib.sha256(

            token.encode()

        ).hexdigest()

        ###############################################################
    # ACCOUNT LOCKOUT
    ###############################################################

    MAX_LOGIN_ATTEMPTS = 5

    @staticmethod
    def account_locked(username):

        attempts = SecurityRepository.failed_attempts(
            username
        )

        return attempts >= SecurityService.MAX_LOGIN_ATTEMPTS

    ###############################################################
    # PASSWORD POLICY
    ###############################################################

    @staticmethod
    def validate_password(password):

        if len(password) < 8:
            raise Exception(
                "Password must contain at least 8 characters."
            )

        if not any(c.isupper() for c in password):
            raise Exception(
                "Password must contain an uppercase letter."
            )

        if not any(c.islower() for c in password):
            raise Exception(
                "Password must contain a lowercase letter."
            )

        if not any(c.isdigit() for c in password):
            raise Exception(
                "Password must contain a digit."
            )

        special = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

        if not any(c in special for c in password):
            raise Exception(
                "Password must contain a special character."
            )

        return True

    ###############################################################
    # PASSWORD RESET
    ###############################################################

    @staticmethod
    def create_reset_token(user):

        token = PasswordResetToken(
            user_id=user.id
        )

        SecurityRepository.create_reset_token(
            token
        )

        SecurityService.audit(

            action="PASSWORD_RESET_REQUEST",

            module="Security",

            description=f"Password reset requested for user {user.id}"

        )

        return token.token

    ###############################################################

    @staticmethod
    def verify_reset_token(token):

        reset = SecurityRepository.get_reset_token(
            token
        )

        if reset is None:
            raise Exception(
                "Invalid reset token."
            )

        if reset.used:
            raise Exception(
                "Token already used."
            )

        if reset.expires_at < datetime.utcnow():
            raise Exception(
                "Token expired."
            )

        return reset

    ###############################################################

    @staticmethod
    def use_reset_token(token):

        SecurityRepository.use_reset_token(
            token
        )

    ###############################################################
    # SESSION MANAGEMENT
    ###############################################################

    @staticmethod
    def create_session(

        user,

        jwt_token

    ):

        session = UserSession(

            user_id=user.id,

            token=jwt_token,

            ip_address=request.remote_addr,

            device=request.headers.get(

                "User-Agent"

            )

        )

        SecurityRepository.create_session(

            session

        )

        SecurityService.audit(

            action="LOGIN",

            module="Authentication",

            description=f"User {user.username} logged in."

        )

        return session

    ###############################################################

    @staticmethod
    def get_sessions(user_id):

        sessions = SecurityRepository.get_sessions(

            user_id

        )

        return [

            s.to_dict()

            for s in sessions

        ]

    ###############################################################

    @staticmethod
    def revoke_session(token):

        session = SecurityRepository.get_session(

            token

        )

        if session is None:

            raise Exception(

                "Session not found."

            )

        SecurityRepository.revoke_session(

            session

        )

        SecurityService.audit(

            action="LOGOUT",

            module="Authentication",

            description="Session revoked."

        )

    ###############################################################

    @staticmethod
    def revoke_all_sessions(user_id):

        SecurityRepository.revoke_all_sessions(

            user_id

        )

        SecurityService.audit(

            action="LOGOUT_ALL",

            module="Authentication",

            description=f"All sessions revoked for user {user_id}"

        )

    ###############################################################
    # API KEYS
    ###############################################################

    @staticmethod
    def create_api_key(

        user,

        name

    ):

        key = ApiKey(

            user_id=user.id,

            name=name

        )

        SecurityRepository.create_api_key(

            key

        )

        SecurityService.audit(

            action="CREATE_API_KEY",

            module="Security",

            description=f"API key created by {user.username}"

        )

        return key.to_dict()

    ###############################################################

    @staticmethod
    def revoke_api_key(key):

        api = SecurityRepository.get_api_key(

            key

        )

        if api is None:

            raise Exception(

                "API key not found."

            )

        SecurityRepository.revoke_api_key(

            api

        )

        SecurityService.audit(

            action="REVOKE_API_KEY",

            module="Security",

            description="API key revoked."

        )
            ###############################################################
    # TWO FACTOR AUTHENTICATION
    ###############################################################

    @staticmethod
    def enable_2fa(user):

        import pyotp

        secret = pyotp.random_base32()

        two_factor = SecurityRepository.get_two_factor(
            user.id
        )

        if two_factor:

            two_factor.secret = secret
            two_factor.enabled = True

            SecurityRepository.update_two_factor()

        else:

            two_factor = TwoFactorSecret(

                user_id=user.id,

                secret=secret,

                enabled=True

            )

            SecurityRepository.create_two_factor(
                two_factor
            )

        SecurityService.audit(

            action="ENABLE_2FA",

            module="Security",

            description=f"2FA enabled for {user.username}"

        )

        return secret

    ###############################################################

    @staticmethod
    def verify_2fa(

        user,

        code

    ):

        import pyotp

        two_factor = SecurityRepository.get_two_factor(
            user.id
        )

        if two_factor is None:

            return False

        totp = pyotp.TOTP(
            two_factor.secret
        )

        return totp.verify(code)
            ###############################################################
    # IP WHITELIST
    ###############################################################

    @staticmethod
    def ip_allowed(ip):

        blocked = SecurityRepository.get_blacklist(
            ip
        )

        if blocked:
            return False

        whitelist = SecurityRepository.whitelist()

        if len(whitelist) == 0:
            return True

        return SecurityRepository.get_whitelist(
            ip
        ) is not None

    ###############################################################
    # ENCRYPTION
    ###############################################################

    @staticmethod
    def encrypt(value):

        import base64

        return base64.b64encode(

            value.encode()

        ).decode()

    ###############################################################

    @staticmethod
    def decrypt(value):

        import base64

        return base64.b64decode(

            value.encode()

        ).decode()

    ###############################################################
    # SECURITY NOTIFICATIONS
    ###############################################################

    @staticmethod
    def notify(

        title,

        message

    ):

        try:

            from app.services.notification_service import (
                NotificationService
            )

            NotificationService.send(

                title=title,

                message=message,

                type="warning"

            )

        except Exception:

            pass