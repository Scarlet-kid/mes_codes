# La classe Element
class Element:
    def __init__(self, v):
        self.valeur = v
        self.suivant = None


# La classe Liste
class Liste:
    def __init__(self):
        self.tete = None
        self.nb = 0


def setValeur(elt: Element, v):
    elt.valeur = v


def setSuivant(elt: Element, succ: Element):
    elt.suivant = succ


def afficherListe(lst: Liste):
    print("[ ", end="")
    elt = lst.tete
    while elt != None:
        print(elt.valeur, end="")
        elt = elt.suivant
        if (elt != None):
            print(", ", end="")
    print("]")


def ajouterValeur(lst: Liste, v) -> Liste:
    lst.nb = lst.nb + 1
    if lst.tete == None:
        lst.tete = Element(v)
        return lst

    elt = lst.tete

    while elt.suivant != None:
        elt = elt.suivant
    nouv = Element(v)
    elt.suivant = nouv
    return lst


def getAt(lst: Liste, n: int):
    if (n > lst.nb) or n < 1:
        return None

    cpt = 1
    elt = lst.tete
    while cpt < n:
        elt = elt.suivant
        cpt = cpt + 1
    return elt.valeur


def delAt(lst: Liste, n: int):
    if (n > lst.nb) or n < 1:
        return None
    lst.nb = lst.nb - 1
    if n == 1:
        val = lst.tete.valeur
        lst.tete = lst.tete.suivant
        return val
    cpt = 1
    elt = lst.tete
    while cpt < n - 1:
        elt = elt.suivant
        cpt += 1
    val = elt.suivant.valeur
    suiv = elt.suivant.suivant
    elt.suivant = suiv
    return val


def prog():
    maListe = Liste()
    ajouterValeur(maListe,5)
    ajouterValeur(maListe,4)
    ajouterValeur(maListe,6)
    afficherListe(maListe)
    print(getAt(maListe,1))
    valeur = delAt(maListe,1)
    print("valeur supprimée:",valeur,"la liste :")
    afficherListe(maListe )

if __name__ == '__main__':
    prog()
