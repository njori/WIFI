from flask import Blueprint
from flask import jsonify

from flask_jwt_extended import jwt_required

from app.services.notification_service import NotificationService


notification_bp = Blueprint(

    "notifications",

    __name__,

    url_prefix="/api/notifications"

)


@notification_bp.get("")
@jwt_required()
def all_notifications():

    notifications = NotificationService.all()

    return jsonify([

        n.to_dict()

        for n in notifications

    ])


@notification_bp.get("/unread")
@jwt_required()
def unread():

    notifications = NotificationService.unread()

    return jsonify([

        n.to_dict()

        for n in notifications

    ])


@notification_bp.put("/<int:id>/read")
@jwt_required()
def read(id):

    notification = NotificationService.mark_read(id)

    return jsonify(

        notification.to_dict()

    )


@notification_bp.delete("/<int:id>")
@jwt_required()
def delete(id):

    return jsonify(

        NotificationService.delete(id)

    )