def defile(lst:list[int])->list[int]:
    if(len(lst) == 0):
        return []
    return lst.pop(0)

def enfile(n:int, lst:list[int])->list[int]:
    lst.append(n)
    return lst

def pel(L:list[int], start:int):
    long = len(L)
    visites = [False] * long
    couche = [-1] * long

    parcours = []
    file = []

    enfile(start, file)
    visites[start] = True
    couche[start] = 0

    while len(file)>0:
        sommet = defile(file)
        parcours.append(sommet)

        for voisins in L[sommet]:
            if not visites[voisins]:
                visites[voisins] = True
                couche[voisins] = couche[sommet] + 1
                enfile(voisins,file)

    return parcours, couche

def connexe(L:list[int])->bool:
    if not L: return True
    parcours,_ = pel(L)
    return len(parcours) == len(L)

def composantesConnexes(L:list[int])->int:
    n = len(L)
    visites = [False] * n
    composantes = []
    for i in range(n):
        if not visites[i]:
            comp,_ = pel(L,i)
        for sommet in comp:
            visites[sommet] = True
        composantes.append(comp)
    
    return composantes

def successeur(L:list[list[int]], n:int)->list[int]:
    return L[n]

def biparti(L:list[list[int]])->bool:
    n = len(L)
    couleur = [-1] * n
    for i in range(n):
        if(couleur[i] == -1):
            file = [i]
            couleur[i] = 0

            while file:
                

def main():
    #print(defile([1,2,3,4,5]))
    #print(enfile(6,[1,2,3,4,5]))
    L = [[1,4,6],[2,4],[1],[0,7,9],[3,5],[6,8],[2,7],[8],[2,3],[1]]
    print(pel(L,0))


if __name__ == "__main__":
    main()