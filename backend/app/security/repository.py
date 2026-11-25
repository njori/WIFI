from datetime import datetime

from app.extensions import db

from app.security.models import (
    Role,
    Permission,
    AuditLog,
    UserSession,
    ApiKey,
    LoginAttempt,
    PasswordResetToken,
    TwoFactorSecret,
    IPWhitelist,
    IPBlacklist
)


class SecurityRepository:

    ##########################################################
    # ROLE
    ##########################################################

    @staticmethod
    def get_roles():
        return Role.query.order_by(Role.name).all()

    @staticmethod
    def get_role(role_id):
        return Role.query.get(role_id)

    @staticmethod
    def get_role_by_name(name):
        return Role.query.filter_by(name=name).first()

    @staticmethod
    def create_role(role):
        db.session.add(role)
        db.session.commit()
        return role

    @staticmethod
    def update_role():
        db.session.commit()

    @staticmethod
    def delete_role(role):
        db.session.delete(role)
        db.session.commit()


    ##########################################################
    # PERMISSION
    ##########################################################

    @staticmethod
    def get_permissions():
        return Permission.query.order_by(Permission.module).all()

    @staticmethod
    def get_permission(permission_id):
        return Permission.query.get(permission_id)

    @staticmethod
    def get_permission_by_name(name):
        return Permission.query.filter_by(
            name=name
        ).first()

    @staticmethod
    def create_permission(permission):
        db.session.add(permission)
        db.session.commit()
        return permission

    @staticmethod
    def update_permission():
        db.session.commit()

    @staticmethod
    def delete_permission(permission):
        db.session.delete(permission)
        db.session.commit()


    ##########################################################
    # ROLE PERMISSION
    ##########################################################

    @staticmethod
    def assign_permission(role, permission):

        if permission not in role.permissions:

            role.permissions.append(permission)

            db.session.commit()

        return role

    @staticmethod
    def revoke_permission(role, permission):

        if permission in role.permissions:

            role.permissions.remove(permission)

            db.session.commit()

        return role


    ##########################################################
    # AUDIT LOG
    ##########################################################

    @staticmethod
    def save_audit(log):

        db.session.add(log)

        db.session.commit()

        return log

    @staticmethod
    def get_audits():

        return AuditLog.query.order_by(

            AuditLog.created_at.desc()

        ).all()

    @staticmethod
    def get_user_audits(user_id):

        return AuditLog.query.filter_by(

            user_id=user_id

        ).order_by(

            AuditLog.created_at.desc()

        ).all()

    @staticmethod
    def get_module_audits(module):

        return AuditLog.query.filter_by(

            module=module

        ).order_by(

            AuditLog.created_at.desc()

        ).all()


    ##########################################################
    # USER SESSIONS
    ##########################################################

    @staticmethod
    def create_session(session):

        db.session.add(session)

        db.session.commit()

        return session

    @staticmethod
    def get_sessions(user_id):

        return UserSession.query.filter_by(

            user_id=user_id

        ).all()

    @staticmethod
    def get_active_sessions(user_id):

        return UserSession.query.filter_by(

            user_id=user_id,

            is_active=True

        ).all()

    @staticmethod
    def get_session(token):

        return UserSession.query.filter_by(

            token=token

        ).first()

    @staticmethod
    def revoke_session(session):

        session.is_active = False

        db.session.commit()

    @staticmethod
    def revoke_all_sessions(user_id):

        sessions = UserSession.query.filter_by(

            user_id=user_id,

            is_active=True

        ).all()

        for session in sessions:

            session.is_active = False

        db.session.commit()


    ##########################################################
    # API KEYS
    ##########################################################

    @staticmethod
    def create_api_key(key):

        db.session.add(key)

        db.session.commit()

        return key

    @staticmethod
    def get_api_keys(user_id):

        return ApiKey.query.filter_by(

            user_id=user_id

        ).all()

    @staticmethod
    def get_api_key(key):

        return ApiKey.query.filter_by(

            key=key

        ).first()

    @staticmethod
    def revoke_api_key(key):

        key.is_active = False

        db.session.commit()


    ##########################################################
    # LOGIN ATTEMPTS
    ##########################################################

    @staticmethod
    def save_login_attempt(attempt):

        db.session.add(attempt)

        db.session.commit()

        return attempt

    @staticmethod
    def failed_attempts(username, minutes=15):

        from datetime import timedelta

        since = datetime.utcnow() - timedelta(

            minutes=minutes

        )

        return LoginAttempt.query.filter(

            LoginAttempt.username == username,

            LoginAttempt.success == False,

            LoginAttempt.created_at >= since

        ).count()

    @staticmethod
    def clear_attempts(username):

        LoginAttempt.query.filter_by(

            username=username

        ).delete()

        db.session.commit()


    ##########################################################
    # PASSWORD RESET
    ##########################################################

    @staticmethod
    def create_reset_token(token):

        db.session.add(token)

        db.session.commit()

        return token

    @staticmethod
    def get_reset_token(token):

        return PasswordResetToken.query.filter_by(

            token=token,

            used=False

        ).first()

    @staticmethod
    def use_reset_token(token):

        token.used = True

        db.session.commit()


    ##########################################################
    # TWO FACTOR
    ##########################################################

    @staticmethod
    def create_two_factor(secret):

        db.session.add(secret)

        db.session.commit()

        return secret

    @staticmethod
    def get_two_factor(user_id):

        return TwoFactorSecret.query.filter_by(

            user_id=user_id

        ).first()

    @staticmethod
    def update_two_factor():

        db.session.commit()


    ##########################################################
    # IP WHITELIST
    ##########################################################

    @staticmethod
    def whitelist():

        return IPWhitelist.query.all()

    @staticmethod
    def get_whitelist(ip):

        return IPWhitelist.query.filter_by(

            ip_address=ip

        ).first()

    @staticmethod
    def add_whitelist(item):

        db.session.add(item)

        db.session.commit()

        return item

    @staticmethod
    def remove_whitelist(item):

        db.session.delete(item)

        db.session.commit()


    ##########################################################
    # IP BLACKLIST
    ##########################################################

    @staticmethod
    def blacklist():

        return IPBlacklist.query.all()

    @staticmethod
    def get_blacklist(ip):

        return IPBlacklist.query.filter_by(

            ip_address=ip

        ).first()

    @staticmethod
    def add_blacklist(item):

        db.session.add(item)

        db.session.commit()

        return item

    @staticmethod
    def remove_blacklist(item):

        db.session.delete(item)

        db.session.commit()