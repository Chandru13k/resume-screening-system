from pathlib import Path

from app.resume_parser.cleaner import TextCleaner
from app.resume_parser.docx_parser import DOCXParser
from app.resume_parser.pdf_parser import PDFParser


class ResumeParser:

    @staticmethod
    def parse(
        file_path: str,
    ) -> str:

        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":

            text = PDFParser.extract_text(
                file_path
            )

        elif extension == ".docx":

            text = DOCXParser.extract_text(
                file_path
            )

        else:

            raise ValueError(
                "Unsupported resume format."
            )

        return TextCleaner.clean(text)