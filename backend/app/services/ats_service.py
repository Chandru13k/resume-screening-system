from app.repositories.resume_profile_repository import (
    ResumeProfileRepository,
)
from app.schemas.ats import (
    ATSCandidate,
    ATSRequest,
    ATSResponse,
)
from app.schemas.search import CandidateSearchRequest
from app.services.semantic_search_service import (
    SemanticSearchService,
)
from app.utils.skill_matcher import SkillMatcher


class ATSService:
    """
    ATS Evaluation Service.

    Flow:

    Job Description
            │
            ▼
    Semantic Search
            │
            ▼
    Top Candidates
            │
            ▼
    Fetch Resume Profile
            │
            ▼
    Skill Matching
            │
            ▼
    ATS Score
    """

    def __init__(self, db):

        self.db = db

        self.search_service = SemanticSearchService()

        self.profile_repo = ResumeProfileRepository(db)

    def evaluate(
        self,
        request: ATSRequest,
    ) -> ATSResponse:

        # ----------------------------------------
        # Step 1
        # Semantic Search
        # ----------------------------------------

        search_results = self.search_service.search(

            CandidateSearchRequest(

                query=request.job_description,

                limit=request.candidate_limit,

            )

        )

        candidates = []

        # ----------------------------------------
        # Step 2
        # ATS Evaluation
        # ----------------------------------------

        for result in search_results.candidates:

            profile = self.profile_repo.get_by_resume_document(

                result.resume_document_id

            )

            if not profile:
                continue

            skill_result = SkillMatcher.compare(

                request.job_description,

                profile.skills or [],

            )

            semantic_score = round(

                result.similarity_score * 100,

                2,

            )

            skill_score = skill_result["skill_score"]

            overall = round(

                (
                    semantic_score * 0.60
                    +
                    skill_score * 0.40
                ),

                2,

            )

            candidates.append(

                ATSCandidate(

                    candidate_id=result.candidate_id,

                    resume_document_id=result.resume_document_id,

                    full_name=result.full_name,

                    email=result.email,

                    location=result.location,

                    semantic_score=semantic_score,

                    skill_match_score=skill_score,

                    overall_score=overall,

                    matched_skills=skill_result["matched_skills"],

                    missing_skills=skill_result["missing_skills"],

                )

            )

        candidates.sort(

            key=lambda x: x.overall_score,

            reverse=True,

        )

        return ATSResponse(

            candidates=candidates,

        )