from pathlib import Path
from uuid import uuid4

from fastapi import HTTPException, UploadFile, status

# Allowed file extensions
ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
}

# Maximum upload size (10 MB)
MAX_FILE_SIZE = 10 * 1024 * 1024

# Upload directory
UPLOAD_DIR = Path("uploads/resumes")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def validate_file(file: UploadFile) -> None:
    """
    Validate uploaded file.
    """

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF and DOCX files are allowed.",
        )


def generate_filename(original_filename: str) -> str:
    """
    Generate unique filename.
    """

    extension = Path(original_filename).suffix.lower()

    return f"{uuid4().hex}{extension}"


async def save_upload_file(file: UploadFile) -> tuple[str, str, int]:
    """
    Save uploaded file to disk.

    Returns:
        stored_filename
        file_path
        file_size
    """

    validate_file(file)

    stored_filename = generate_filename(file.filename)

    destination = UPLOAD_DIR / stored_filename

    content = await file.read()

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Maximum file size is 10 MB.",
        )

    destination.write_bytes(content)

    return (
        stored_filename,
        str(destination),
        len(content),
    )