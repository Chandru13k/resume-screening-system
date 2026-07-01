from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """
    Singleton wrapper around SentenceTransformer.
    """

    _model = None

    @classmethod
    def model(cls):

        if cls._model is None:

            cls._model = SentenceTransformer(
                "all-MiniLM-L6-v2"
            )

        return cls._model

    @classmethod
    def encode(
        cls,
        text: str,
    ) -> list[float]:

        vector = cls.model().encode(
            text,
            normalize_embeddings=True,
        )

        return vector.tolist()