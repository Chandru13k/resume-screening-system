from pydantic import BaseModel


class CandidateMatchResponse(BaseModel):

    candidate_id: int

    resume_id: int

    matched_skills: list[str]

    missing_skills: list[str]

    skill_match_percentage: float

    overall_score: float


class JobMatchResponse(BaseModel):

    candidates: list[CandidateMatchResponse]