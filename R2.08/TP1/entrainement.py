from matplotlib import pyplot as plt

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
    return (sommelstCarrée/long(lst)) - moyenne(lst)

def ecart(lst:list[float])->float:
    return variance(lst)**0.5

def tri_bulle(lst:list[float])->float:
    for _ in range(long(lst)):
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
    minimum = mini(lst)
    maximum = maxi(lst)
    q1,q2,q3 = quartile(lst)
    moy = moyenne(lst)
    plt.figure()
    plt.title("boite a moustache")
    plt.vlines(q2,0.8,1.2,colors='red') # La mediane
    plt.vlines(q1,0.8,1.2)
    plt.vlines(q3,0.8,1.2)
    plt.hlines(1.2,q1,q3)
    plt.hlines(0.8,q1,q3)
    plt.hlines(1,minimum,q1)
    plt.hlines(1,q3,maximum)
    plt.vlines(minimum,0.9,1.1)
    plt.vlines(maximum,0.9,1.1)
    plt.vlines(moy,0.8,1.2,colors='black')
    plt.text(minimum,0.6,f"min\n({minimum})",ha='center')
    plt.text(maximum,0.6,f"min\n({maximum})",ha='center')
    plt.text(q1,0.6,f"q1\n({q1})",ha='center')
    plt.text(q2,1.3,f"médiane\n({q2})",ha='center',c='red')
    plt.text(q3,0.6,f"q3\n({q3})",ha='center')
    plt.text(moy,0.6,f"moyenne\n({round(moy,2)})",ha='center',c='black')
    plt.ylim(0,2)
    plt.show()
    
with open("R2.08/TP1/poid.txt",'r') as file:
    myData = []
    for elt in file:
        elt.strip()
        myData.append(int(elt))

def etablir_releve(liste_poids):
    t = long(liste_poids)        
    mi = mini(liste_poids)      
    ma = maxi(liste_poids)       
    moy = moyenne(liste_poids)   
    ec = ecart(liste_poids)    
    q1, q2, q3 = quartile(liste_poids) 

    print(f"La taille de la liste est : {t}")
    print(f"La valeur minimale est : {mi}")
    print(f"La valeur maximale est : {ma}")
    print(f"La moyenne est : {moy}")
    print(f"L'écart-type est : {ec}")
    print(f"Les quartiles sont : ({q1}, {q2}, {q3})")

    moustache(liste_poids)
    
#print(etablir_releve(myData))

print(moustache(myData))
    
    