import re

from sqlalchemy import text

import spacy

nlp = spacy.load("en_core_web_sm")


class EntityExtractor:
    """
    Extract common entities from resume text.
    """

    EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    PHONE_REGEX = (
        r"(?:\+?\d{1,3}[\s-]?)?"
        r"(?:\(?\d{2,5}\)?[\s-]?)?"
        r"\d{3,5}[\s-]?\d{4}"
    )

    GITHUB_REGEX = r"https?://(?:www\.)?github\.com/[^\s]+"

    LINKEDIN_REGEX = (
        r"https?://(?:www\.)?linkedin\.com/[^\s]+"
    )

    PORTFOLIO_REGEX = (
        r"https?://(?!.*linkedin)(?!.*github)[^\s]+"
    )

    CODING_PATTERNS = {
        "leetcode": r"https?://(?:www\.)?leetcode\.com/[^\s]+",
        "codechef": r"https?://(?:www\.)?codechef\.com/[^\s]+",
        "hackerrank": r"https?://(?:www\.)?hackerrank\.com/[^\s]+",
        "codeforces": r"https?://(?:www\.)?codeforces\.com/[^\s]+",
    }

    @staticmethod
    def extract_email(text: str):

        match = re.search(
            EntityExtractor.EMAIL_REGEX,
            text,
        )

        return match.group(0) if match else None

    @staticmethod
    def extract_phone(text: str):

        match = re.search(
            EntityExtractor.PHONE_REGEX,
            text,
        )

        return match.group(0).strip() if match else None

    @staticmethod
    def extract_github(text: str):

        match = re.search(
            EntityExtractor.GITHUB_REGEX,
            text,
        )

        return match.group(0) if match else None

    @staticmethod
    def extract_linkedin(text: str):

        match = re.search(
            EntityExtractor.LINKEDIN_REGEX,
            text,
        )

        return match.group(0) if match else None

    @staticmethod
    def extract_portfolio(text: str):

        urls = re.findall(
            EntityExtractor.PORTFOLIO_REGEX,
            text,
        )

        if urls:
            return urls[0]

        return None

    @staticmethod
    def extract_coding_profiles(text: str):

        profiles = {}

        for platform, pattern in EntityExtractor.CODING_PATTERNS.items():

            match = re.search(pattern, text)

            if match:

                profiles[platform] = match.group(0)

        return profiles

    @staticmethod
    def extract_name(text: str):

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        if not lines:
            return None

        first_line = lines[0]

        if "@" in first_line or "http" in first_line.lower():
            return None

        return first_line

    @staticmethod
    def extract_location(text: str):

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        if len(lines) < 2:
            return None

        second_line = lines[1]

        # Example:
        # Bengaluru, India | email | phone

        location = second_line.split("|")[0].strip()

        return location