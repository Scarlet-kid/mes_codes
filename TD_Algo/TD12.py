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

def calcul(nb1:float, nb2:float, operande:str)->float:
    result:int = 0

    if operande == "+":
        result = nb1+nb2
    elif operande == "-":
        result = nb1-nb2
    elif operande == "*":
        result = nb1*nb2
    elif operande == "/":
        result = nb1 / nb2
    else:
        raise Exception("Opération indisponible")
    
    return result

def calcul_pile(laPile):
    operande=depiler(laPile)
    nb2=depiler(laPile)
    nb1=depiler(laPile)
    return calcul(nb1,nb2,operande)

def calcul_pile2(laPile):
    nb2=depiler(laPile)
    nb1=depiler(laPile)
    operande=depiler(laPile)
    return calcul(nb1,nb2,operande)

def calcul_pile3(p):
    res=0
    while not estVide(p):
        res=calcul_pile2(p)
        if not estVide(p):
            empiler(p,res)
    return res

def prog():
    #print(calcul(5,7,"*"))
    
    calc=Pile()
    empiler(calc,'-')
    empiler(calc,4)
    empiler(calc,'+')
    empiler(calc,3)
    empiler(calc,6)
    print("6+3-4 =",calcul_pile3(calc))
    
    calc2=Pile()
    empiler(calc2,'-')
    empiler(calc2,10)
    empiler(calc2,'+')
    empiler(calc2,4)
    empiler(calc2,6)
    
    #print(calcul_pile(maPile))


if __name__ == "__main__":
    prog()