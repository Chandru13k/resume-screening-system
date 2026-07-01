from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from app.models.user import User

from app.models.candidate_profile import CandidateProfile

from app.models.recruiter_profile import RecruiterProfile

from app.models.job import Job

from app.models.job_skill import JobSkill

from app.models.resume_document import ResumeDocument

from app.models.resume_skill import ResumeSkill

from app.models.candidate_job_match import CandidateJobMatch