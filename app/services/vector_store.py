"""
FAISS Vector Store Service

Creates, saves, loads and searches
the vector database.
"""

from langchain_community.vectorstores import FAISS

from app.config.settings import VECTOR_STORE_PATH


class VectorStoreService:
    """
    Handles FAISS vector database operations.
    """

    def __init__(self):

        self.index_path = VECTOR_STORE_PATH

    def create_vector_store(
        self,
        documents,
        embedding_model,
    ):
        """
        Create a FAISS index from documents.
        """

        vector_store = FAISS.from_documents(
            documents,
            embedding_model,
        )

        return vector_store

    def save_vector_store(
        self,
        vector_store,
    ):
        """
        Save the FAISS index.
        """

        vector_store.save_local(
            str(self.index_path)
        )

    def load_vector_store(
        self,
        embedding_model,
    ):
        """
        Load an existing FAISS index.
        """

        return FAISS.load_local(
            str(self.index_path),
            embedding_model,
            allow_dangerous_deserialization=True,
        )