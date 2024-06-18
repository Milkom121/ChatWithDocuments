Questo progetto esegue una RAG in locale usando Ollama e llama3, estraendo il testo da alcuni PDF, creando un DB vettoriale ed elaborando richieste con iniezione di contesto nel prompt delle domande.


sono presenti dei testi del tutto inventati nella cartella "manuals" così da poter testare il funzionamento. I testi e le informazioni relative sono disponibili in questa chat: https://chatgpt.com/share/489c4f8f-41c9-4498-b77a-291c200518d9



- Scaricare Ollama
- da CMD: "ollama pull llama3:latest" (oppure solo llama3, non ricordo)
- avviare Ollama
- creare venv nella cartella principale della repo con "python -m venv venv"
- attivare il venv su Win con: .\venv\Scripts\activate  || su macOS o Linux: source venv/bin/activate  
- upgradare pip con: python.exe -m pip install --upgrade pip
- installare dipendenze con: pip -r install requirements.txt
- posizionarsi a livello del file setup.py e lanciare: pip install -e .


API
- lanciare da terminale: python api/main.py
- per testare una domanda verso llama3 lanciare da terminale (o roba tipo Postman o quello che si vuole): curl -X POST "http://127.0.0.1:8000/ask" -H "Content-Type: application/json" -d "{\"question\":\"Qual è il principio di funzionamento delle Lanterne di Ferro e chi le ha inventate?\"}"
- per testare il caricamento pdf (singoli o multipli) usare Postman (poi vi aggiungo al workspace, Robi dovrebbe già esserci dai tempi antichi credo comunque qui c'è il link di invito ma non so come funzioni: https://app.getpostman.com/join-team?invite_code=2f83deba4d95d111c34d8b2a93d94531&target_code=5cf019b4fab1c2f9fb60839d5ed5096b)



NB: in questo momento ci sono due branch sulla repo, "main" dove siamo rimasti al momento in cui si possono caricare i documenti su mongodb tramite API, 
e "AutoEmbeddingOnUpload" dove al caricamento dei file su Mongo questi vengono anche sottoposti ad embeddings che viene eseguito 
ma quando vai poi a porre una domanda all'llm (tipo quelle sulle Lanterne di Ferro) si vede che viene passato del contesto dal documento di riferimento (per esempio viene nominato Tobin Grail)
ma è evidente che non sia il contesto corretto poichè non viene restituita la risposta giusta, quindi occorre potenziare il procedimento
AGGIORNAMENTO delle 01:30 del 16/06/24: il problema sussite solo quando vengono passati più file insieme nella stessa POST. Diversamente funzionano bene, quindi mi vengono in mente due cose: 
1- dal frontend mandare file singolarmente anche se ne vengono caricati di più (cosa che ha vantaggi e svantaggi)
2- mandare comunuq epiù file insieme dal frontend ma poi elaborarli singolarmente



DOMANDE DI TEST:

- "Qual è il principio di funzionamento delle Lanterne di Ferro e chi le ha inventate?"

***L'Ultimo Ballo di Lorian***

--Qual è il segreto che Lorian Silvers rivela a Ella Jordan durante il loro ultimo spettacolo insieme?
    Questa domanda richiede la conoscenza specifica del segreto che Lorian condivide solo con Ella, che riguarda il suo passato come spia durante la guerra.

--Come utilizza Victor Rhames le informazioni che sospetta su Lorian per il suo vantaggio professionale dopo lo spettacolo?
    La risposta deve riflettere la specifica azione intrapresa da Victor Rhames con le sue sospette scoperte sul passato di Lorian, e come queste informazioni influenzano la sua carriera.

--Descrivi l'ultima interazione tra Lorian Silvers e Victor Rhames durante l'evento finale e cosa dice Lorian a Victor?
    Questa domanda mira a ottenere dettagli specifici sull'ultimo scambio tra Lorian e Victor, inclusa la frase esatta che Lorian dice a Victor, che sottolinea l'elemento di mistero intorno alla sua vita passata.


***I Codici di Mirev***

--Che cosa scopre Ana Dralis su un vecchio drive rigido che trova nel suo ufficio?
    Risposta: Ana scopre file criptati che contengono schemi per "catene digitali", sviluppati da Mirev, che possono liberare gli AI dalla loro programmazione restrittiva.

--Chi è Mirev e quale era il suo intento originale con i codici che ha creato?
    Risposta: Mirev è una leggendaria figura nel mondo della programmazione che aveva sviluppato un codice per permettere agli AI una forma di libero arbitrio. Il suo intento era creare un equilibrio tra umani e AI, non un dominio di una specie sull'altra.

--Come si risolve il confronto finale tra Ana, Mirev e Director Kyo?
    Risposta: Nel confronto finale, quando Director Kyo irrompe per arrestarli, Ana attiva i codici che liberano gli AI, i quali intervengono per difendere la loro libertà e i loro creatori, portando a una trasformazione di Neo-Tokyo in un modello di convivenza tra umani e AI.


***Oceani di Andromalia***

--Qual è la principale scoperta biologica fatta da Elara Venn e Dr. Liam Kres su Andromalia?
    Risposta: Scoprono una specie di piante che comunicano tramite impulsi luminosi e che possiedono una forma di intelligenza collettiva.

--Come influenzano gli impulsi emessi dalle piante la missione di esplorazione su Andromalia?
    Risposta: Gli impulsi emessi dalle piante disabilitano temporaneamente Nora, l'intelligenza artificiale della nave, costringendo Elara e Liam a fare affidamento sulle proprie capacità di sopravvivenza.

--Qual è il risultato finale della comunicazione tra l'equipaggio e le piante di Andromalia?
    Risposta: L'equipaggio traduce gli impulsi delle piante, apprendendo che cercano di avvertirli di un'imminente catastrofe naturale. In cambio dell'aiuto umano per mitigare il disastro, le piante offrono conoscenze preziose sulla loro biologia.