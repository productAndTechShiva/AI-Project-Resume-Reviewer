"""
response_schema.py

Defines the response structure
for AI Resume Reviews.

Uses Pydantic models for:

1. Validation
2. Serialization
3. Swagger documentation
"""

from pydantic import BaseModel, Field
from typing import List


class ResumeReviewResponse(BaseModel):
    """
    Standard response returned
    after resume analysis.
    """

    """
    ge=0 means >= 0 and le=100 means <= 100 ---- range 0-100
    Anything outside rejected. For example, score: 150 -- automatically rejected.
    """

    score: int = Field(   
        ge=0,
        le=100
    )

    strengths: List[str]

    weaknesses: List[str]

    suggestions: List[str]

    improved_summary: str