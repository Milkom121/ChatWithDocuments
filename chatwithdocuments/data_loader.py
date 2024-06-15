# Importa il TextLoader per caricare i documenti di testo
# Importa il CharacterTextSplitter per dividere il testo in parti più piccole
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

# Funzione per caricare e dividere il testo in chunk più piccoli
def load_and_split_text(text_path, encoding='utf-8', separator='.', chunk_size=1000, chunk_overlap=0):
    # Configura il text splitter con i parametri forniti
    text_splitter = CharacterTextSplitter(separator=separator, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    # Crea un'istanza di TextLoader per caricare il testo dal file
    loader = TextLoader(text_path, encoding=encoding)
    # Divide il testo in chunk utilizzando il text splitter configurato
    return loader.load_and_split(text_splitter=text_splitter)
