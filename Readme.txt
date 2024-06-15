Questo progetto esegue una RAG in locale usando Ollama e llama3, estraendo il testo da alcuni PDF, creando un DB vettoriale ed elaborando richieste con iniezione di contesto nel prompt delle domande.


sono presenti dei testi del tutto inventati nella cartella "manuals" così da poter testare il funzionamento. I testi e le informazioni relative sono disponibili in questa chat: https://chatgpt.com/share/489c4f8f-41c9-4498-b77a-291c200518d9



- Scaricare Ollama
- da CMD: "ollama pull llama3:latest" (oppure solo llama3, non ricordo)
- avviare Ollama
- creare venv nella cartella principale della repo con "python -m venv venv"
- attivare il venv con ".\venv\Scripts\activate" su Win mentre "source venv/bin/activate"  su macOS o Linux
- upgradare pip con: "python.exe -m pip install --upgrade pip"
- installare dipendenze con: "pip -r install requirements.txt"
- posizionarsi a livello del file setup.py e lanciare "pip install -e ."
- per parsare i pdf in manuals e creare il DB "emb" raggiungere il file main.py e lanciarlo con: "python main.py"
- lanciare poi prompt.py con: "python prompt.py"

