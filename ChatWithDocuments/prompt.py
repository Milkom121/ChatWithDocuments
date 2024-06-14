
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



#[NON FUNZIONANTE CON OLLAMA]

# prompt.py

# Importa le librerie necessarie
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings  # Importa OllamaEmbeddings dalla posizione corretta
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.llms.ollama import Ollama  # Assicurati di avere la libreria corretta per Ollama
from dotenv import load_dotenv
import logging
import requests

# Carica le variabili d'ambiente dal file .env
load_dotenv()

# Configura il logging
logging.basicConfig(level=logging.INFO)

def test_model_availability(model_name, base_url):
    try:
        response = requests.get(f"{base_url}/api/tags")
        if response.status_code == 200:
            available_models = response.json().get("models", [])
            logging.info(f"Modelli disponibili: {available_models}")
            for model in available_models:
                if model["name"] == model_name:
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

def main(question):
    try:
        model_name = "llama3:latest"
        base_url = "http://127.0.0.1:11434"

        # Verifica la disponibilità del modello
        if not test_model_availability(model_name, base_url):
            return

        # Crea un'istanza di Ollama, che rappresenta il modello di linguaggio per la chat
        chat = Ollama(model=model_name, base_url=base_url)
        logging.info(f"Chat model: {chat}")

        # Crea un'istanza di OllamaEmbeddings per ottenere rappresentazioni vettoriali dei documenti
        embeddings = OllamaEmbeddings(model=model_name, base_url=base_url)
        logging.info(f"Embeddings model: {embeddings}")

        # Inizializza il database vettoriale Chroma con la directory persistente e la funzione di embeddings
        db = Chroma(
            persist_directory="emb",   # Directory dove è salvato il database vettoriale
            embedding_function=embeddings,  # Funzione per calcolare le embeddings
        )
        logging.info(f"Vector database: {db}")

        # Converte il database vettoriale in un retriever
        retriever = db.as_retriever(return_source_documents=True)
        logging.info(f"Retriever: {retriever}")

        # Crea una catena di domande e risposte utilizzando il modello di linguaggio e il retriever
        chain = RetrievalQA.from_chain_type(
            llm=chat,           # Modello di linguaggio utilizzato per generare le risposte
            retriever=retriever, # Retriever che recupera i documenti rilevanti dal database vettoriale
            chain_type="stuff",  # Tipo di catena, in questo caso "stuff" (può variare in base alla configurazione)
        )
        logging.info(f"QA Chain: {chain}")

        # Esegue la catena di domande e risposte con una domanda specifica
        result = chain.invoke(question)
        logging.info(f"Result: {result}")

        # Stampa il risultato ottenuto
        print(result)

    except Exception as e:
        logging.error(f"Errore durante l'esecuzione della catena di domande e risposte: {e}")

if __name__ == "__main__":
    # Definisci la domanda da porre al modello
    question = "\n\nQual è il principio di funzionamento delle Lanterne di Ferro e chi le ha inventate?"
    main(question)
