from app.services.prompt_builder import PromptBuilder


prompt = PromptBuilder.build_resume_review_prompt(
    "John Doe\nPython Developer"
)

print(prompt)