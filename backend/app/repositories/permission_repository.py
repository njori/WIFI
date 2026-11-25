from app.core.base_repository import BaseRepository
from app.models.permission import Permission


class PermissionRepository(BaseRepository):

    model = Permission

    @classmethod
    def get_permission(

        cls,

        role,

        resource,

        action

    ):

        return Permission.query.filter_by(

            role=role,

            resource=resource,

            action=action

        ).first()