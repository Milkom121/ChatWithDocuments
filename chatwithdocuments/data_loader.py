from langchain.text_splitter import CharacterTextSplitter
from langchain_core.documents.base import Document

# Funzione per caricare e dividere il testo
def load_and_split_text(content, separator=".", chunk_size=1000, chunk_overlap=200):
    text_splitter = CharacterTextSplitter(
        separator=separator,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    texts = text_splitter.split_text(content)
    documents = [Document(page_content=text) for text in texts]
    return documents
