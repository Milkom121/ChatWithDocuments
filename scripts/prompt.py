
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
# Importa la funzione per interrogare il modello LLM
from chatwithdocuments.query_llm import query_model

# Funzione principale che gestisce il processo di domande e risposte
def main():
    # Definisce la domanda da porre al modello
    question = "\n\nQual è il principio di funzionamento delle Lanterne di Ferro e chi le ha inventate?"

    # Interroga il modello con la domanda specifica
    result = query_model(question)
    
    # Stampa il risultato ottenuto
    if result:
        print(result)
    else:
        print("Errore durante l'interrogazione del modello LLM.")

# Esegue la funzione principale se lo script è eseguito direttamente
if __name__ == "__main__":
    main()
