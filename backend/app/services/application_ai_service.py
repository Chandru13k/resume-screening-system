import json

from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from app.ai.gemini_service import GeminiService
from app.ai.hybrid_matcher import HybridMatcher

from app.models.application_ai_insight import (
    ApplicationAIInsight,
)

from app.repositories.application_ai_repository import (
    ApplicationAIRepository,
)

from app.repositories.application_repository import (
    ApplicationRepository,
)


class ApplicationAIService:

    def __init__(self, db: Session):

        self.db = db

        self.application_repo = (
            ApplicationRepository(db)
        )

        self.ai_repo = (
            ApplicationAIRepository(db)
        )

        self.matcher = (
            HybridMatcher(db)
        )

        self.gemini = (
            GeminiService()
        )

    # --------------------------------------------------
    # AI Insights
    # --------------------------------------------------

    def get_ai_insights(
        self,
        recruiter_id: int,
        application_id: int,
    ):

        application = (
            self.application_repo.get_by_id(
                application_id
            )
        )

        if not application:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Application not found.",
            )

        if (
            application.job.recruiter_id
            != recruiter_id
        ):

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied.",
            )

        # ------------------------------------------
        # Already Generated?
        # ------------------------------------------

        existing = (
            self.ai_repo.get_by_application(
                application_id
            )
        )

        if existing:

            return {

                "application_id": existing.application_id,

                "summary": existing.summary,

                "strengths": json.loads(
                    existing.strengths
                ),

                "weaknesses": json.loads(
                    existing.weaknesses
                ),

                "score_explanation": (
                    existing.score_explanation
                ),

                "interview_questions": json.loads(
                    existing.interview_questions
                ),

                "recommendation": (
                    existing.recommendation
                ),

                "created_at": existing.created_at,
            }

        # ------------------------------------------
        # Calculate AI Match
        # ------------------------------------------

        match = self.matcher.match_candidate(
            job_id=application.job_id,
            resume_id=application.resume_id,
        )

        # ------------------------------------------
        # Gemini
        # ------------------------------------------

        ai = (
            self.gemini.generate_candidate_insights(
                resume_text=application.resume.extracted_text,
                job_description=application.job.description,
                overall_score=match["overall_score"],
                matched_skills=match[
                    "matched_skills"
                ],
                missing_skills=match[
                    "missing_skills"
                ],
            )
        )

        insight = ApplicationAIInsight(

            application_id=application.id,

            summary=ai["summary"],

            strengths=json.dumps(
                ai["strengths"]
            ),

            weaknesses=json.dumps(
                ai["weaknesses"]
            ),

            score_explanation=ai[
                "score_explanation"
            ],

            interview_questions=json.dumps(
                ai[
                    "interview_questions"
                ]
            ),

            recommendation=ai[
                "recommendation"
            ],
        )

        self.ai_repo.create(
            insight
        )

        self.db.commit()

        self.db.refresh(
            insight
        )

        return {

            "application_id": insight.application_id,

            "summary": insight.summary,

            "strengths": ai["strengths"],

            "weaknesses": ai["weaknesses"],

            "score_explanation": (
                insight.score_explanation
            ),

            "interview_questions": ai[
                "interview_questions"
            ],

            "recommendation": (
                insight.recommendation
            ),

            "created_at": insight.created_at,
        }