from app.services.prompt_builder import PromptBuilder
from app.services.ollama_service import OllamaService

resume_text = """
John Doe

Software Engineer

Skills:
Python
React
AWS

Experience:
3 years
"""

prompt = PromptBuilder.build_resume_review_prompt(
    resume_text
)

response = OllamaService.generate(
    prompt
)

print(response)