from functools import wraps

from flask_jwt_extended import (
    get_jwt_identity
)

from app.models.user import User
from app.services.permission_service import PermissionService


def permission_required(

    resource,

    action

):

    def wrapper(fn):

        @wraps(fn)

        def decorated(*args, **kwargs):

            user_id = get_jwt_identity()

            user = User.query.get(user_id)

            if not user:

                return {

                    "message": "Unauthorized"

                }, 401

            if not PermissionService.allowed(

                user.role,

                resource,

                action

            ):

                return {

                    "message": "Access denied"

                }, 403

            return fn(

                *args,

                **kwargs

            )

        return decorated

    return wrapper