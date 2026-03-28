def matTolist(lst:list[list]):
    maList = []
    for i in range (len(lst)):
        for j in range(len(lst)):
            if(lst[i][j] == 1):
                maList.append(j+1)
        print(f"{i+1} = {maList}")
        maList.clear()

"""print(matTolist([[1,0,1,0,1,1],
                 [1,1,1,0,0,0],
                 [1,0,0,0,1,1],
                 [0,1,0,1,0,0],
                 [1,1,0,0,0,1],
                 [1,0,1,1,1,0]]))"""

def degre(lst:list[list])->list:
    maList = []
    cpt = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if(lst[i][j] == 1):
                cpt += 1
        maList.append(cpt)
        cpt = 0
    return maList

"""print(degre([[1,0,1,0,1,1],
             [1,1,1,0,0,0],
             [1,0,0,0,1,1],
             [0,1,0,1,0,0],
             [1,1,0,0,0,1],
             [1,0,1,1,1,0]]))"""

mat = [      [1,0,1,0,1,1],
             [1,1,1,0,0,0],
             [1,0,0,0,1,1],
             [0,1,0,1,0,0],
             [1,1,0,0,0,1],
             [1,0,1,1,1,0]
    ]

D = {
    
    1:[1,3,5,6],
    2:[1,2,3],
    3:[1,5,6],
    4:[2,4],
    5:[1,2,6],
    6:[1,3,4,5]
    
}
print(len(D))


def listToMat(D:dict):
    mat = []
    for i in range(len(D)):
        pass # Completer renvoyer la matrice d'adjacence a partir de la lst d'adjacence modelisé a partir des dictionnaires.


A = [2,3,4,5,1,6,1,4,5,1,3,5,6,1,3,4,6,4,5,2] 
B = [1,5,7,10,18,21]
def listToMat(A:list,B:list):
    mat = [[0 for i in range(len(B-1))]for i in range(len(B-1))]
    pass
