def createMatrix(nl:int=10,nc:int=10)->list[list[int]]:
    m:list[list[int]] = list()
    for i in range(nl):
        m.append(list())
        for j in range(nc):
            m[i].append(0)
    return m

def initCB()->list[list[int]]:
    cb:list[list[int]] = createMatrix()
    
    for i in range(4):
        for j in range(0,10,2):
            cb[i][j+(i+1)%2] = 2
            cb[i+6][j+(i+1)%2] = 1
    return cb




def isBlack(row: int,col: int)->bool:
    return (row+col)%2!=0

def printCB(cb:list[list[int]])->None:
    print("  ",end="")
    for j in range(10):
        print(j,end=" ")
    print()
    for i in range(10):
        print(" -"+"--"*10)
        print(chr(ord('A')+i),end="")
        for j in range(10):
            if cb[i][j]==0:
                c = ' '
            elif cb[i][j]==1:
                c = 'B'
            else:
                c = 'N'
            print("|"+c,end="")
        print("|")
    print(" -"+"--"*10)

def valide(damier,tup1,tup2):
    for i in range(tup1[0]-1,tup1[0]+1):
        for j in range(tup1[1]-1,tup1[1]+1):
            if damier[i][j] == " ":
                return True

if __name__ == "__main__":
    Mon_jeu = initCB()
    printCB(Mon_jeu)
