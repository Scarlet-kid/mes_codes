class Etudiant:
    def __init__(self, nom: str, prenom: str, date: int, moyenne: float, promo: int):
        self.nom = nom
        self.prenom = prenom
        self.date = date
        self.moyenne = moyenne
        self.promo = promo

    def __str__(self):
        return f"{self.nom} {self.prenom}, né(e) en {self.date}, moyenne: {self.moyenne}, promo: {self.promo}"

def saisie_etu_info() -> Etudiant:
    nom = input("Le nom de l'étudiant: ")
    prenom = input("Le prénom de l'étudiant: ")
    date = int(input("La date de naissance de l'étudiant: "))
    moyenne = float(input("Saisir la moyenne de l'étudiant: "))
    promo = int(input("L'étudiant fait partie de quelle promo?: "))
    etudiant_cree = Etudiant(nom, prenom, date, moyenne, promo)
    return etudiant_cree

def list_etudiant() -> list:
    liste = []
    liste.append(saisie_etu_info())
    return liste

def ajout_etudiant(liste: list) -> list:
    n = int(input("Combien d'étudiants voulez-vous ajouter ?: "))
    for i in range(n):
        print(f"--- Étudiant numéro {i + 1} ---")
        liste.append(saisie_etu_info())
    return liste

def recherche_etudiant(liste: list, nom_recherche: str) -> int:
    """
    Recherche un étudiant par son nom et retourne son indice dans la liste.
    Si l'étudiant n'est pas trouvé, retourne -1.
    """
    for indice, etu in enumerate(liste):
        if etu.nom.lower() == nom_recherche.lower():
            return indice
    return -1

def main():
    liste = list_etudiant()
    ajout_etudiant(liste)

    nom_rech = input("Saisir le nom de l'étudiant que vous souhaitez rechercher: ")
    indice = recherche_etudiant(liste, nom_rech)

    if indice != -1:
        print(f"L'étudiant {liste[indice]} se trouve à l'indice {indice} dans la liste.")
    else:
        print("L'étudiant n'est pas présent dans la liste.")

if __name__ == "__main__":
    main()
