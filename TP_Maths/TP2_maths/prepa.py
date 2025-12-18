from teste import concatene, affichage2

def affichage(mat:list[list[int]]):
    
    var=""
    for ligne in mat:
        for colonne in ligne:
            var+=str(colonne) + ' '
        var+='\n'
    
    print(var)

def pivot(A:list[list[int]],b:list[int],j:int):
    #Concatenons le A et le b pour faciliter les calculs et economiser de l'espace mémoire:
    A = concatene(A,b)
    # Focalisation sur la colonne j
    maListe_de_j = []
    for i in range(j,len(A)):
        maListe_de_j.append(A[i][j])
    # maListe_de_j contient maintenant tous les élements de la colonne j
    # le max de cette liste
    MaxmaListedeJ = max(maListe_de_j)
    # Cherchons son indice dans A:
    indiceDumax = maListe_de_j.index(MaxmaListedeJ)
    # Début du switch:
        # Initialisation
    ligneduJ = A[j]
    ligneduMax = A[indiceDumax]
    temp = None
        #Le swichage en uestion
    temp = ligneduJ
    ligneduJ = ligneduMax
    ligneduMax = temp
        # Le réaffectation
    A[j] = ligneduJ
    A [indiceDumax] = ligneduMax
    
    return A

def elimination_down(A,b,j=0):
    n = len(A)
    m = len(A[0])
    
    pivot = A[j][j]
    
    for i in range(j+1, n):
        facteur = A[i][j] / pivot
        
        # On modifie la ligne i de A
        for k in range(j,m): # Modification de toutes les colonnes de la ligne:
            A[i][k] = A[i][k] - facteur * A[j][k] #Opération prioritaire:python sait faire ca. Badass python.
            
        b[i] = b[i] - facteur * b[j]
    
    return concatene(A,b)

def descendre(A,b):
    for j in range(len(A)-1):
        elimination_down(A,b,j)
    
    return concatene(A,b)

def elimination_up(A,b,j=2):
    n = len(A[0])
    pivot = A[j][j]
    
    # Recherche du facteur
    for i in range(j-1, -1, -1):
        facteur = A[i][j] / pivot
        
        for k in range(j,n):
            A[i][k] = A[i][k] - facteur * A[j][k]
            
        b[i] = b[i] - facteur * b[j]
        
    return concatene(A,b)

def remontee(A,b):
    for j in range(len(A)-1,-1,-1):
        elimination_up(A,b,j)
        
    return concatene(A,b)

def resoudre_diagonale(A,b):
    for i in range(len(A)):
        b[i] = b[i] / A[i][i]
    
    return affichage2(b)

def gauss(A,b):
    affichage(descendre(A,b))
    affichage(remontee(A,b))
    print(resoudre_diagonale(A,b))

if __name__=='__main__':
    #affichage([[1,2,3],[4,5,6],[7,8,9]])
    #print(affichage(pivot([[2,-3,1],[1,3,-2],[3,-1,-1]],[-1,1,-2],0)))
    #affichage(elimination_down([[2,-3,1],[1,3,-2],[3,-1,-1]],[-1,1,-2],0))
    #affichage(descendre([[2,-3,1],[1,3,-2],[3,-1,-1]],[-1,1,-2]))
    #affichage(elimination_up([[2,-3,1],[1,3,-2],[3,-1,-1]],[-1,1,-2],2))
    #affichage(remontee([[2,-3,1],[1,3,-2],[3,-1,-1]],[-1,1,-2]))
    #print(resoudre_diagonale([[2,0,0],[0,4,0],[0,0,5]],[-1,1,-2]))
    print(gauss([[2,-1,3],[1,1,-2],[5,-3,2]],[9,-3,5]))