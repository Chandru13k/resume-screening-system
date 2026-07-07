from pydantic import BaseModel


class CandidateRanking(BaseModel):

    candidate_id: int
    resume_id: int

    semantic_score: float
    skill_score: float
    resume_completeness: float

    overall_score: float

    matched_skills: list[str]

    missing_skills: list[str]


class RankingResponse(BaseModel):

    candidates: list[CandidateRanking]