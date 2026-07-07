from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ResumeUploadResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    candidate_id: int

    original_filename: str

    stored_filename: str

    file_path: str

    file_type: str

    file_size: int

    upload_status: str

    parsing_completed: bool

    created_at: datetime


class ResumeSkillResponse(BaseModel):

    id: int

    skill: str


class ResumeDetailsResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int

    candidate_id: int

    original_filename: str

    stored_filename: str

    file_path: str

    file_type: str

    file_size: int

    upload_status: str

    parsing_completed: bool

    extracted_text: str | None

    created_at: datetime