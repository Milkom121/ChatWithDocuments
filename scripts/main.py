

# # main.py

# import os  # Libreria per le operazioni di sistema
# import fitz  # PyMuPDF, libreria per la gestione dei file PDF
# from langchain_community.document_loaders import TextLoader  # Classe per caricare e gestire i documenti di testo
# from langchain.text_splitter import CharacterTextSplitter  # Classe per dividere il testo in parti più piccole
# from langchain_openai import OpenAIEmbeddings  # Classe per generare embeddings usando OpenAI
# from langchain_community.vectorstores import Chroma  # Classe per creare e gestire il database vettoriale Chroma
# from dotenv import load_dotenv  # Libreria per caricare le variabili d'ambiente dal file .env
# import logging  # Libreria per il logging

# # Carica le variabili d'ambiente dal file .env
# load_dotenv()

# # Configura il logging per fornire informazioni dettagliate durante l'esecuzione dello script
# logging.basicConfig(level=logging.INFO)

# # Funzione per estrarre il testo da un file PDF
# def extract_text_from_pdf(pdf_path):
#     try:
#         document = fitz.open(pdf_path)  # Apre il file PDF specificato
#         text = ""  # Inizializza una stringa vuota per accumulare il testo estratto
#         for page_num in range(document.page_count):  # Itera su tutte le pagine del PDF
#             page = document.load_page(page_num)  # Carica la pagina corrente
#             text += page.get_text()  # Aggiunge il testo della pagina corrente alla stringa di testo
#         return text  # Restituisce il testo estratto
#     except Exception as e:
#         logging.error(f"Errore nell'estrazione del testo da {pdf_path}: {e}")  # Logga eventuali errori
#         return ""  # Restituisce una stringa vuota in caso di errore

# # Funzione principale che gestisce l'intero processo
# def main():
#     embeddings = OpenAIEmbeddings()  # Crea un'istanza di OpenAIEmbeddings per generare rappresentazioni vettoriali dei documenti

#     # Configura il text splitter per dividere il testo in parti più piccole
#     text_splitter = CharacterTextSplitter(
#         separator=".",  # Usa il punto come separatore per dividere il testo
#         chunk_size=1000,  # Dimensione massima di ogni chunk (parte)
#         chunk_overlap=0  # Nessuna sovrapposizione tra i chunk
#     )

#     pdf_dir = "Manuals"  # Definisce il percorso della cartella contenente i file PDF
#     if not os.path.exists(pdf_dir):  # Controlla se la directory esiste
#         logging.error(f"La directory {pdf_dir} non esiste.")  # Logga un errore se la directory non esiste
#         return  # Termina l'esecuzione dello script

#     # Itera su tutti i file nella directory specificata
#     for filename in os.listdir(pdf_dir):
#         if filename.endswith(".pdf"):  # Verifica che il file sia un PDF
#             pdf_path = os.path.join(pdf_dir, filename)  # Costruisce il percorso completo del file PDF
#             pdf_text = extract_text_from_pdf(pdf_path)  # Estrae il testo dal file PDF

#             if pdf_text:  # Procede solo se il testo è stato estratto correttamente
#                 temp_text_path = f"{filename}_text.txt"  # Definisce il nome del file temporaneo per salvare il testo estratto
#                 with open(temp_text_path, "w", encoding="utf-8") as f:  # Apre il file temporaneo in modalità scrittura
#                     f.write(pdf_text)  # Scrive il testo estratto nel file temporaneo

#                 loader = TextLoader(temp_text_path, encoding="utf-8")  # Crea un'istanza di TextLoader per caricare il testo dal file temporaneo
#                 docs = loader.load_and_split(text_splitter=text_splitter)  # Divide il testo in documenti utilizzando il text splitter configurato

#                 # Crea un database Chroma dalle rappresentazioni vettoriali dei documenti
#                 db = Chroma.from_documents(
#                     docs,  # I documenti caricati e divisi
#                     embedding=embeddings,  # Le embeddings generate da OpenAI
#                     persist_directory="emb"  # Directory dove salvare il database
#                 )

#     # Rimuove i file di testo temporanei
#     for filename in os.listdir("."):
#         if filename.endswith("_text.txt"):  # Verifica che il file sia un file temporaneo
#             os.remove(filename)  # Rimuove il file temporaneo

# # Esegue la funzione principale se lo script è eseguito direttamente
# if __name__ == "__main__":
#     main()



#main.py
# Importa le funzioni necessarie dai moduli
from chatwithdocuments.pdf_processing import extract_text_from_pdf
from chatwithdocuments.data_loader import load_and_split_text
from chatwithdocuments.embedding import create_embeddings
from chatwithdocuments.utils import setup_environment
from langchain_community.vectorstores import Chroma
import logging  # Libreria per il logging
import os  # Libreria per le operazioni di sistema

# Funzione principale che gestisce l'intero processo
def main():
    # Configura l'ambiente di esecuzione
    setup_environment()
    # Configura il logging per fornire informazioni dettagliate durante l'esecuzione dello script
    logging.basicConfig(level=logging.INFO)
    
    # Definisce il nome del modello e l'URL base
    model_name = "llama3:latest"
    base_url = "http://127.0.0.1:11434"
    # Crea un'istanza di OllamaEmbeddings
    embeddings = create_embeddings(model_name, base_url)
    
    # Definisce il percorso della cartella contenente i file PDF
    pdf_dir = "manuals"
    # Controlla se la directory esiste
    if not os.path.exists(pdf_dir):
        # Logga un errore se la directory non esiste
        logging.error(f"La directory {pdf_dir} non esiste.")
        return

    # Inizializza una lista per accumulare i documenti caricati e divisi
    documents = []
    # Itera su tutti i file nella directory specificata
    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):  # Verifica che il file sia un PDF
            # Costruisce il percorso completo del file PDF
            pdf_path = os.path.join(pdf_dir, filename)
            # Estrae il testo dal file PDF
            pdf_text = extract_text_from_pdf(pdf_path)
            if pdf_text:  # Procede solo se il testo è stato estratto correttamente
                # Definisce il nome del file temporaneo per salvare il testo estratto
                temp_text_path = f"{filename}_text.txt"
                # Apre il file temporaneo in modalità scrittura
                with open(temp_text_path, "w", encoding="utf-8") as f:
                    # Scrive il testo estratto nel file temporaneo
                    f.write(pdf_text)
                # Divide il testo in documenti utilizzando il text splitter configurato
                docs = load_and_split_text(temp_text_path)
                # Aggiunge i documenti alla lista
                documents.extend(docs)
    
    # Elimina i file di testo temporanei
    for filename in os.listdir("."):
        if filename.endswith("_text.txt"):  # Verifica che il file sia un file temporaneo
            os.remove(filename)  # Rimuove il file temporaneo
    
    # Crea un database Chroma dalle rappresentazioni vettoriali dei documenti
    db = Chroma.from_documents(documents, embedding=embeddings, persist_directory="emb")

# Esegue la funzione principale se lo script è eseguito direttamente
if __name__ == "__main__":
    main()
