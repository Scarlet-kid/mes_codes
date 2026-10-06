class Element:
    def __init__(self,v,s=None):
        self.valeur = v
        self.suivant = s
class Liste:
    def __init__(self):
        self.tete = None
        self.nb = 0
        
def setValeur(elt:Element, v):
    elt.valeur = v
    
def setSuivant(elt:Element, succ:Element):
    elt.suivant = succ
    
def ajouterValeur(lst:Liste,v)->Liste:
    lst.nb = lst.nb+1
    if lst.tete == None:
        lst.tete=Element(v)
        return lst   
    elt = lst.tete   
    while elt.suivant!=None:
        elt = elt.suivant
    nouv = Element(v)
    elt.suivant = nouv
    return lst

def afficherListe(lst:Liste):
    print("[ ",end="")
    elt = lst.tete
    while elt!=None :
        print(elt.valeur,end="")
        elt = elt.suivant
        if(elt!=None):
            print(", ",end="")
    print("]")
    
def longueurListe(lst:Liste)->int:
    return lst.nb

def getAt(lst:Liste,n:int):
    if(n>lst.nb) or n<1:
        return None
    cpt = 1
    elt = lst.tete
    while cpt<n:
        elt = elt.suivant
        cpt = cpt + 1
    return elt.valeur

def delAt(lst:Liste,n:int):
    if(n>lst.nb) or n<1:
        return None
    lst.nb = lst.nb - 1
    if n==1:
        val=lst.tete.valeur
        lst.tete = lst.tete.suivant
        return val
    cpt = 1
    elt = lst.tete
    while cpt<n-1:
        elt = elt.suivant
        cpt = cpt + 1
    val = elt.suivant.valeur
    suiv = elt.suivant.suivant
    elt.suivant = suiv
    return val