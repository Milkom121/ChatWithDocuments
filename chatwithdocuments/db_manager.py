from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = os.getenv('DB_NAME')
COLLECTION_NAME = os.getenv('COLLECTION_NAME', 'pdfs')

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def upload_pdf(filename, content):
    document = {
        "filename": filename,
        "content": content  # Salva il contenuto come testo
    }
    result = collection.insert_one(document)
    return result.inserted_id

def download_pdf(pdf_id):
    document = collection.find_one({"_id": ObjectId(pdf_id)})
    if document:
        return document['content']
    else:
        return None

def get_all_pdfs():
    return list(collection.find())
