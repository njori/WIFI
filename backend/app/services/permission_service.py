from app.repositories.permission_repository import PermissionRepository


class PermissionService:

    @staticmethod
    def allowed(

        role,

        resource,

        action

    ):

        if role == "super_admin":

            return True

        permission = PermissionRepository.get_permission(

            role,

            resource,

            action

        )

        return permission is not None