from qdrant_client import QdrantClient
from qdrant_client.http.models import (
    Distance,
    VectorParams,
    PointStruct,
)


class VectorStore:

    COLLECTION_NAME = "resume_embeddings"

    def __init__(self):

        self.client = QdrantClient(
            host="localhost",
            port=6333,
        )

        self._create_collection()

    def _create_collection(self):

        collections = self.client.get_collections()

        names = [
            collection.name
            for collection in collections.collections
        ]

        if self.COLLECTION_NAME not in names:

            self.client.create_collection(
                collection_name=self.COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE,
                ),
            )

    def upsert_resume(
        self,
        resume_id: int,
        candidate_id: int,
        embedding: list[float],
    ):

        self.client.upsert(
            collection_name=self.COLLECTION_NAME,
            points=[
                PointStruct(
                    id=resume_id,
                    vector=embedding,
                    payload={
                        "resume_id": resume_id,
                        "candidate_id": candidate_id,
                    },
                )
            ],
        )

    def search(
        self,
        embedding: list[float],
        limit: int = 10,
    ):

        response = self.client.query_points(
            collection_name=self.COLLECTION_NAME,
            query=embedding,
            limit=limit,
        )

        return response.points