def long(lst:list[float])->int:
    res = 0
    for _ in lst:
        res += 1
    return res

def somme(lst:list[float])->float:
    res = 0
    for i in lst:
        res += i
    return res

def mini(lst:list[float])->float:
    Mymin = lst[0]
    for i in lst:
        if i <= Mymin:
            Mymin = i
    return Mymin

def maxi(lst:list[float])->float:
    Mymax = lst[0]
    for i in lst:
        if i >= Mymax:
            Mymax = i
    return Mymax

def moyenne(lst:list[float])->float:
    return somme(lst)/long(lst)

def variance(lst:list[float])->float:
    sommelstCarrée = somme([i**2 for i in lst])
    return (sommelstCarrée/long) - moyenne(lst)

def ecart(lst:list[float])->float:
    return variance(lst)**0.5

def tri_bulle(lst:list[float])->float:
    for i in range(long(lst)-1):
        if lst[i]>lst[i+1]: # SI ce qu'il y'a avant est plus grand que ce qu'il ya apres
            tmp = lst[i] # On met dans une variable le plus grand par défaut 
            lst[i] = lst[i+1] # On écrase ce qu'il ya avant avec le plus petit
            lst[i+1] = tmp # Et ce qu'il ya apres prend la plus grande valeur pour que le cycle continue.
    return lst

#print(tri_bulle([12,4,5,7,9,9]))

def mediane(lst:list[float])->float:
    lstLongueur = long(lst)
    lstTrié = tri_bulle(lst)
    if lstLongueur%2 == 0:
        val1 = lstTrié[(lstLongueur//2)-1]
        val2 =  lstTrié[(lstLongueur//2)]
        return (val1+val2)/2
    else:
        return lstTrié[(lstLongueur//2)]

def quartile(lst:list[float])->tuple:
    q2 = mediane(lst)
    lstLongueur = long(lst)
    l1 = lst[0:lstLongueur//2]
    q1 = mediane(l1)
    l2 = lst[(lstLongueur//2)+1::]
    q3 = mediane(l2)
    return q1,q2,q3

def moustache(lst:list[float]):
    pass


    