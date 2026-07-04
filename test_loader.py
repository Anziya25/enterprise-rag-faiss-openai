from app.services.document_loader import DocumentLoader

loader = DocumentLoader()

documents = loader.load_txt("documents/notes/sample.txt")

print("=" * 50)

print("Number of Documents:", len(documents))

print("=" * 50)

print(documents[0].page_content)

print("=" * 50)

print(documents[0].metadata)