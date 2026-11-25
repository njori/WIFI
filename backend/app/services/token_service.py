from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
)


class TokenService:

    @staticmethod
    def generate(user):

        access = create_access_token(
            identity=str(user.id)
        )

        refresh = create_refresh_token(
            identity=str(user.id)
        )

        return {
            "access_token": access,
            "refresh_token": refresh
        }