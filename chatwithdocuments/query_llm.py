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

# Funzione per interrogare il modello LLM con una domanda
def query_model(question, model_name="llama3:latest", base_url="http://127.0.0.1:11434"):
    setup_environment()
    logging.basicConfig(level=logging.INFO)
    
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
        # Logga e restituisce il risultato ottenuto
        logging.info(f"Result: {result}")
        return result
    except Exception as e:
        logging.error(f"Errore durante l'esecuzione della catena di domande e risposte: {e}")
        return None
