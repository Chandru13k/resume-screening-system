from enum import Enum


class ApplicationStatus(str, Enum):

    APPLIED = "APPLIED"

    SHORTLISTED = "SHORTLISTED"

    INTERVIEW = "INTERVIEW"

    REJECTED = "REJECTED"

    HIRED = "HIRED"