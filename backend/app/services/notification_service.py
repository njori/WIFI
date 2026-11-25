from app.models.notification import Notification
from app.repositories.notification_repository import NotificationRepository
from app.sockets.emitter import SocketEmitter


class NotificationService:

    @staticmethod
    def send(

        title,

        message,

        category="System",

        priority="info",

        user_id=None

    ):

        notification = Notification(

            title=title,

            message=message,

            category=category,

            priority=priority,

            user_id=user_id

        )

        notification = NotificationRepository.create(
            notification
        )

        SocketEmitter.notification(

            notification.to_dict()

        )

        return notification

    @staticmethod
    def all():

        return NotificationRepository.latest()

    @staticmethod
    def unread():

        return Notification.query.filter_by(

            is_read=False

        ).order_by(

            Notification.created_at.desc()

        ).all()
    @staticmethod
    def mark_read(notification_id):

        notification = NotificationRepository.get_by_id(
            notification_id
        )

        if not notification:

            raise Exception(
                "Notification not found."
            )

        notification.is_read = True

        NotificationRepository.update()

        return notification

    @staticmethod
    def delete(notification_id):

        notification = NotificationRepository.get_by_id(
            notification_id
        )

        if not notification:

            raise Exception(
                "Notification not found."
            )

        NotificationRepository.delete(notification)

        return {
            "message": "Deleted successfully."
        }