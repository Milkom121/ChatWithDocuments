# Importa OllamaEmbeddings per creare rappresentazioni vettoriali dei documenti
from langchain_community.embeddings import OllamaEmbeddings

# Funzione per creare un'istanza di OllamaEmbeddings
def create_embeddings(model_name="llama3:latest", base_url="http://127.0.0.1:11434"):
    # Restituisce un'istanza di OllamaEmbeddings configurata con il modello e l'URL base forniti
    return OllamaEmbeddings(model=model_name, base_url=base_url)
