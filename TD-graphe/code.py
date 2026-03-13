def matTolist(lst:list[list]):
    maList = []
    for i in range (len(lst)):
        for j in range(len(lst)):
            if(lst[i][j] == 1):
                maList.append(j+1)
        print(f"{i+1} = {maList}")
        maList.clear()

print(matTolist([[1,0,1,0,1,1],
                 [1,1,1,0,0,0],
                 [1,0,0,0,1,1],
                 [0,1,0,1,0,0],
                 [1,1,0,0,0,1],
                 [1,0,1,1,1,0]]))

def matTolist2(lst:list[list]):
    B = [[j for j in range(len(lst)) if lst[i][j] != 0 for i in range(len(lst))]]
    liste = {}
    for k in range(len(B)):
        liste[k] = [i for i in B[k]]
    return liste


def hauteur(lst:list[list]):
    pass

