from app.core.base_repository import BaseRepository
from app.models.automation_log import AutomationLog


class AutomationRepository(

    BaseRepository

):

    model = AutomationLog