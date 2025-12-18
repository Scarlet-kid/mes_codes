from random import random,randint
"""def Val_Moyenne(lst:list[float]):
    n:int = len(lst)
    for i in range(len(lst)):
        res=sum(lst[i])
    Rep= res/n
    return Rep

utl=float(input("Saisir la iste :"))
print(Val_Moyenne(utl))"""

"""def moyenne(lst:list[float])->float:
    somme:float = 0.0
    for v in lst:
        somme += v # somme = somme + v
    return somme / len(lst)

maListe : list[float] =[]
for i in range(10):
    maListe.append(10*random())
    maListe.append(10*randint(0,10))

print(f'{maListe}, la moyenne vaut,{moyenne(maListe)}')
"""
"""def Sum_List(lst_1: list[float],lst_2:list[float]):
    Final:list[float]= []
    for i in range(0,len(lst_1)):
        Final.append(lst_1[i] + lst_2[i])
    return Final"""

def eraseDouble(lst:list[float]):
    l1:list[float] = []
    for i in lst: # pour toutes les valeurs de la liste lst
        if i not in l1: # if not(v in res): #  si v n'est pas dans res on l'ajoute
            l1.append(i)
    return l1
"""print(eraseDouble([1,5,8,6,5,4,2,1,1,8,9,5,5,5]))"""

"""def supprimerDoublons(lst)->None:
    i:int = 1
    tmp:list[float] = [lst[0]]
    while i<len(lst):
        if(lst[i] in tmp):
            del(lst[i])
        else:
            tmp.append(lst[i])
            i = i+1
"""

"""def Elt_communs(lst1:list[float],lst2:list[float]):
    res:list[float] = []
    for i in lst1:
        if i in lst2:
        #if lst1[i] == lst2[i]:
            res.append(i)
    return res"""

"""def Elt_communs(lst1:list[float],lst2:list[float]):
    res:list[float] = []
    l1=eraseDouble(lst1)
    l2=eraseDouble(lst2)
    for i in l1:
        if i in l2:
        #if lst1[i] == lst2[i]: # verification mais a une meme position
            res.append(i)
    return res
"""

def Elt_non_communs(lst1:list[float],lst2:list[float]):
    res:list[float] = []
    l1=eraseDouble(lst1)
    l2=eraseDouble(lst2)
    for i in l1:
        if i not in l2:
            res.append(i)
    return res

print(Elt_non_communs([0,5,10,1,4,7,11],[0,5,6,8,0,55,11]))


        




