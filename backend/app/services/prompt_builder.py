"""
prompt_builder.py

Responsible for creating prompts
that are sent to Llama3.

Why?

Keeping prompts separate from
business logic makes them easier
to improve and maintain.
"""


class PromptBuilder:

    @staticmethod
    def build_resume_review_prompt(
        resume_text: str
    ) -> str:
        """
        Creates a structured prompt
        for resume analysis.

        Parameters:
            resume_text (str)

        Returns:
            str
        """

        prompt = f"""
You are an expert ATS Resume Reviewer and Career Coach.

Analyze the resume provided below.

IMPORTANT RULES:

IMPORTANT RULES:

1. Return ONLY a valid JSON object.
2. Do NOT include any text before the JSON.
3. Do NOT include any text after the JSON.
4. Do NOT use markdown.
5. Do NOT wrap the response in ```json blocks.
6. The response must start with {{
7. The response must end with }}
8. Score must be between 0 and 100.
9. Provide meaningful and actionable feedback.

Any response that is not valid JSON will be rejected by the system.



Required JSON Format:

{{
    "score": 0,
    "strengths": [
        ""
    ],
    "weaknesses": [
        ""
    ],
    "suggestions": [
        ""
    ],
    "improved_summary": ""
}}

Resume:

{resume_text}
"""

        return prompt.strip()