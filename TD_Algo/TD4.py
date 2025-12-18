def iteratif(x : int, n : int)-> int :
    res = 1
    for i in range(1,n+1,1) :
        res = res * x
    return res

def recursif(x : int, n : int)-> int :
    if n == 0 :
        return 1
    else :
        return x * recursif(x,n-1)

def puissRecV2(x : float, n : float) -> float :
    if n == 0 :
        return 1
    m : float= n//2
    res : float = puissRecV2(x,m)
    if n%2 == 0 :
        return res * res
    else :
        return x * res * res


def estPremierIter(n : int) -> bool :
    diviseur : int = 2
    trouver : bool = False
    if n < 2 :
        return False
    while not trouver and diviseur < n :
        if n % diviseur == 0 :
            trouver = True
        else :
            diviseur +=1
    return not trouver



if __name__ == "__main__" :
    print(estPremierIter(22091))