from app.repositories.candidate_dashboard_repository import (
    CandidateDashboardRepository,
)


class CandidateDashboardService:

    def __init__(self, db):

        self.repo = CandidateDashboardRepository(
            db
        )

    def dashboard(
        self,
        candidate_id: int,
    ):

        return {

            "profile": self.repo.get_profile(
                candidate_id
            ),

            "resumes": self.repo.get_resumes(
                candidate_id
            ),

        }