# class Roles:
#     ADMIN = "admin"
#     MANAGER = "manager"
#     TECHNICIAN = "technician"
#     VIEWER = "viewer"

#     ALL = [
#         ADMIN,
#         MANAGER,
#         TECHNICIAN,
#         VIEWER,
#     ]
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    TECHNICIAN = "technician"
    VIEWER = "viewer"