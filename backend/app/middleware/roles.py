from functools import wraps

from flask_jwt_extended import (
    verify_jwt_in_request,
    get_jwt_identity,
)

from app.repositories.user_repository import UserRepository
from app.utils.responses import error


def roles_required(*roles):

    def decorator(fn):

        @wraps(fn)
        def wrapper(*args, **kwargs):

            verify_jwt_in_request()

            user = UserRepository.get_by_id(
                int(get_jwt_identity())
            )

            if user is None:
                return error(
                    "User not found.",
                    404
                )

            if not user.is_active:
                return error(
                    "Account disabled.",
                    403
                )

            if user.role not in roles:
                return error(
                    "Permission denied.",
                    403
                )

            return fn(*args, **kwargs)

        return wrapper

    return decorator