"""
Document Loader

Responsible for reading different document formats
and converting them into LangChain Document objects.
"""

from pathlib import Path
from typing import List

import fitz  # PyMuPDF
from docx import Document as DocxDocument
from langchain_core.documents import Document
class DocumentLoader:
    """
    Loads documents from TXT, PDF and DOCX files.
    """
    def load_txt(self, file_path: str) -> List[Document]:
        """
        Load a text file and return it as a LangChain Document.
        """

        path = Path(file_path)

        with open(path, "r", encoding="utf-8") as file:
            text = file.read()

        document = Document(
            page_content=text,
            metadata={
                "source": path.name,
                "file_type": ".txt"
            }
        )

        return [document]