def premiereValeur(liste : list, indice : int) -> None :
    for i in range(len(liste)) :
        if liste[i] == indice :
            return i 
    return -1


def premiereValeurV2(liste : list, indice : float) -> None :
    trouve :bool = False
    fini : bool = False
    i : int= 0
    while (not fini) :
        if (liste[i] == indice) :
            trouve = True
            fini = True
        else :
            i +=1
            if (i == len(liste)) :
                fini = True
    if (trouve) :
        return i
    else :
        return -1
    
def inSorted(liste : list, indice : int) -> int :
    trouve :bool = False
    fini : bool = False
    i : int= 0
    while (not fini) :
        if (liste[i] == indice) :
            trouve = True
            fini = True
        elif (liste[i] > indice):
            fini = True
        else :
            i +=1
            if (i == len(liste)) :
                fini = True
    if (trouve) :
        return i
    else :
        return -1
        
def dichotomie(lst : list, v : int) -> int :
    deb : int = 0
    fin : int = len(lst)-1
    fini : bool = False
    ind : int = -1
    while not fini :
        m = (deb + fin) // 2
        if lst[m] == v :
            fini = True
            ind = m
        elif fin <= deb :
            fini = True
        elif lst[m] < v :
            deb = m + 1
        else : 
            fin = m - 1
    return ind

def testerDichotomie() :
    lst = [2,6,9,12,14,15,17,27,31,43,51,62,75,88,89,91,98]
    if dichotomie(lst,1) != -1 :
        print('test 0 failed')
    else :
        print('test 1 OK')


                  
if __name__ == "__main__" :
    testerDichotomie()