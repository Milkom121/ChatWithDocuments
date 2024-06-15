# Importa la libreria dotenv per caricare le variabili d'ambiente dal file .env
import os
from dotenv import load_dotenv

# Funzione per configurare l'ambiente di esecuzione
def setup_environment():
    # Carica le variabili d'ambiente dal file .env
    load_dotenv()
    # Disabilita la telemetria di Chroma per evitare l'invio di dati sensibili
    os.environ["CHROMA_TELEMETRY_DISABLED"] = "true"
