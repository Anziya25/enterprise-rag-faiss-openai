"""
Embedding Service

Creates and manages Hugging Face embeddings.
"""

from langchain_huggingface import HuggingFaceEmbeddings

from app.config.settings import EMBEDDING_MODEL


class EmbeddingService:
    """
    Handles embedding generation using Hugging Face.
    """

    def __init__(self):

        self.embedding_model = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={
                "device": "cpu"
            },
            encode_kwargs={
                "normalize_embeddings": True
            }
        )

    def get_embedding_model(self):
        """
        Return the embedding model.
        """
        return self.embedding_model

    def embed_query(self, query: str):
        """
        Generate embedding for a user query.
        """
        return self.embedding_model.embed_query(query)

    def embed_documents(self, texts):
        """
        Generate embeddings for multiple text chunks.
        """
        return self.embedding_model.embed_documents(texts)