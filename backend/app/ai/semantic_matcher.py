from app.ai.embedding_service import EmbeddingService
from app.ai.vector_store import VectorStore


class SemanticMatcher:
    """
    Performs semantic resume search using Qdrant.
    """

    def __init__(self):
        self.vector_store = VectorStore()

    def search(
        self,
        job_description: str,
        limit: int = 10,
    ):
        embedding = EmbeddingService.encode(job_description)

        results = self.vector_store.search(
            embedding=embedding,
            limit=limit,
        )

        candidates = []

        for result in results:
            candidates.append(
                {
                    "resume_id": result.payload["resume_id"],
                    "candidate_id": result.payload["candidate_id"],
                    "semantic_score": round(result.score * 100, 2),
                }
            )

        return candidates