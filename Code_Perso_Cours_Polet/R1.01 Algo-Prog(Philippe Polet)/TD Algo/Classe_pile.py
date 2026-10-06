class Element:
    def __init__(self,v,s=None):
        self.valeur = v
        self.suivant = s


class Pile:
    def __init__(self, cap=10):
        self.tete = None
        self.nb = 0
        self.capacite = cap
        
def estPleine(p:Pile)->bool:
    return p.nb==p.capacite

def estVide(p:Pile)->bool:
    return p.nb==0

def empiler(p:Pile, v):
    if estPleine(p):
        raise Exception("Pile pleine")
    else:
        p.tete=Element(v,p.tete)
        p.nb= p.nb+1
        
def depiler(p:Pile):
    if estVide(p):
        raise Exception("Pile vide")
    else:
        v = p.tete.valeur
        p.tete = p.tete.suivant
        p.nb = p.nb-1
        return v
        
def afficherPile(p:Pile):
    print("[ ",end="")
    elt = p.tete
    while elt!=None :
        print(elt.valeur,end="")
        elt = elt.suivant
        if(elt!=None):
            print(", ",end="")
    print("]")
    
maPile = Pile(2)
try :
    empiler(maPile,1)
    empiler(maPile,2)
    empiler(maPile,3)
except Exception as probleme :
    print("il y a eut un probleme:")

afficherPile(maPile)
valeur=depiler(maPile)   
print("valeur = ",valeur, "mapile =")
afficherPile(maPile)
