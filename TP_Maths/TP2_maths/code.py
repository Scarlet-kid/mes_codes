from teste import concatene

def affichage(matrice:list[list[int]])->list[int]:

    texte=""
    for ligne in matrice:
        for colonne in ligne:
            texte+=str(colonne) + " "
        texte+="\n"
    
    return texte 
        
#print(affichage([[1,2,3],[4,5,6],[7,8,9]]))

def pivot(A:list[list[int]],b:list[int],j:int):
    A=concatene(A,b)
    col_j=[]
    for ligne in range(j,len(A)):
        col_j.append(A[ligne][j])
    #return col_j
    max_col_j = max(col_j) # Le max de la colonne.
    index_max_col_j= col_j.index(max_col_j) # Index du max dans la liste des valeurs de la colonne
    l1=A[j]
    l_max=A[index_max_col_j]
    temp=None
    #Permutation
    temp=l1
    l1=l_max
    l_max=temp
    #Modification
    A[j]=l1
    A[index_max_col_j]=l_max
    return A


result=(pivot([[2,-3,1],[1,3,-2],[3,-1,-1]],[-1,1,-2],0))
#print(affichage(result))

def elimination_down(A, b, j):
    n = len(A)          # nombre de lignes
    m = len(A[0])       # nombre de colonnes

    pivot = A[j][j] # Le pivot

    for i in range(j + 1, n):          # pour chaque ligne sous le pivot
        facteur = A[i][j] / pivot

        # on modifie la ligne i de A
        for k in range(j, m):
            A[i][k] = A[i][k] - facteur * A[j][k] 
            

        # on modifie aussi b[i]
        b[i] = b[i] - facteur * b[j]

    #return concatene(A, b)

var=elimination_down([[2,-3,1],[1,3,-2],[3,-1,-1]],[-1,1,-2],0)
#print(affichage(var))

def descendre(A,b):
    for j in range(3):
        elimination_down(A,b,j)

    return affichage(concatene(A,b))

var2 = descendre([[2,-3,1],[1,3,-2],[3,-1,-1]],[-1,1,-2])
#print(affichage(var2))

def elimination_up(A, b, j):
    m = len(A[0])     # nombre de colonnes
    pivot = A[j][j]

    for i in range(j):     # lignes AU-DESSUS du pivot
        facteur = A[i][j] / pivot

        # on modifie toute la ligne i de A
        for k in range(m):
            A[i][k] = A[i][k] - facteur * A[j][k]

        # on modifie aussi b[i]
        b[i] = b[i] - facteur * b[j]

    #return concatene(A, b)

def remontee(A,b):
    for j in range(2,-1,-1):
        elimination_up(A,b,j)

    return affichage(concatene(A,b))


var3=elimination_up([[2,-3,1],[1,3,-2],[3,-1,-1]],[-1,1,-2],2)
#print(affichage(var3))
#print(affichage(remontee([[2,-3,1],[1,3,-2],[3,-1,-1]],[-1,1,-2])))

"""def resoudre_diagonale(A,b):

    for i in range(0,len(A)):
        if A[i][i]<=0:
            #A[i][i] = A[i][i]/-A[i][i]
            b[i]= -b[i]/A[i][i]
        elif A[i][i]<=0 and b[i]<=0:
            b[i] = -b[i] / -A[i][i]
        elif A[i][i]>=0 and b[i]>=0:
            #A[i][i] = A[i][i] / A[i][i]
            b[i] = b[i] / A[i][i]
            
    return b"""

def resoudre_diagonale(A, b):
    n = len(A)
    x = [0]*n
    for i in range(n):
        x[i] = b[i] / A[i][i]
    return x


var4=resoudre_diagonale([[2,0,0],[0,4,0],[0,0,5]],[-1,1,-2])
#print(var4)

def gauss(A,b):
    print(descendre(A,b))
    print(remontee(A,b))

    return resoudre_diagonale(A,b)

print(gauss([[2,-1,3],[1,1,-2],[5,-3,2]],[9,-3,5]))
