# Importa le librerie necessarie per la catena di domande e risposte
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_community.llms.ollama import Ollama

# Funzione per creare una catena di domande e risposte
def create_qa_chain(embedding, model_name="llama3:latest", base_url="http://127.0.0.1:11434"):
    # Crea un'istanza di Ollama, che rappresenta il modello di linguaggio per la chat
    chat = Ollama(model=model_name, base_url=base_url)
    # Inizializza il database vettoriale Chroma con la directory persistente e la funzione di embeddings
    db = Chroma(persist_directory="emb", embedding_function=embedding)
    # Converte il database vettoriale in un retriever
    retriever = db.as_retriever(return_source_documents=True)
    # Restituisce una catena di domande e risposte configurata
    return RetrievalQA.from_chain_type(llm=chat, retriever=retriever, chain_type="stuff")
