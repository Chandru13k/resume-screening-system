from app.ai.indexing_service import IndexingService


def test_index_resume_uses_embedding_service_instance(monkeypatch):
    calls = {}

    class DummyEmbeddingService:
        def __init__(self):
            calls["initialized"] = True

        def encode(self, text):
            calls["text"] = text
            return [0.1, 0.2]

    class DummyVectorStore:
        def upsert_resume(self, resume_id, candidate_id, embedding):
            calls["upsert"] = (resume_id, candidate_id, embedding)

    monkeypatch.setattr("app.ai.indexing_service.EmbeddingService", DummyEmbeddingService)
    monkeypatch.setattr("app.ai.indexing_service.VectorStore", DummyVectorStore)

    service = IndexingService()
    service.index_resume(resume_id=7, candidate_id=3, text="hello world")

    assert calls["initialized"] is True
    assert calls["text"] == "hello world"
    assert calls["upsert"] == (7, 3, [0.1, 0.2])
