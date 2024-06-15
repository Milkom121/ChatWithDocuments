


#main.py [FUNZIONANTE]
# # Importa le funzioni necessarie dai moduli
# from chatwithdocuments.pdf_processing import extract_text_from_pdf
# from chatwithdocuments.data_loader import load_and_split_text
# from chatwithdocuments.embedding import create_embeddings
# from chatwithdocuments.utils import setup_environment
# from langchain_community.vectorstores import Chroma
# import logging  # Libreria per il logging
# import os  # Libreria per le operazioni di sistema

# # Funzione principale che gestisce l'intero processo
# def main():
#     # Configura l'ambiente di esecuzione
#     setup_environment()
#     # Configura il logging per fornire informazioni dettagliate durante l'esecuzione dello script
#     logging.basicConfig(level=logging.INFO)
    
#     # Definisce il nome del modello e l'URL base
#     model_name = "llama3:latest"
#     base_url = "http://127.0.0.1:11434"
#     # Crea un'istanza di OllamaEmbeddings
#     embeddings = create_embeddings(model_name, base_url)
    
#     # Definisce il percorso della cartella contenente i file PDF
#     pdf_dir = "manuals"
#     # Controlla se la directory esiste
#     if not os.path.exists(pdf_dir):
#         # Logga un errore se la directory non esiste
#         logging.error(f"La directory {pdf_dir} non esiste.")
#         return

#     # Inizializza una lista per accumulare i documenti caricati e divisi
#     documents = []
#     # Itera su tutti i file nella directory specificata
#     for filename in os.listdir(pdf_dir):
#         if filename.endswith(".pdf"):  # Verifica che il file sia un PDF
#             # Costruisce il percorso completo del file PDF
#             pdf_path = os.path.join(pdf_dir, filename)
#             # Estrae il testo dal file PDF
#             pdf_text = extract_text_from_pdf(pdf_path)
#             if pdf_text:  # Procede solo se il testo è stato estratto correttamente
#                 # Definisce il nome del file temporaneo per salvare il testo estratto
#                 temp_text_path = f"{filename}_text.txt"
#                 # Apre il file temporaneo in modalità scrittura
#                 with open(temp_text_path, "w", encoding="utf-8") as f:
#                     # Scrive il testo estratto nel file temporaneo
#                     f.write(pdf_text)
#                 # Divide il testo in documenti utilizzando il text splitter configurato
#                 docs = load_and_split_text(temp_text_path)
#                 # Aggiunge i documenti alla lista
#                 documents.extend(docs)
    
#     # Elimina i file di testo temporanei
#     for filename in os.listdir("."):
#         if filename.endswith("_text.txt"):  # Verifica che il file sia un file temporaneo
#             os.remove(filename)  # Rimuove il file temporaneo
    
#     # Crea un database Chroma dalle rappresentazioni vettoriali dei documenti
#     db = Chroma.from_documents(documents, embedding=embeddings, persist_directory="emb")

# # Esegue la funzione principale se lo script è eseguito direttamente
# if __name__ == "__main__":
#     main()


from chatwithdocuments.pdf_processing import extract_text_from_pdf
from chatwithdocuments.data_loader import load_and_split_text
from chatwithdocuments.embedding import create_embeddings
from chatwithdocuments.utils import setup_environment
from chatwithdocuments.db_manager import upload_pdf, get_all_pdfs
from langchain_community.vectorstores import Chroma
import logging

# Funzione principale che gestisce l'intero processo
def main():
    setup_environment()
    logging.basicConfig(level=logging.INFO)
    
    model_name = "llama3:latest"
    base_url = "http://127.0.0.1:11434"
    embeddings = create_embeddings(model_name, base_url)
    
    # Inizializza una lista per accumulare i documenti caricati e divisi
    documents = []
    
    # Carica tutti i PDF dal database
    pdfs = get_all_pdfs()
    for pdf in pdfs:
        pdf_text = pdf['content']
        if pdf_text:
            # Divide il testo in documenti utilizzando il text splitter configurato
            docs = load_and_split_text(pdf_text)
            documents.extend(docs)
    
    # Crea un database Chroma dalle rappresentazioni vettoriali dei documenti
    db = Chroma.from_documents(documents, embedding=embeddings, persist_directory="emb")

# Esegue la funzione principale se lo script è eseguito direttamente
if __name__ == "__main__":
    main()
