from app.utils.skill_matcher import SkillMatcher

job = """
Looking for Python developer with FastAPI,
SQL,
Docker,
Machine Learning,
NLP
"""

candidate = [
    "Python",
    "FastAPI",
    "SQL",
    "NLP",
]

result = SkillMatcher.compare(
    job,
    candidate,
)

print(result)