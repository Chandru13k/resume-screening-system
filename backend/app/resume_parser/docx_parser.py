from docx import Document


class DOCXParser:

    @staticmethod
    def extract_text(
        file_path: str,
    ) -> str:

        document = Document(file_path)

        paragraphs = []

        for paragraph in document.paragraphs:

            if paragraph.text.strip():

                paragraphs.append(
                    paragraph.text.strip()
                )

        return "\n".join(paragraphs)