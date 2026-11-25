from app.core.base_repository import BaseRepository
from app.models.report import Report


class ReportRepository(BaseRepository):

    model = Report

    @classmethod
    def latest(cls):

        return (

            Report.query

            .order_by(

                Report.created_at.desc()

            )

            .all()

        )