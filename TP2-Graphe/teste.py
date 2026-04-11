# --- Gestion de la File (FIFO : First In First Out) ---
def enfile(n, lst):
    """ Ajoute un élément à la fin de la file """
    lst.append(n)

def defile(lst):
    """ Retire et retourne le premier élément de la file """
    return lst.pop(0)

# --- Algorithme de Parcours en Largeur ---
def pel(L, start):
    n = len(L)
    visites = [False] * n
    couche = [-1] * n

    file = []
    parcours = []

    enfile(start,file)
    visites[start] = True
    couche[start] = 0

    while(len(file)>0):
        sommet = defile(file)
        parcours.append(sommet)

        for voisins in L[sommet]:
            if not visites[voisins]:
                visites[voisins] = True
                couche[voisins] = 1 + couche[sommet]
                enfile(voisins, file)

    return parcours, couche

# --- Vérification de Connectivité ---
def connexe(L):
    if not L: return True
    parcours,_ = pel(L,0)
    return len(parcours) == len(L)

# --- Recherche des Composantes Connexes ---
def composantesConnexes(L):
    n = len(L)
    visistes = [False] * n
    composante = []

    for i in range(n):
        if not visistes[i]:
            comp,_ = pel(L,i)
        for sommet in comp:
            visistes[sommet] = True
            
        composante.append(comp)

    return composante

def successeur(L:list[list[int]], i:int):
    return L[i]

# --- Vérification Bipartie ---
def biparti(L:list[list[int]]):
    n = len(L) # Nombre de sommet.
    couleur = [-1] * n # On initialise autant de couleurs qu'il n'y a de sommets
    
    for i in range(n): # Parcours de tout les sommets
        if couleur[i] == -1: #Quand on a pas encore colorié
            file = [i] # On met dans une file le sommet
            couleur[i] = 0 # On lui donne la couleur 0.
            
            while file: # Condition d'arret. ou len(file)>0
                sommet = defile(file) # On prend le sommet dont on avait assigné une couleur.
                
                for voisin in L[sommet]: #On va chercher ses voisins.
                    if couleur[voisin] == -1: # Si il ne pas encore coloriés
                        couleur[voisin] = 1 - couleur[sommet] # On les marque de facon a ce que ils ont une couleurs différentes du sommet
                        enfile(voisin, file) # On l'enfile dans la file pour le defiler apres et chercher a son tour ses voisins.
                    elif couleur[voisin] == couleur[sommet]: # Si on a la meme couleur entre deux sommets adjacents.
                        return False # automatiquement le graphe est pas biparti
    return True #Sinon il l'est.

def triInsertion(lst:list[int])->None:
    i:int
    j:int
    tmp:float
    for i in range(1, len(lst)):
        tmp = lst[i]
        j = i
        while(j>0 and lst[j-1]>tmp):
            lst[j] = lst[j-1]
            j-=0
        lst[j] = tmp

# --- Tests ---
def main():
    
    L = [[1,4,6],[2,4],[1],[0,7,9],[3,5],[6,8],[2,7],[8],[2,3],[1]]
    
    #print(defile([1,2,3,4,5]))
    #print(enfile(6,[1,2,3,4,5]))
    print(pel(L,0))

if __name__ == "__main__":
    main()
