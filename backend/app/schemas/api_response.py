from pydantic import BaseModel

from app.schemas.response_schema import (
    ResumeReviewResponse
)


class ResumeApiResponse(
    BaseModel
):

    success: bool

    filename: str

    review: ResumeReviewResponse