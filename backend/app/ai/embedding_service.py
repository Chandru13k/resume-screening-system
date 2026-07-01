from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """
    Generates embeddings for resumes and job descriptions.
    """

    MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

    def __init__(self):

        self.model = SentenceTransformer(
            self.MODEL_NAME
        )

    # --------------------------------------------------
    # Single Text
    # --------------------------------------------------

    def encode(
        self,
        text: str,
    ) -> list[float]:

        embedding = self.model.encode(
            text,
            normalize_embeddings=True,
        )

        return embedding.tolist()

    # --------------------------------------------------
    # Multiple Texts
    # --------------------------------------------------

    def encode_batch(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
        )

        return embeddings.tolist()