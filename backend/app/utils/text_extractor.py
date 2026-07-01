from pathlib import Path

import fitz
from docx import Document
from fastapi import HTTPException, status


class TextExtractor:
    """
    Extract text and hyperlinks from supported resume formats.
    """

    @staticmethod
    def extract(file_path: str) -> dict:

        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return TextExtractor._extract_pdf(file_path)

        if extension == ".docx":
            return TextExtractor._extract_docx(file_path)

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unsupported file format.",
        )

    @staticmethod
    def _extract_pdf(file_path: str) -> dict:

        try:

            document = fitz.open(file_path)

            text = []
            links = []

            for page in document:

                page_text = page.get_text()

                if page_text:
                    text.append(page_text)

                # Extract embedded hyperlinks
                for link in page.get_links():

                    uri = link.get("uri")

                    if uri:
                        links.append(uri)

            document.close()

            return {
                "text": TextExtractor._clean_text(
                    "\n".join(text)
                ),
                "links": list(set(links)),
            }

        except Exception:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Unable to read PDF file.",
            )

    @staticmethod
    def _extract_docx(file_path: str) -> dict:

        try:

            document = Document(file_path)

            text = []

            for paragraph in document.paragraphs:

                if paragraph.text.strip():
                    text.append(paragraph.text)

            # python-docx doesn't easily expose hyperlinks.
            return {
                "text": TextExtractor._clean_text(
                    "\n".join(text)
                ),
                "links": [],
            }

        except Exception:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Unable to read DOCX file.",
            )

    @staticmethod
    def _clean_text(text: str):

        lines = []

        for line in text.splitlines():

            line = line.strip()

            if line:

                lines.append(line)

        return "\n".join(lines)