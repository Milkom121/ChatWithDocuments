import fitz  # PyMuPDF
import logging

def extract_text_from_pdf(pdf_path):
    try:
        document = fitz.open(pdf_path)
        text = ""
        for page_num in range(document.page_count):
            page = document.load_page(page_num)
            text += page.get_text()
        return text
    except Exception as e:
        logging.error(f"Errore nell'estrazione del testo da {pdf_path}: {e}")
        return ""
