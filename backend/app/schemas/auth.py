from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.enums.user_role import UserRole


class CandidateRegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

    full_name: str
    phone: str | None = None
    location: str | None = None

    github_url: str | None = None
    linkedin_url: str | None = None
    portfolio_url: str | None = None
    coding_profiles: dict | None = None


class RecruiterRegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

    recruiter_name: str
    company_name: str
    designation: str
    company_website: str | None = None


class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    role: UserRole
    is_active: bool