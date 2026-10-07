
from trie import*
class Etudiant:
    def __init__(self,nom, prenom, naissance,moyenne,promo):
        self.nom = nom
        self.prenom = prenom
        self.naissance = naissance
        self.moyenne = moyenne
        self.promo = promo

    def __str__(self):
        return f'nom:{self.nom}, prenom:{self.prenom}, naissance:{self.naissance}, moyenne:{self.moyenne}, promo:{self.promo}'

def saisie_etu_info():
    nom = str(input('le nom de l\' etudiant:'))
    prenom = str(input('le prenom de l\' etudiant:'))
    naissance = str(input('la date de naissance de l\' etudiant:'))
    moyenne = float(input('le nom de l\' etudiant:'))
    promo = int(input("La promo de l'étudiant:"))
    return Etudiant(nom, prenom, naissance, moyenne, promo)

def liste_Etudiant():
    nb = int(input('Combien d\'étudiant voulez vous ajouter?:'))
    maListe = []
    for i in range(nb):
        print(f"Etudiant numéros {i+1}")
        maListe.append(saisie_etu_info())

def affichage(lst:list[Etudiant]):
    for etu in lst:
        print(etu)

def ajout(lst:list[Etudiant]):
    nb = int(input("Combien d'étudiant voulez-vous rajouter :"))
    for i in range(nb):
        print(f"Etudiant numéros {i+1}")
        lst.append(saisie_etu_info())

def recherche(lst:list[Etudiant]):
    name = str(input("Le nom de l'étudiant que vous cherchez:"))
    for indice,etu in enumerate(lst,start=0):
        if etu.nom == name:
            return indice
    
    return -1

def retrait(lst:list[Etudiant]):
    etu = str(input("le nom de l'étudiant a supprimer:"))
    for indice,etudiant in enumerate(lst,start=0):
        if etudiant.nom == etu:
            lst.pop(indice)
            print(f'Etudiant {etu} supprimé avec succès')
    return -1


def triInsertionEtudiants(lst: list) -> None:
    for i in range(1, len(lst)):
        tmp = lst[i]          # tmp est un ETUDIANT
        j = i
        while j > 0 and lst[j-1].moyenne > tmp.moyenne:   # comparaison sur la moyenne
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = tmp

def trie(lst:list[Etudiant]):
    # On cree un couple etudiant-moyenne dans une liste:
    couple = [(etu.moyenne,etu) for etu in lst]

    triInsertion(couple)

    lst_trie = [etu for (_, etu) in couple]

    return lst_trie

def major_par_promotion(lst:list[Etudiant]):
    majors : dict[int, Etudiant] = {}

    for etu in lst:
        promo = etu.promo

        if promo not in majors:
            majors[promo] = etu

        else:
            if etu.moyenne > majors[promo].moyenne:
                majors[promo] = etu

    return majors