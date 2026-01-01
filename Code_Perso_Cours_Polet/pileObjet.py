class Element:
    def __init__(self, v, s=None):
        self.valeur = v
        self.suivant = s

class Pile:
    def __init__(self, cap = 10):
        self.tete = None
        self.nb = 0
        self.capacite = cap

def estPleine(p:Pile):
    return p.nb == p.capacite

def estVide(p:Pile):
    return p.nb == 0

def empiler(p:Pile, v):
    if estPleine(p):
        raise Exception("Pile pleine")
    else:
        p.tete = Element(v, p.tete)
        p.nb = p.nb + 1

def deplier(p:Pile):
    if estVide(p):
        raise Exception("Pile vide")
    else:
        v = p.tete.valeur
        p.tete = p.tete.suivant
        p.nb = p.nb - 1
        return v

def affiherPile(p:Pile):
    print("[ ",end="")
    elt = p.tete
    while elt != None :
        print(elt.valeur,end="")
        elt = elt.suivant
        if elt != None:
            print(", ",end="")
    print("]")

maPile = Pile(10)
empiler(maPile,1)
empiler(maPile,2)
empiler(maPile,3)
affiherPile(maPile)
valeur = deplier(maPile)
print("valeur = ",valeur, "maPile =")
affiherPile(maPile)

# Gestion des files:
def enfiler(f:list, v ):
    f.append(v)

def defiler(f:list):
    return f.pop(0)

def estVide(f:list):
    return len(f) == 0

maFile =[]
enfiler(maFile,1)
enfiler(maFile,2)
enfiler(maFile,3)
print(maFile)
valeur=defiler(maFile)
print("valeur = ",valeur, "maFile =", maFile)