from datetime import datetime

from pydantic import BaseModel


class ResumeUploadResponse(BaseModel):

    id: int

    original_filename: str

    stored_filename: str

    file_type: str

    file_size: int

    upload_status: str

    created_at: datetime

    class Config:
        from_attributes = True