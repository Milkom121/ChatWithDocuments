from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from chatwithdocuments.query_llm import query_model

# Modello di richiesta
class Question(BaseModel):
    question: str

# Inizializza l'app FastAPI
app = FastAPI()

# Endpoint per porre domande al modello LLM
@app.post("/ask")
def ask_question(question: Question):
    # Interroga il modello con la domanda specificata
    result = query_model(question.question)
    if result:
        return {"answer": result}
    else:
        raise HTTPException(status_code=500, detail="Errore durante l'interrogazione del modello LLM.")

# Configura CORS se necessario
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
