from app.middleware.roles import roles_required
from flask import Blueprint, request

from marshmallow import ValidationError

from app.schemas.auth_schema import (
    RegisterSchema,
    LoginSchema,
)
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    create_access_token,
)


from app.services.auth_service import AuthService

from app.utils.responses import success, error
from app.repositories.user_repository import UserRepository
from app.utils.roles import UserRole


admin_required = roles_required(
    UserRole.ADMIN.value
)

manager_required = roles_required(
    UserRole.ADMIN.value,
    UserRole.MANAGER.value
)

technician_required = roles_required(
    UserRole.ADMIN.value,
    UserRole.MANAGER.value,
    UserRole.TECHNICIAN.value
)


auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth"
)


@auth_bp.post("/register")
def register():

    try:
        data = RegisterSchema().load(request.json)
    except ValidationError:
        return error(
            "Invalid registration details.",
            400
        )

    try:
        user = AuthService.register(data)
    except Exception as exc:
        return error(str(exc), 400)

    return success(
        "User created successfully.",
        user.to_dict(),
        201
    )


@auth_bp.post("/login")
def login():

    try:
        data = LoginSchema().load(request.json)
        result = AuthService.login(
            data["email"],
            data["password"],
            data["role"]
        )
    except ValidationError:
        return error("Invalid login details.", 400)
    except Exception as exc:
        return error(str(exc), 401)

    return success(
        "Login successful.",
        result
    )

@auth_bp.get("/me")
@jwt_required()
def me():

    user = UserRepository.get_by_id(
        int(get_jwt_identity())
    )

    return success(
        data=user.to_dict()
    )
@auth_bp.post("/refresh")
@jwt_required(refresh=True)
def refresh():

    identity = get_jwt_identity()

    token = create_access_token(
        identity=identity
    )

    return success(
        data={
            "access_token": token
        }
    )

@auth_bp.post("/logout")
def logout():

    return success(
        "Logged out successfully."
    )