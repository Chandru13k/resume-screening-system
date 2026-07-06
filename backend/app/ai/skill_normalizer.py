SKILL_MAP = {

    "python3": "Python",
    "python": "Python",

    "fast api": "FastAPI",
    "fastapi": "FastAPI",

    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",

    "aws": "AWS",
    "amazon web services": "AWS",

    "docker": "Docker",

    "git": "Git",

    "redis": "Redis",

    "mysql": "MySQL",

    "mongodb": "MongoDB",

    "django": "Django",

    "flask": "Flask",

    "kubernetes": "Kubernetes",

    "linux": "Linux",

    "rest api": "REST API",

    "restful api": "REST API",

    "machine learning": "Machine Learning",

    "deep learning": "Deep Learning",

    "tensorflow": "TensorFlow",

    "pytorch": "PyTorch",

    "pandas": "Pandas",

    "numpy": "NumPy",

    "scikit learn": "Scikit-Learn",
}


def normalize(skills: list[str]) -> list[str]:

    normalized = []

    for skill in skills:

        value = skill.strip().lower()

        normalized.append(
            SKILL_MAP.get(
                value,
                skill.strip().title(),
            )
        )

    return sorted(set(normalized))