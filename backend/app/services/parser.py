"""
parser.py

Responsible for extracting text from:

1. PDF resumes
2. DOCX resumes

Output:
Plain text string

Example:

Input:
resume.pdf

Output:
"John Doe\nSoftware Engineer\nSkills..."
"""

import io

from pypdf import PdfReader
from docx import Document



class ResumeParser:
    """
    Handles resume text extraction.
    """

    @staticmethod
    def extract_pdf_text(file_bytes: bytes) -> str:
        """
        Extract text from PDF file.

        Parameters:
            file_bytes (bytes)

        Returns:
            str
        """

        try:

            pdf_stream = io.BytesIO(file_bytes)

            pdf_reader = PdfReader(pdf_stream)

            extracted_text = ""

            for page in pdf_reader.pages:

                page_text = page.extract_text()

                if page_text:
                    extracted_text += page_text + "\n"

            return extracted_text.strip()

        except Exception as e:
            raise Exception(
                f"PDF parsing failed: {str(e)}"
            )

    @staticmethod
    def extract_docx_text(file_bytes: bytes) -> str:
        """
        Extract text from DOCX file.

        Parameters:
            file_bytes (bytes)

        Returns:
            str
        """

        try:

            doc_stream = io.BytesIO(file_bytes)

            document = Document(doc_stream)

            paragraphs = []

            for paragraph in document.paragraphs:

                if paragraph.text.strip():

                    paragraphs.append(
                        paragraph.text.strip()
                    )

            return "\n".join(paragraphs)

        except Exception as e:

            raise Exception(
                f"DOCX parsing failed: {str(e)}"
            )

    @staticmethod
    def extract_text(
        filename: str,
        file_bytes: bytes
    ) -> str:
        """
        Auto detect file type and extract text.
        """

        filename = filename.lower()

        if filename.endswith(".pdf"):

            return ResumeParser.extract_pdf_text(
                file_bytes
            )

        elif filename.endswith(".docx"):

            return ResumeParser.extract_docx_text(
                file_bytes
            )

        raise Exception(
            "Unsupported file type"
        )