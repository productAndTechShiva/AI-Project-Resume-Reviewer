from app.schemas.response_schema import (
    ResumeReviewResponse
)

response = ResumeReviewResponse(
    score=80,
    strengths=[
        "Strong technical skills"
    ],
    weaknesses=[
        "Missing metrics"
    ],
    suggestions=[
        "Add measurable achievements"
    ],
    improved_summary="Experienced developer..."
)

print(response)