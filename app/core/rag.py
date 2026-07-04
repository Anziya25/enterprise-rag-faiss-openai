"""
RAG Pipeline

Combines retrieval and generation.
"""

from app.services.retriever import RetrieverService
from app.services.chat import ChatService
from app.core.prompts import SYSTEM_PROMPT, USER_PROMPT


class RAGPipeline:
    """
    Complete RAG Pipeline.
    """

    def __init__(self):

        self.retriever = RetrieverService()

        self.chat = ChatService()

    def ask(self, question: str):

        results = self.retriever.search(question)

        context = "\n\n".join(
            [doc.page_content for doc, _ in results]
        )

        prompt = (
            SYSTEM_PROMPT
            + "\n\n"
            + USER_PROMPT.format(
                context=context,
                question=question,
            )
        )

        answer = self.chat.generate(prompt)

        return {
            "answer": answer,
            "sources": [
                doc.metadata
                for doc, _ in results
            ]
        }