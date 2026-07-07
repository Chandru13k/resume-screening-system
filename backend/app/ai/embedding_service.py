from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """
    Generates embeddings for resumes and job descriptions.
    """

    MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

    # Load model only once
    model = SentenceTransformer(MODEL_NAME)

    @staticmethod
    def encode(text: str) -> list[float]:
        embedding = EmbeddingService.model.encode(
            text,
            normalize_embeddings=True,
        )

        return embedding.tolist()

    @staticmethod
    def encode_batch(texts: list[str]) -> list[list[float]]:
        embeddings = EmbeddingService.model.encode(
            texts,
            normalize_embeddings=True,
        )

        return embeddings.tolist()