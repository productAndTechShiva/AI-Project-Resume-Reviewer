"""
resume.py

Resume related API endpoints.

Responsibilities:
1. Receive uploaded resume
2. Validate uploaded file
3. Return response

AI integration will be added later.
"""

# Ollama returns the response in string format. So we need json to convert it into a Python dictionary -- json.loads(response)
import json

# FastAPI imports
from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException
from app.services.parser import ResumeParser
# added at a later stage
from app.services.prompt_builder import PromptBuilder
from app.services.ollama_service import OllamaService
from app.schemas.response_schema import (
    ResumeReviewResponse
)
from app.utils.json_extractor import (
    extract_json
)

from app.schemas.api_response import ResumeApiResponse


# --------------------------------------------------
# Create Router
# --------------------------------------------------
# All endpoints in this file belong to:
#
# /api/resume
#
# because main.py registers:
#
# prefix="/api/resume"
# --------------------------------------------------

router = APIRouter()


# --------------------------------------------------
# Supported Resume Formats
# --------------------------------------------------

ALLOWED_EXTENSIONS = [
    ".pdf",
    ".docx"
]


# --------------------------------------------------
# Test Endpoint
# --------------------------------------------------

@router.get("/test")
def test_route():
    """
    Used to verify routing works.
    """

    return {
        "success": True,
        "message": "Resume route working"
    }


# --------------------------------------------------
# Upload Resume Endpoint
# --------------------------------------------------

@router.post("/upload")
async def upload_resume(
    resume: UploadFile = File(...)
):
    """
    Upload Resume Endpoint

    Receives:
    PDF or DOCX file

    Returns:
    File information

    Example:
    POST /api/resume/upload
    """
    try:
        # ----------------------------------------------
        # Validate filename exists
        # ----------------------------------------------

        if not resume.filename:
            raise HTTPException(
                status_code=400,
                detail="Filename missing"
            )

        # ----------------------------------------------
        # Convert filename to lowercase
        # ----------------------------------------------

        filename = resume.filename.lower()

        # ----------------------------------------------
        # Validate extension
        # ----------------------------------------------

        if not (
            filename.endswith(".pdf")
            or filename.endswith(".docx")
        ):
            raise HTTPException(
                status_code=400,
                detail="Only PDF and DOCX files are allowed"
            )

        # ----------------------------------------------
        # Read uploaded file
        # ----------------------------------------------

        file_content = await resume.read()

        # ----------------------------------------------
        # File Size
        # ----------------------------------------------

        #file_size = len(file_content)

        # ----------------------------------------------
        # Extracts the raw text using parser.py
        # ----------------------------------------------

        resume_text = ResumeParser.extract_text(
            filename=resume.filename,
            file_bytes=file_content
        )

        # -----------------------------
        # Build AI prompt
        # -----------------------------

        prompt = (
            PromptBuilder
            .build_resume_review_prompt(
                resume_text
            )
        )

        # -----------------------------
        # Call Llama3
        # -----------------------------

        ai_response = (
            OllamaService.generate(
                prompt
            )
        )

        #for debugging - after test first attempt failed
        # print(ai_response)
        #print(repr(ai_response))

        # -----------------------------
        # Convert JSON string
        # to Python dictionary
        # -----------------------------
        # ----- the below code is throwing error as it adds strings before json - app received invalid json. So, replaced with new code.
        # parsed_response = json.loads(
        #     ai_response
        # )
        # ---------------- for debugging --------------------
        # print("AI_RESPONSE TYPE:", type(ai_response))
        # print("AI_RESPONSE REPR:", repr(ai_response))
        # ------------------------------------
        # parsed_response = extract_json(
        #     ai_response
        # )

        parsed_response = json.loads(
            ai_response
        )

        # ---------------- for debugging --------------------
        # print(type(parsed_response))
        # print(parsed_response)

        # -----------------------------
        # Validate response
        # -----------------------------

        review = ResumeReviewResponse(
            **parsed_response
        )

        # ---------------- for debugging --------------------
        # print("SCHEMA VALIDATION PASSED")

        # ----------------------------------------------
        # Return response
        # ----------------------------------------------

        # return {
        #     "success": True,
        #     "filename": resume.filename,
        #     "review": review.model_dump()
        # }

        response = ResumeApiResponse(
        success=True,
        filename=resume.filename,
        review=review
        )

        return response.model_dump()

    except json.JSONDecodeError:

        raise HTTPException(
            status_code=500,
            detail=(
                "AI returned invalid JSON."
        )
    )

    except Exception as e:
        import traceback

        print("\n========== FULL ERROR ==========")
        traceback.print_exc()
        print("================================\n")

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    # except Exception as e:
    #     print("\n========== ERROR ==========")
    #     print(type(e))
    #     print(str(e))
    #     print("===========================\n")

    #     raise HTTPException(
    #         status_code=500,
    #         detail=str(e)
    #     )