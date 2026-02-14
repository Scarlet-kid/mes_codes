from math import sqrt
import matplotlib.pyplot as plt

def long(lst:list[float])->int:
    res = 0
    for _ in(lst):
        res += 1
    return res # C'est carré

def somme(lst:list[float])->float:
    res = 0
    for i in lst:
        res += i
    return res

def mini(lst:list[float])->float:
    mini = lst[0]
    for i in lst:
        if i < mini:
            mini = i
    return mini

# On peut optimiser pt en commence le parcours a partir de lst[1::]

def maxi(lst:list[float])->float:
    maxi = lst[0]
    for i in lst:
        if i > maxi:
            maxi = i
    return maxi

def moyenne(lst:list[float])->float:
    return round(somme(lst)/long(lst),2)

# Séparation de l'ecart type en fct
def variance(lst:list[float])->float:
    lst2 = []
    for i in lst:
        lst2.append(i**2)
    moy_carre = moyenne(lst)**2
    Masomme = somme(lst2)
    return (Masomme/long(lst)) - moy_carre #Plus de sécurité

def ecart(lst:list[float])->float:
    return sqrt(variance(lst)) #on round avec 2 deux chiffres apres la virgule

#------------------------------------------------------
def tri_bulle(lst:list[float])->float:
    for _ in range(long(lst)):
        for i in range(long(lst)-1):
            if lst[i]>lst[i+1]: # SI ce qu'il y'a avant est plus grand que ce qu'il ya apres
                tmp = lst[i] # On met dans une variable le plus grand par défaut cest a dire ce qu'il ya avant
                lst[i] = lst[i+1] # On écrase ce qu'il ya avant avec le plus petit
                lst[i+1] = tmp # Et ce qu'il ya apres prend la plus grande valeur pour que le cycle continue.
    return lst

def mediane(lst:list[float])->float:
    lst_ordonné = tri_bulle(lst) # Tres important faut tjrs trié avant la mediane.
    n = long(lst_ordonné)
    #print(n)
    if n % 2 == 0:
        val1 = lst_ordonné[n//2]
        val2 = lst_ordonné[(n//2)-1]
        return (val1+val2)/2
    else:
        return lst_ordonné[n//2]
    
def quartiles(lst:list[float]):
    q2 = mediane(lst)
    l1 = lst[0:long(lst)//2]
    q1 = mediane(l1)
    l2 = lst[(long(lst)//2)+1::]
    q3 = mediane(l2)
    return q1 ,q2 ,q3

def moustache(x:list[float]):
    minimum = mini(x)         
    q1, med, q3 = quartiles(x)
    maximum = maxi(x)          
    moy = moyenne(x)          
    plt.figure() #Initialisation de la feuille vierge et de sa taille. pas de taille il va s'adapter
    plt.title("diagramme de Tukey") #Titre
    plt.plot([q1, q3], [0.2, 0.2], color='blue')  
    plt.plot([q1, q3], [0.4, 0.4], color='blue')
    plt.plot([q1, q1], [0.2, 0.4], color='blue') 
    plt.plot([q3, q3], [0.2, 0.4], color='blue')
    plt.plot([minimum, q1], [0.3, 0.3], color='blue')
    plt.plot([q3, maximum], [0.3, 0.3], color='blue') 
    plt.plot([minimum, minimum], [0.25, 0.35], color='blue')
    plt.plot([maximum, maximum], [0.25, 0.35], color='blue') 
    plt.plot([med, med], [0.2, 0.4], color='blue', linewidth=2)
    plt.plot([moy, moy], [0.2, 0.4], color='red', linewidth=2) 
    plt.text(minimum, 0.15, f"min\n({minimum})", ha='center', va='top')
    plt.text(q1, 0.15, f"q1\n({q1})", ha='center', va='top')
    plt.text(med, 0.15, f"med\n({med})", ha='center', va='top')
    plt.text(q3, 0.15, f"q3\n({q3})", ha='center', va='top')
    plt.text(maximum, 0.15, f"max\n({maximum})", ha='center', va='top')
    plt.text(moy, 0.45, f"({moy})\nmoy", color='red', ha='center', va='bottom')
    plt.axis('off')
    plt.ylim(0, 0.7) 
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
    q1, q2, q3 = quartiles(liste_poids) 

    print(f"La taille de la liste est : {t}")
    print(f"La valeur minimale est : {mi}")
    print(f"La valeur maximale est : {ma}")
    print(f"La moyenne est : {moy}")
    print(f"L'écart-type est : {ec}")
    print(f"Les quartiles sont : ({q1}, {q2}, {q3})")

    moustache(liste_poids)


def prog():
    #print(long([1,2,3]))
    #print(somme([1,2,3]))
    #print(mini([1,2,3]))
    #print(maxi([1,2,3]))
    #print(moyenne([1,2,3]))
    #print(ecart([1,2,3]))
    #print(tri_bulle([5,7,9,6,1]))
    #print(mediane([5,7,9,6,4,1,8]))
    #print(quartiles([i for i in range(10)]))
    #[0,1,2,3,4,5,6,7,8,9]
    print(moustache([i for i in range(1,101)]))
    #etablir_releve(myData)
if __name__ == "__main__":
    prog()