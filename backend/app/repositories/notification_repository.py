from app.core.base_repository import BaseRepository
from app.models.notification import Notification


class NotificationRepository(BaseRepository):

    model = Notification

    @classmethod
    def unread(cls):

        return Notification.query.filter_by(
            is_read=False
        ).order_by(
            Notification.created_at.desc()
        ).all()

    @classmethod
    def latest(cls):

        return Notification.query.order_by(
            Notification.created_at.desc()
        ).all()