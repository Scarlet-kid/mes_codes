from random import randint

def estSimple(mat:list[list])->bool:
    simple = True
    for i in range(len(mat)):
        if mat[i][i] != 0:
            simple = False
    return simple

def estCarree(mat:list[list])->bool:
    l1 = len(mat[0])
    cpt = 0
    for i in l1:
        cpt += 1
    return l1 == cpt


def afficher(mat:list[list])->list[list]:
    for i in mat:
        print(i)
    

def matSym(n):
    M = [[0]*n for i in range(n)]
    
    for i in range(n):
        for j in range(i+1, n):
            x = randint(0,1)
            M[i][j] = x
            M[j][i] = x
            
    return afficher(M)

def sym(mat:list[list])->bool:
    sym = True
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] != mat[j][i]:
                sym = False
    return sym

def diago(mat:list[list])->list:
    Mat = []
    for i in range(len(mat)):
        Mat.append(mat[i][i])
    return Mat

def mult(m1:list, m2:list)->list:
    ma = []
    if len(m1) == len(m2):
        for i in range(len(m1)):
            ma.append(m1[i]*m2[i])
    return ma

def voisins(a:list[list],i:int)->list:
    return a[i].copy()
    

def color(lst:list)->int:
    Max = max(lst)
    for i in range(len(lst)):
        if(lst[i]<Max):
            Max = lst[i]
    res =  Max
    for k in lst:
        if k==res:
            res+=1
    return res

def color2(lst:list)->int:
    Min = min(lst)
    for k in lst:
        if k == Min:
            Min += 1
    return Min

def naif(M):
    n = len(M)
    couleurs = [0]*n
    
    for i in range(n):
        v = voisins(M,i)
        voisins_couleurs = mult(v,couleurs)
        couleurs[i] = color(voisins_couleurs)
        
    return couleurs

def main():
    #a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    #m = [[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
    #print(matSym(3))
    #print(sym(m))
    #print(diago(a))
    #a=[1,2,3]
    #b=[4,5,6]
    #print(mult(a,b))
    #a=[0, 0, 1, 4, 5, 0, 3]
    #b=[1, 2, 3, 4, 5, 6]
    #print(color2(b))
    print(color2([1,5,3,5]))
    a=[[0, 1, 1, 1, 0,0], [1, 0, 0, 1, 0,0], [1, 0, 0, 1, 0,0], [1, 1, 1, 0, 1,1], [0, 0, 0, 1, 0,1],[0,0,0,1,1,0]]
    #print(naif(a))
    

if __name__ == "__main__":
    main()