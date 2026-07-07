import json

import google.generativeai as genai

from app.core.config import settings


class GeminiService:

    def __init__(self):

        genai.configure(
            api_key=settings.GEMINI_API_KEY,
        )

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate_candidate_insights(
        self,
        resume_text: str,
        job_description: str,
        overall_score: float,
        matched_skills: list[str],
        missing_skills: list[str],
    ) -> dict:

        prompt = f"""
You are an experienced Technical Recruiter.

Analyze the candidate based on the resume and job description.

Overall AI Match Score:
{overall_score}

Matched Skills:
{matched_skills}

Missing Skills:
{missing_skills}

Resume:

{resume_text}

Job Description:

{job_description}

Return ONLY valid JSON.

Format:

{{
  "summary":"...",
  "strengths":[
      "...",
      "..."
  ],
  "weaknesses":[
      "...",
      "..."
  ],
  "score_explanation":"...",
  "interview_questions":[
      "...",
      "...",
      "...",
      "...",
      "..."
  ],
  "recommendation":"..."
}}
"""

        response = self.model.generate_content(
            prompt
        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace(
                "```json",
                "",
            )

        if text.endswith("```"):
            text = text[:-3]

        return json.loads(text.strip())