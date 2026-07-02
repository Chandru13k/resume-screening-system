from app.repositories.dashboard_repository import DashboardRepository


class DashboardService:

    def __init__(self, db):

        self.repo = DashboardRepository(db)

    def recruiter_dashboard(
        self,
        recruiter_id: int,
    ):

        return {

            "stats": {

                "total_jobs": self.repo.total_jobs(
                    recruiter_id
                ),

                "active_jobs": self.repo.active_jobs(
                    recruiter_id
                ),

                "parsed_resumes": self.repo.total_resumes(),

            },

            "recent_jobs": self.repo.recent_jobs(
                recruiter_id
            ),

        }