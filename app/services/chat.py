"""
Chat Service

Handles interaction with the local LLM using Ollama.
"""

from langchain_ollama import ChatOllama

from app.config.settings import LLM_MODEL


class ChatService:
    """
    Handles LLM inference.
    """

    def __init__(self):

        self.llm = ChatOllama(
            model=LLM_MODEL,
            temperature=0,
        )

    def generate(self, prompt: str):
        """
        Generate an answer from the local LLM.
        """

        response = self.llm.invoke(prompt)

        return response.content