# models/etudiant.py

class Etudiant:
    def __init__(self, nom, prenom, telephone, classe, notes):
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.classe = classe
        self.notes = notes
        self.moyenne = sum(notes) / len(notes) if notes else 0.0
# Cette fonction **transforme l’objet `Etudiant` en dictionnaire**. C’est pratique pour :
# - L’enregistrer dans une base de données MongoDB
# - L'afficher proprement
# - L’envoyer dans un fichier JSON, etc
    def to_dict(self):
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "telephone": self.telephone,
            "classe": self.classe,
            "notes": self.notes,
            "moyenne": self.moyenne
        }
