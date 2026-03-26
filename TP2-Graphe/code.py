def defile(lst):
    if len(lst) == 0:
        return []
    return lst.pop(0) #Enleve et supprime le dernier element.

def enfile(n, lst):
    lst.append(n) 
    return lst #Cest cest bon !

        
def pel(L:list[list[int]], start:int):
    n = len(L)
    visites = [False] * n #init : on na encore rien visité(pour ne pas repasser par un sommet deja exploré)
    couches = [-1] * n #init : pas encore de couche (distance a partir du depart par rapport a un sommet deja visté courant)
    
    file = [] # file structure de donnée first in first out parcours en lageur géré par les files.
    parcours = [] # resultat final.
    
    enfile(start, file) #On enfile le premier noeud correspondant au noeud ou on commence.toujours le premier a enfiler
    visites[start] = True #On na deja visité ce noeud
    couches[start] = 0 # la distance du commencement est a 0 voila pourquoi l'int
    
    while file: #Vrai tant qu'il reste des sommets a explorer.
        sommet = defile(file) #On prend le premier sommet commencement
        parcours.append(sommet) #On le met dans la liste du resultat final.
        
        for voisin in L[sommet]: #On visite les voisins du premier sommet visité
            if not visites[voisin]: #Si on a pas encore visité ce voisin
                visites[voisin] = True #On le marque comme étant visité.
                couches[voisin] = couches[sommet] + 1 #On calcule la distance.
                enfile(voisin, file) #On l'ajoute a la file
    
    return parcours, couches #On retourne la liste du parcours et des couches.

""" Graphe connexe"""
def connexe(graphe:list[list[int]])->bool:
    ParcoursEnLargeur = pel(graphe,0)[0]
    return len(ParcoursEnLargeur) == len(graphe)


def composantesConnexes(L):
    n = len(L) #nombre de sommet.
    visites = [False] * n #Pour eviter de faire le meme parcours 
    composantes = [] #La liste finale des composantes 
    
    for i in range(n): # On doit parcouri tous les sommets
        if not visites[i]: #Si on na pas visité ce sommet implique qu'il appatient a une nouvelle composante.
            comp = pel(L, i)[0] #Une composante connexe a partir d'un sommet.
            
            for sommet in comp: #On parcours les sommets de la composante.
                visites[sommet] = True #On marque les sommets de la composante pour ne plus les parcourir apres.
            
            composantes.append(comp) #On stocke la composante dans notre liste de composante.
    
    return composantes #On retourne

def biparti(L):
    n = len(L)
    couleur = [-1] * n  # -1 = non colorié
    
    for i in range(n):
        if couleur[i] == -1:
            file = [i]
            couleur[i] = 0
            
            while file:
                sommet = defile(file)
                
                for voisin in L[sommet]:
                    if couleur[voisin] == -1:
                        couleur[voisin] = 1 - couleur[sommet]
                        enfile(voisin, file)
                    elif couleur[voisin] == couleur[sommet]:
                        return False
    return True

def main():
    maListe = [1,2,3]
    #print(defile(maListe))
    #print(enfile(6,maListe))
    L = [[1,4,6],[2,4],[1],[0,7,9],[3,5],[6,8],[2,7],[8],[2,3],[1]]
    print(pel(L,0))
    print(connexe(L))

if __name__ == "__main__":
    main()