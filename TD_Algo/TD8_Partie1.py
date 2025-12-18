import random

def createMatrix2(n,m):
    mat=[]
    for i in range(n):
        mat.append([])
        for j in range(m):
            mat[i].append(random.randint(0,5))
    return mat

def est_Present(matrixe,elt):
    compt=0
    ok = True
    for ligne in range (len(matrixe)):
        for colonne in range (len(matrixe)):
            if matrixe[ligne][colonne] == elt:
                compt+=1
    return compt

def Somme_Matrix(m1,m2):
    m3 = createMatrix2(len(m1),len(m1[0]))
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m3[i][j] = m1[i][j] + m2[i][j]
    return m3


def Scalaire_Matrix(a,matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = a*matrix[i][j]
    return matrix

def calculerCase(i,a,b):
    somme=0
    for k in range(len(b)):
        pass
        #somme+=a[i][k]*b[k][j]
    #return somme

def produit_matrix(a,b):
    nbl=len(a)
    nbc=len(b[0])
    c=createMatrix2(nbl,nbc)
    for i in range(nbl):
        for j in range(nbc):
            c[i][j]=calculerCase(i,a,b)
    return c
  
def transpose(m1):
    pass

        
if __name__ == "__main__":
   mat1 = createMatrix2(2,3)
   mat2 = createMatrix2(2,3)
   print(mat1)
   print(mat2)
   print(Somme_Matrix(mat1,mat2))
   print(Scalaire_Matrix(4,mat2))