# Importation de la classe Etudiant pour créer des objets étudiants
from models.etudiant import Etudiant

# Importation de la fonction d'ajout et de la collection MongoDB
from services.mongo_service import ajouter_etudiant, collection


# 🎓 Menu pour ajouter un étudiant
def ajouter_etudiant_menu():
    # Demander les informations de l'étudiant à l'utilisateur
    nom = input("Nom: ")
    prenom = input("Prénom: ")
    telephone = input("Téléphone: ")
    classe = input("Classe: ")
    notes = list(map(float, input("Notes (séparées par des espaces): ").split()))

    # Vérifie que les notes sont valides (entre 0 et 20)
    if any(note < 0 or note > 20 for note in notes):
        print("❌ Erreur : Les notes doivent être entre 0 et 20.")
        return

    # Création de l'objet étudiant
    etudiant = Etudiant(nom, prenom, telephone, classe, notes)

    # Ajout de l'étudiant à MongoDB (via mongo_service)
    if ajouter_etudiant(etudiant.to_dict()):
        print("✅ Étudiant ajouté avec succès.")
    else:
        print("❌ Téléphone déjà utilisé.")


# 📋 Afficher tous les étudiants
def afficher_etudiants():
    etudiants = list(collection.find({}, {'_id': False}))  # Exclure le champ Mongo _id
    for etudiant in etudiants:
        print(f"Nom: {etudiant['nom']}, Prénom: {etudiant['prenom']}, Téléphone: {etudiant['telephone']}, Classe: {etudiant['classe']}, Moyenne: {etudiant['moyenne']}")


# 🔍 Rechercher un étudiant par champ
def rechercher_etudiant():
    champ = input("Rechercher par (nom, prenom, telephone, classe): ")
    valeur = input("Valeur: ")
    etudiants = list(collection.find({champ: valeur}, {'_id': False}))
    if etudiants:
        for etudiant in etudiants:
            print(f"Nom: {etudiant['nom']}, Prénom: {etudiant['prenom']}, Téléphone: {etudiant['telephone']}, Classe: {etudiant['classe']}, Moyenne: {etudiant['moyenne']}")
    else:
        print("❌ Aucun résultat.")


# 📝 Modifier les notes d’un étudiant
def modifier_notes():
    tel = input("Téléphone de l'étudiant: ")
    etudiant = collection.find_one({"telephone": tel})
    if etudiant:
        notes = list(map(float, input("Nouvelles notes (séparées par des espaces): ").split()))
        moyenne = sum(notes) / len(notes)
        # Mise à jour des notes et de la moyenne
        collection.update_one({"telephone": tel}, {"$set": {"notes": notes, "moyenne": moyenne}})
        print("✅ Notes modifiées.")
    else:
        print("❌ Étudiant non trouvé.")


# 🗑️ Supprimer un étudiant par téléphone
def supprimer_etudiant():
    tel = input("Téléphone: ")
    collection.delete_one({"telephone": tel})
    print("✅ Étudiant supprimé.")


# 📊 Trier les étudiants par moyenne décroissante
def trier_par_moyenne():
    etudiants = list(collection.find({}, {'_id': False}).sort("moyenne", -1))  # -1 pour décroissant
    for etudiant in etudiants:
        print(f"Nom: {etudiant['nom']}, Prénom: {etudiant['prenom']}, Téléphone: {etudiant['telephone']}, Classe: {etudiant['classe']}, Moyenne: {etudiant['moyenne']}")


# 🧭 Menu principal
if __name__ == "__main__":
    while True:
        print("\n📚 Menu Gestion Étudiants")
        print("1. Ajouter un étudiant")
        print("2. Afficher les étudiants")
        print("3. Rechercher un étudiant")
        print("4. Modifier les notes")
        print("5. Supprimer un étudiant")
        print("6. Trier par moyenne")
        print("0. Quitter")

        choix = input("Choix: ")
        if choix == "1":
            ajouter_etudiant_menu()
        elif choix == "2":
            afficher_etudiants()
        elif choix == "3":
            rechercher_etudiant()
        elif choix == "4":
            modifier_notes()
        elif choix == "5":
            supprimer_etudiant()
        elif choix == "6":
            trier_par_moyenne()
        elif choix == "0":
            break
        else:
            print("❌ Choix invalide.")
