
#[FUNZIONANTE CON OPENAI]
# # prompt.py

# # Importa le librerie necessarie
# from langchain_community.vectorstores import Chroma
# from langchain_openai import OpenAIEmbeddings
# from langchain.chains.retrieval_qa.base import RetrievalQA
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# import logging

# # Carica le variabili d'ambiente dal file .env
# load_dotenv()

# # Configura il logging
# logging.basicConfig(level=logging.INFO)

# def main(question):
#     try:
#         # Crea un'istanza di ChatOpenAI, che rappresenta il modello di linguaggio per la chat
#         chat = ChatOpenAI()

#         # Crea un'istanza di OpenAIEmbeddings per ottenere rappresentazioni vettoriali dei documenti
#         embeddings = OpenAIEmbeddings()

#         # Inizializza il database vettoriale Chroma con la directory persistente e la funzione di embeddings
#         db = Chroma(
#             persist_directory="emb",   # Directory dove è salvato il database vettoriale
#             embedding_function=embeddings,  # Funzione per calcolare le embeddings
#         )

#         # Converte il database vettoriale in un retriever
#         retriever = db.as_retriever(return_source_documents=True)

#         # Crea una catena di domande e risposte utilizzando il modello di linguaggio e il retriever
#         chain = RetrievalQA.from_chain_type(
#             llm=chat,           # Modello di linguaggio utilizzato per generare le risposte
#             retriever=retriever, # Retriever che recupera i documenti rilevanti dal database vettoriale
#             chain_type="stuff",  # Tipo di catena, in questo caso "stuff" (può variare in base alla configurazione)
#         )

#         # Esegue la catena di domande e risposte con una domanda specifica
#         result = chain.invoke(question)

#         # Stampa il risultato ottenuto
#         print(result)

#     except Exception as e:
#         logging.error(f"Errore durante l'esecuzione della catena di domande e risposte: {e}")

# if __name__ == "__main__":
#     # Definisci la domanda da porre al modello
#     question = "Qual è il principio di funzionamento delle Lanterne di Ferro e chi le ha inventate?"
#     main(question)



#[FUNZIONANTE CON OLLAMA]

# prompt.py
# Importa le funzioni necessarie dai moduli
from chatwithdocuments.embedding import create_embeddings
from chatwithdocuments.question_answering import create_qa_chain
from chatwithdocuments.utils import setup_environment
import logging  # Libreria per il logging

# Funzione per verificare la disponibilità del modello
def test_model_availability(model_name, base_url):
    import requests  # Importa la libreria requests per effettuare richieste HTTP
    try:
        # Effettua una richiesta GET per ottenere i modelli disponibili
        response = requests.get(f"{base_url}/api/tags")
        if response.status_code == 200:  # Verifica che la richiesta sia andata a buon fine
            available_models = response.json().get("models", [])
            logging.info(f"Modelli disponibili: {available_models}")
            for model in available_models:
                if model["name"] == model_name:  # Verifica se il modello richiesto è disponibile
                    logging.info(f"Il modello '{model_name}' è disponibile.")
                    return True
            logging.error(f"Il modello '{model_name}' non è disponibile. Assicurati di averlo scaricato e configurato correttamente.")
            return False
        else:
            logging.error(f"Errore nel recupero dei modelli disponibili: {response.status_code}, {response.text}")
            return False
    except Exception as e:
        logging.error(f"Errore durante la verifica della disponibilità del modello: {e}")
        return False

# Funzione principale che gestisce il processo di domande e risposte
def main(question):
    # Configura l'ambiente di esecuzione
    setup_environment()
    # Configura il logging
    logging.basicConfig(level=logging.INFO)
    
    # Definisce il nome del modello e l'URL base
    model_name = "llama3:latest"
    base_url = "http://127.0.0.1:11434"
    
    # Verifica la disponibilità del modello
    if not test_model_availability(model_name, base_url):
        return
    
    # Crea un'istanza di OllamaEmbeddings
    embeddings = create_embeddings(model_name, base_url)
    # Crea una catena di domande e risposte utilizzando il modello di linguaggio e il retriever
    qa_chain = create_qa_chain(embeddings, model_name, base_url)
    
    try:
        # Esegue la catena di domande e risposte con una domanda specifica
        result = qa_chain.invoke(question)
        # Logga e stampa il risultato ottenuto
        logging.info(f"Result: {result}")
        print(result)
    except Exception as e:
        logging.error(f"Errore durante l'esecuzione della catena di domande e risposte: {e}")

# Esegue la funzione principale se lo script è eseguito direttamente
if __name__ == "__main__":
    # Definisce la domanda da porre al modello
    question = "\n\nQual è il principio di funzionamento delle Lanterne di Ferro e chi le ha inventate?"
    main(question)
 