import re


EMAIL_REGEX = r"^[^@]+@[^@]+\.[^@]+$"


def valid_email(email: str) -> bool:
    return bool(re.match(EMAIL_REGEX, email))


def valid_password(password: str) -> bool:
    return len(password) >= 8