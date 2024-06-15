from chatwithdocuments.embedding import create_embeddings
from langchain_community.vectorstores import Chroma
from chatwithdocuments.data_loader import load_and_split_text

def on_file_uploaded(file_id, filename, content):
    # Esegui le operazioni desiderate dopo il caricamento del file
    print(f"File caricato: {filename} con ID: {file_id}")

    # Genera gli embeddings per il contenuto del file
    embeddings = create_embeddings()
    
    # Divide il contenuto in documenti
    documents = load_and_split_text(content)
    
    # Crea o aggiorna il database vettoriale Chroma
    db = Chroma.from_documents(documents, embedding=embeddings, persist_directory="emb")
    print(f"Embeddings creati e aggiunti al database vettoriale per il file: {filename}")
