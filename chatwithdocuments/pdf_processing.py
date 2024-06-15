# Importa la libreria PyMuPDF per la gestione dei file PDF
# Importa la libreria di logging per tracciare l'esecuzione del codice
import fitz
import logging

# Funzione per estrarre il testo da un file PDF
def extract_text_from_pdf(pdf_path):
    try:
        # Apre il file PDF specificato
        document = fitz.open(pdf_path)
        # Inizializza una stringa vuota per accumulare il testo estratto
        text = ""
        # Itera su tutte le pagine del PDF
        for page_num in range(document.page_count):
            # Carica la pagina corrente
            page = document.load_page(page_num)
            # Aggiunge il testo della pagina corrente alla stringa di testo
            text += page.get_text()
        # Restituisce il testo estratto
        return text
    except Exception as e:
        # Logga eventuali errori
        logging.error(f"Errore nell'estrazione del testo da {pdf_path}: {e}")
        # Restituisce una stringa vuota in caso di errore
        return ""
