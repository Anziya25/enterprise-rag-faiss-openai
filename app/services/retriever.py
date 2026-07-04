"""
Retriever Service

Searches the FAISS vector database.
"""

from app.services.embedder import EmbeddingService
from app.services.vector_store import VectorStoreService


class RetrieverService:
    """
    Retrieves relevant chunks from FAISS.
    """

    def __init__(self):

        self.embedder = EmbeddingService()

        self.vector_store = VectorStoreService()

        self.db = self.vector_store.load_vector_store(
            self.embedder.get_embedding_model()
        )

    def search(
        self,
        query: str,
        k: int = 5,
    ):
        """
        Retrieve top-k similar chunks.
        """

        results = self.db.similarity_search_with_score(
            query,
            k=k,
        )

        return results