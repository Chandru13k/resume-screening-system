from app.ai.embedding_service import EmbeddingService
from app.ai.qdrant_service import QdrantService
from app.schemas.search import (
    CandidateSearchRequest,
    CandidateSearchResponse,
    CandidateSearchResult,
)


class SemanticSearchService:
    """
    Semantic Candidate Search Service.

    Converts recruiter query into an embedding,
    searches Qdrant and returns ranked candidates.
    """

    def __init__(self):

        self.embedding_service = EmbeddingService()

        self.qdrant_service = QdrantService()

    def search(
        self,
        request: CandidateSearchRequest,
    ) -> CandidateSearchResponse:

        # ---------------------------------------
        # Generate query embedding
        # ---------------------------------------

        query_vector = self.embedding_service.encode(
            request.query
        )

        # ---------------------------------------
        # Search Qdrant
        # ---------------------------------------

        results = self.qdrant_service.search(
            vector=query_vector,
            limit=request.limit,
        )

        candidates = []

        for point in results:

            payload = point.payload or {}

            candidates.append(

                CandidateSearchResult(

                    candidate_id=payload.get(
                        "candidate_id",
                        0,
                    ),

                    resume_document_id=payload.get(
                        "resume_document_id",
                        0,
                    ),

                    full_name=payload.get(
                        "full_name",
                    ),

                    email=payload.get(
                        "email",
                    ),

                    location=payload.get(
                        "location",
                    ),

                    skills=payload.get(
                        "skills",
                        [],
                    ),

                    similarity_score=round(
                        float(point.score),
                        4,
                    ),
                )

            )

        return CandidateSearchResponse(
            candidates=candidates,
        )