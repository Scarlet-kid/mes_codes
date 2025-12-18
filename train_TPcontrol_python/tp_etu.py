from Tri_insertion import triInsertion

class Etudiant:
    def __init__(self,nom:str,prenom:str,date:int,moyenne:float,promo:int):
        self.nom = nom
        self.prenom = prenom
        self.date = date
        self.moyenne = moyenne
        self.promo = promo

    def __str__(self):
        return f"nom:{self.nom}, prenom: {self.prenom}, ne(e) en {self.date}, moyenne: {self.moyenne}, promo: {self.promo}"

def saisie_etu_info():
    nom = str(input("Le nom de l'étudiant:"))
    prenom = str(input("Le prénom de l'étudiant:"))
    date = int(input("La date de naissance de l'étudiant:"))
    moyenne = float(input("Saisir la moyenne de l'étudiant:"))
    promo = int(input("L'étudiant fait parti de quelle promo?:"))
    return Etudiant(nom,prenom,date,moyenne,promo)

def list_etudiant() -> list[Etudiant]:
        etu = int(input("Combien d'étudiant voulez vous ajouter premièrement:"))
        liste: list[Etudiant] = []
        for i in range(etu):
            print(f"étudiant numéros {i + 1}")
            liste.append(saisie_etu_info())  # on ajoute l'Etudiant directement
        return liste

def ajout_etudiant(liste: list[Etudiant]) -> list[Etudiant]:
        n = int(input("Combien d'étudiants voulez vous rajouter?:"))
        for i in range(n):
            print(f'Etudiant numéros {i + 1}')
            liste.append(saisie_etu_info())  # ✅ pareil ici
        return liste

def afficher_etudiant(lst: list[Etudiant]):

        for i in lst:
            print(i)

def recherche_etudiant(liste: list[Etudiant]) -> int:
        name = str(input("Saisir le nom de l'étudiant que vous souhaitez rechercher:"))
        for indice, etu in enumerate(liste):
            if etu.nom == name:
                return indice
        return -1  # seulement après la boucle

def supprimer_etudiant(lst: list[Etudiant]):
        indice = recherche_etudiant(lst)
        lst.pop(indice)  # le pop marche les indices.

def TrielstEtudiant(lst: list[Etudiant]) -> list[Etudiant]:
        # On crée une liste de tuples (moyenne, etudiant)
        couples = [(etu.moyenne, etu) for etu in lst]

        # On réutilise TON triInsertion sur cette liste
        triInsertion(couples)

        # On récupère la liste d'étudiants triés
        lst_tries = [etu for (_, etu) in couples]

        return lst_tries

def major_par_promotion(lst: list[Etudiant]) -> dict:

        majors: dict[int, Etudiant] = {}

        for etu in lst:
            promo = etu.promo

            # Si c'est le premier étudiant de cette promo, il est major pour l'instant
            if promo not in majors:
                majors[promo] = etu
            else:
                # Sinon on compare sa moyenne avec celle du major actuel
                if etu.moyenne > majors[promo].moyenne:
                    majors[promo] = etu

        return majors




if __name__ == "__main__":
    # print(saisie_etu_info())
    # print(list_etudiant())
    l1 = list_etudiant()
    print(afficher_etudiant(l1))
    print(ajout_etudiant(l1))
    # print(ajout_etudiant(l1))
    print(afficher_etudiant(l1))
    # print(recherche_etudiant(l1))
    # print(TrielstEtudiant(l1))
    
    majors = major_par_promotion(l1)
    for promo, etu in majors.items():
        print(f"Le major de la promotion {promo} est : {etu}")