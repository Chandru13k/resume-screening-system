from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    PointStruct,
    VectorParams,
)

from app.core.config import settings


class QdrantService:
    """
    Handles all Qdrant operations.
    """

    COLLECTION_NAME = "candidate_resumes"

    VECTOR_SIZE = 384

    def __init__(self):

        self.client = QdrantClient(
            url=settings.QDRANT_URL,
        )

        self.create_collection()

    # --------------------------------------------------
    # Create Collection
    # --------------------------------------------------

    def create_collection(self):

        collections = self.client.get_collections()

        existing = [
            collection.name
            for collection in collections.collections
        ]

        if self.COLLECTION_NAME in existing:
            return

        self.client.create_collection(
            collection_name=self.COLLECTION_NAME,
            vectors_config=VectorParams(
                size=self.VECTOR_SIZE,
                distance=Distance.COSINE,
            ),
        )

    # --------------------------------------------------
    # Insert / Update Vector
    # --------------------------------------------------

    def upload_resume_vector(
        self,
        resume_id: int,
        vector: list[float],
        payload: dict,
    ):

        self.client.upsert(
            collection_name=self.COLLECTION_NAME,
            wait=True,
            points=[
                PointStruct(
                    id=resume_id,
                    vector=vector,
                    payload=payload,
                )
            ],
        )

    # --------------------------------------------------
    # Search
    # --------------------------------------------------

    def search(
        self,
        vector: list[float],
        limit: int = 10,
    ):

        return self.client.query_points(
            collection_name=self.COLLECTION_NAME,
            query=vector,
            limit=limit,
        ).points

    # --------------------------------------------------
    # Delete
    # --------------------------------------------------

    def delete_vector(
        self,
        resume_id: int,
    ):

        self.client.delete(
            collection_name=self.COLLECTION_NAME,
            points_selector=[resume_id],
        )