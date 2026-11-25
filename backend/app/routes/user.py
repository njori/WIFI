from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.utils.responses import success, error
from app.utils.roles import UserRole
from app.middleware.roles import roles_required


user_bp = Blueprint(
    "users",
    __name__,
    url_prefix="/api/users"
)


@user_bp.get("")
@jwt_required()
@roles_required(UserRole.ADMIN.value)
def get_users():
    return success(data=[
        user.to_dict()
        for user in User.query.order_by(User.username).all()
    ])


@user_bp.put("/<int:user_id>")
@jwt_required()
@roles_required(UserRole.ADMIN.value)
def update_user(user_id):
    user = UserRepository.get_by_id(user_id)
    if user is None:
        return error("User not found.", 404)

    data = request.get_json(silent=True) or {}
    role = data.get("role")
    valid_roles = {item.value for item in UserRole}

    if role is not None and role not in valid_roles:
        return error("Invalid user role.", 400)

    if role is not None:
        user.role = role

    if "is_active" in data:
        user.is_active = bool(data["is_active"])

    UserRepository.update(user)
    return success("User updated successfully.", user.to_dict())
