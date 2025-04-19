# services/mongo_service.py

from pymongo import MongoClient
from config.settings import MONGO_URI

client = MongoClient(MONGO_URI)
db = client['gestion_etudiants']
collection = db['etudiants']

def ajouter_etudiant(etudiant_dict):
    if collection.find_one({"telephone": etudiant_dict["telephone"]}):
        return False  # Téléphone déjà utilisé
    collection.insert_one(etudiant_dict)
    return True
