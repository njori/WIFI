from functools import wraps
from flask import jsonify, request
from flask import jsonify

from flask_jwt_extended import (
    get_jwt_identity,
    verify_jwt_in_request
)

from app.models.user import User
from app.security.repository import SecurityRepository


##############################################################
# GET CURRENT USER
##############################################################

def current_user():

    verify_jwt_in_request()

    identity = get_jwt_identity()

    user = User.query.get(identity)

    if user is None:

        raise Exception("User not found.")

    return user


##############################################################
# ROLE REQUIRED
##############################################################

def role_required(role_name):

    def decorator(fn):

        @wraps(fn)

        def wrapper(*args, **kwargs):

            user = current_user()

            if user.role is None:

                return jsonify({

                    "success": False,

                    "message": "No role assigned."

                }),403

            if user.role.name != role_name:

                return jsonify({

                    "success": False,

                    "message": "Access denied."

                }),403

            return fn(*args, **kwargs)

        return wrapper

    return decorator


##############################################################
# ADMIN REQUIRED
##############################################################

def admin_required(fn):

    @wraps(fn)

    def wrapper(*args, **kwargs):

        user = current_user()

        if user.role is None:

            return jsonify({

                "success": False,

                "message": "No role assigned."

            }),403

        if user.role.name not in [

            "Admin",

            "Super Admin"

        ]:

            return jsonify({

                "success": False,

                "message": "Administrator access required."

            }),403

        return fn(*args, **kwargs)

    return wrapper


##############################################################
# SUPER ADMIN REQUIRED
##############################################################

def super_admin_required(fn):

    @wraps(fn)

    def wrapper(*args, **kwargs):

        user = current_user()

        if user.role is None:

            return jsonify({

                "success": False,

                "message": "No role assigned."

            }),403

        if user.role.name != "Super Admin":

            return jsonify({

                "success": False,

                "message": "Super Administrator required."

            }),403

        return fn(*args, **kwargs)

    return wrapper


##############################################################
# PERMISSION REQUIRED
##############################################################

def permission_required(permission_name):

    def decorator(fn):

        @wraps(fn)

        def wrapper(*args, **kwargs):

            user = current_user()

            if user.role is None:

                return jsonify({

                    "success": False,

                    "message": "No role assigned."

                }),403

            permissions = [

                permission.name

                for permission in user.role.permissions

            ]

            if permission_name not in permissions:

                return jsonify({

                    "success": False,

                    "message": "Permission denied."

                }),403

            return fn(*args, **kwargs)

        return wrapper

    return decorator


##############################################################
# ANY PERMISSION REQUIRED
##############################################################

def any_permission_required(permission_list):

    def decorator(fn):

        @wraps(fn)

        def wrapper(*args, **kwargs):

            user = current_user()

            if user.role is None:

                return jsonify({

                    "success": False,

                    "message": "No role assigned."

                }),403

            permissions = [

                permission.name

                for permission in user.role.permissions

            ]

            allowed = any(

                permission in permissions

                for permission in permission_list

            )

            if not allowed:

                return jsonify({

                    "success": False,

                    "message": "Permission denied."

                }),403

            return fn(*args, **kwargs)

        return wrapper

    return decorator


##############################################################
# ALL PERMISSIONS REQUIRED
##############################################################

def all_permissions_required(permission_list):

    def decorator(fn):

        @wraps(fn)

        def wrapper(*args, **kwargs):

            user = current_user()

            if user.role is None:

                return jsonify({

                    "success": False,

                    "message": "No role assigned."

                }),403

            permissions = [

                permission.name

                for permission in user.role.permissions

            ]

            for permission in permission_list:

                if permission not in permissions:

                    return jsonify({

                        "success": False,

                        "message": "Permission denied."

                    }),403

            return fn(*args, **kwargs)

        return wrapper

    return decorator


##############################################################
# SELF OR ADMIN
##############################################################

def self_or_admin(fn):

    @wraps(fn)

    def wrapper(*args, **kwargs):

        user = current_user()

        target_user = kwargs.get("user_id")

        if str(user.id) == str(target_user):

            return fn(*args, **kwargs)

        if user.role and user.role.name in [

            "Admin",

            "Super Admin"

        ]:

            return fn(*args, **kwargs)

        return jsonify({

            "success": False,

            "message": "Access denied."

        }),403

    return wrapper


##############################################################
# ACTIVE SESSION REQUIRED
##############################################################

def active_session_required(fn):

    @wraps(fn)

    def wrapper(*args, **kwargs):

        token = None

        auth = request.headers.get("Authorization")

        if auth:

            token = auth.replace(

                "Bearer ",

                ""

            )

        session = SecurityRepository.get_session(

            token

        )

        if session is None:

            return jsonify({

                "success": False,

                "message": "Session not found."

            }),401

        if not session.is_active:

            return jsonify({

                "success": False,

                "message": "Session expired."

            }),401

        return fn(*args, **kwargs)

    return wrapper