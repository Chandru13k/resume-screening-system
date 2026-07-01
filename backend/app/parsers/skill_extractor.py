import re


class SkillExtractor:
    """
    Extract skills from resume.
    """

    SKILLS = {

        # Programming

        "python",
        "java",
        "c",
        "c++",
        "c#",
        "javascript",
        "typescript",
        "go",
        "rust",
        "php",

        # Web

        "html",
        "css",
        "react",
        "angular",
        "vue",
        "node",
        "express",
        "fastapi",
        "django",
        "flask",

        # Database

        "mysql",
        "postgresql",
        "mongodb",
        "sqlite",
        "redis",

        # ML

        "machine learning",
        "deep learning",
        "nlp",
        "tensorflow",
        "keras",
        "pytorch",
        "scikit-learn",

        # AI

        "langchain",
        "llamaindex",
        "openai",
        "gemini",
        "huggingface",
        "qdrant",
        "faiss",

        # Cloud

        "aws",
        "azure",
        "gcp",
        "docker",
        "kubernetes",

        # Others

        "git",
        "linux",
        "pandas",
        "numpy",
        "opencv",
        "matplotlib",
        "power bi",
        "tableau",
        "sql",

    }
    DISPLAY_NAMES = {

        "sql": "SQL",
        "nlp": "NLP",
        "aws": "AWS",
        "gcp": "GCP",

        "html": "HTML",
        "css": "CSS",

        "javascript": "JavaScript",

        "typescript": "TypeScript",

        "fastapi": "FastAPI",

        "pytorch": "PyTorch",

        "tensorflow": "TensorFlow",

        "opencv": "OpenCV",

        "power bi": "Power BI",

        "c++": "C++",

        "c#": "C#",

    }

    @classmethod
    def extract(cls, text: str):

        lower = text.lower()

        found = set()

        for skill in cls.SKILLS:

            pattern = rf"\b{re.escape(skill)}\b"

            if re.search(pattern, lower):

                found.add(cls.DISPLAY_NAMES.get(skill, skill.title()))

        return sorted(found)