from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import List
from chatwithdocuments.query_llm import query_model
from chatwithdocuments.db_manager import upload_pdf
from chatwithdocuments.pdf_processing import extract_text_from_pdf
import logging
import os
import traceback

# Configura il logging per scrivere su console e file
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])

# Modello di richiesta
class Question(BaseModel):
    question: str

# Inizializza l'app FastAPI
app = FastAPI()

# Endpoint per porre domande al modello LLM
@app.post("/ask")
def ask_question(question: Question):
    logging.info(f"Ricevuta domanda: {question.question}")
    
    # Interroga il modello con la domanda specificata
    result = query_model(question.question)
    if result:
        logging.info(f"Risposta dal modello: {result}")
        return {"answer": result}
    else:
        logging.error("Errore durante l'interrogazione del modello LLM.")
        raise HTTPException(status_code=500, detail="Errore durante l'interrogazione del modello LLM.")

# Endpoint per caricare più file PDF nel database
@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):
    uploaded_file_ids = []
    try:
        for file in files:
            logging.info(f"Ricevuto file: {file.filename}")
            # Legge il contenuto del file
            content = await file.read()

            # Salva il file temporaneamente per l'elaborazione
            temp_file_path = f"/tmp/{file.filename}"
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(content)

            # Estrai il testo dal file PDF
            pdf_text = extract_text_from_pdf(temp_file_path)

            # Carica il contenuto testuale nel database
            file_id = upload_pdf(file.filename, pdf_text)
            logging.info(f"File caricato con ID: {file_id}")
            uploaded_file_ids.append(str(file_id))

            # Rimuovi il file temporaneo
            os.remove(temp_file_path)
        
        return {"file_ids": uploaded_file_ids}
    except Exception as e:
        logging.error(f"Errore durante il caricamento dei file: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail="Errore durante il caricamento dei file.")

# Configura CORS per permettere le richieste dal frontend
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:3000",  # Ad esempio, se stai usando React per il frontend
    # Aggiungi altri domini autorizzati
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Avvia l'app FastAPI con Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
