from datetime import datetime

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.services.password_service import PasswordService
from app.services.token_service import TokenService
from app.services.log_service import LogService
from app.services.notification_service import NotificationService

class AuthService:

    @staticmethod
    def register(data):

        if UserRepository.exists_email(data["email"]):
            raise Exception("Email already exists.")

        if UserRepository.exists_username(data["username"]):
            raise Exception("Username already exists.")

        user = User(
            username=data["username"],
            email=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            role="viewer",
            is_active=True,
        )

        user.password_hash = PasswordService.hash_password(
            data["password"]
        )

        UserRepository.create(user)

        # Log registration
        LogService.write(
            module="Authentication",
            action="Register",
            message=f"{user.username} created an account.",
            user_id=user.id,
        )

        return user

    @staticmethod
    def login(email, password, role):

        user = UserRepository.get_by_email(email)

        if user is None:
            raise Exception("Invalid credentials.")

        if not PasswordService.verify(password, user.password_hash):
            raise Exception("Invalid credentials.")

        if user.role != role:
            raise Exception("Selected role does not match this account.")

        user.last_login = datetime.utcnow()

        UserRepository.update(user)

        tokens = TokenService.generate(user)

        # Log login
        LogService.write(
            module="Authentication",
            action="Login",
            message=f"{user.username} logged in.",
            user_id=user.id,
        )
        NotificationService.send(
            title="Login",
            message=f"{user.username} signed in.",
            priority="success",
            user_id=user.id
)

        return {
            "user": user.to_dict(),
            **tokens
        }