from app.ai.embedding_service import EmbeddingService
from app.ai.vector_store import VectorStore


class IndexingService:
    """
    Responsible for indexing parsed resumes into Qdrant.
    """

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()

    def index_resume(
        self,
        resume_id: int,
        candidate_id: int,
        text: str,
    ) -> None:

        if not text:
            return

        embedding = self.embedding_service.encode(text)

        self.vector_store.upsert_resume(
            resume_id=resume_id,
            candidate_id=candidate_id,
            embedding=embedding,
        )