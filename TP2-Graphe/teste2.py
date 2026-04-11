def degreMatrice(M, i):
    degre = 0
    for j in range(len(M[i])):
        if M[i][j] == 1:
            degre += 1
    return degre

def degreSommets(M):
    res = []
    for i in range(len(M)):
        deg = degreMatrice(M, i)
        res.append([deg, i])
    return res

def triInsertion(lst:list):
    tmp:float
    i:int
    j:int
    for i in range(1,len(lst)):
        tmp=lst[i]
        j=i
        while j<0 and lst[j-1]<tmp:
            lst[j]=lst[j-1]
            j=j-1
        lst[j] = tmp 

def trisommetsDegresDecroissant(M):
    liste = degreSommets(M)
    triInsertion(liste)
    return liste

def mult(a, b):
    if(len(a) == len(b)):
        return [a[i] * b[i] for i in range(len(a))]
    return []

def voisins(M, i):
    return M[i]

def number(L):
    i = 1
    while i in L: #tant que i est dans l alors ca s'incremente. donc techniquement ca s'arrete quand il trouve un truc qui ya pas dedans
        i += 1
    return i

def numbering(M):
    n = len(M)
    res = [0] * n
    
    for i in range(n):
        voisins = []
        for j in range(n):
            if M[i][j] == 1:
                voisins.append(res[j])
        res[i] = number(voisins)
    return res


 
def main():
    L = [[1,1,1],[0,0,0],[0,1,1],[0,1,0]]
    print(degreMatrice(L, 1))
    print(degreSommets(L))
    print(trisommetsDegresDecroissant(L))
    a = [1,5,3,5]
    b = [4,2,3]
    print(mult(a, b))
    print(number(a))
    print(numbering(L))

if __name__ == "__main__":
    main()