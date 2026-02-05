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
    return Masomme/long(lst) - moy_carre

def ecart(lst:list[float])->float:
    return sqrt(variance(lst)) #on round avec 2

#------------------------------------------------------
def tri_bulle(lst:list[float])->list[float]:
    for j in range(len(lst)-1):
        if lst[j]>lst[j+1]:
            tmp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = tmp
    return lst

def mediane(lst:list[float])->float:
    lst_ordonné = tri_bulle(lst)
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

def moustache(x):
    minimum = mini(x)         
    q1, med, q3 = quartiles(x)
    maximum = maxi(x)          
    moy = moyenne(x)          
    plt.figure(figsize=(10, 5)) #Initialisation de la feuille vierge et de sa taille.
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

poids = [
    87, 49, 49, 56, 87, 66, 77, 69, 46, 100, 71, 96, 63, 69, 75, 83, 51, 100, 71, 53, 
    86, 74, 68, 76, 52, 53, 97, 46, 99, 51, 63, 59, 65, 79, 71, 84, 82, 69, 68, 70, 
    67, 87, 93, 58, 81, 48, 77, 49, 46, 49, 96, 61, 74, 92, 84, 82, 49, 59, 87, 91, 
    56, 74, 55, 82, 73, 96, 72, 46, 61, 60, 73, 65, 56, 64, 94, 48, 64, 72, 94, 81, 
    53, 64, 67, 74, 60, 81, 70, 52, 77, 51, 82, 88, 52, 75, 87, 77, 51, 100, 77, 59, 
    98, 46, 79, 94, 93, 80, 73, 51, 66, 62, 86, 71, 89, 91, 65, 59, 97, 81, 63, 50, 
    49, 59, 98, 83, 54, 100, 87, 55, 62, 48, 91, 81, 74, 91, 60, 91, 48, 93, 71, 46, 
    58, 79, 83, 77, 78, 75, 86, 89, 52, 70, 95, 69, 73, 89, 64, 79, 87, 87, 53, 56, 
    55, 52, 91, 63, 86, 64, 70, 87, 68, 50, 76, 70, 83, 48, 56, 70, 68, 69, 61, 47, 
    55, 100, 52, 85, 53, 60, 63, 79, 100, 95, 55, 47, 95, 52, 55, 91, 58, 71, 55, 77, 
    71, 67, 84, 61, 78, 95, 91, 97, 76, 55, 90, 55, 63, 100, 50, 72, 61, 64, 93, 55, 
    99, 89, 59, 57, 84, 84, 95, 58, 82, 60, 57, 99, 97, 92, 55, 56, 100, 99, 62, 74, 
    61, 95, 68, 58, 47, 64, 62, 85, 100, 78, 61, 55, 69, 77, 48, 63, 56, 52, 93, 71, 
    89, 78, 100, 63, 49, 73, 90, 58, 75, 64, 97, 47, 89, 63, 99, 45, 46, 69, 48, 94, 
    67, 50, 61, 56, 72, 91, 57, 57, 72, 71, 97, 46, 89, 53, 94, 60, 84, 80, 95, 48, 
    60, 71, 65, 54, 96, 89, 60, 91, 98, 84, 62, 100, 94, 99, 96, 50, 79, 67, 68, 85, 
    77, 67, 67, 64, 50, 74, 63, 90, 63, 70, 86, 86, 58, 55, 96, 57, 78, 84, 85, 77, 
    91, 79, 78, 71, 86, 65, 78, 53, 91, 54, 75, 63, 50, 78, 60, 47, 51, 84, 64, 55, 
    53, 58, 99, 50, 62, 59, 97, 58, 49, 77, 77, 67, 81, 55, 78, 69, 69, 63, 55, 51, 
    79, 94, 85, 74, 74, 74, 85, 51, 74, 90, 65, 87, 93, 94, 61, 47, 96, 69, 80, 65, 
    76, 53, 84, 69, 93, 94, 65, 50, 80, 63, 87, 77, 50, 63, 88, 100, 46, 79, 68, 96, 
    46, 87, 50, 52, 87, 73, 78, 54, 52, 99, 72, 94, 61, 86, 82, 65, 94, 89, 95, 95, 
    57, 64, 53, 56, 49, 91, 70, 99, 91, 45, 50, 74, 60, 77, 68, 95, 91, 68, 50, 48, 
    58, 54, 49, 72, 84, 89, 62, 89, 68, 60, 86, 62, 56, 66, 63, 88, 89, 98, 66, 60, 
    51, 49, 81, 85, 51, 54, 92, 94, 77, 74, 57, 48, 47, 64, 48, 57, 63, 93, 53, 49, 
    98, 58, 59, 71, 46, 46, 97, 95, 68, 75, 87, 73, 92, 66, 76, 72, 70, 99, 67, 81, 
    54, 65, 75, 66, 53, 53, 65, 90, 75, 57, 97, 48, 55, 89, 57, 87, 96, 90, 74, 64, 
    74, 56, 52, 73, 66, 69, 98, 50, 68, 79, 62, 82, 50, 52, 72, 90, 75, 47, 85, 98, 
    89, 77, 84, 63, 91, 91, 66, 48, 94, 52, 61, 78, 72, 90, 97, 54, 50, 47, 79, 68, 
    58, 53, 94, 97, 60, 57, 96, 94, 77, 62, 49, 46, 64, 50, 67, 67, 98, 77, 59, 66, 
    91, 90, 61, 100, 97, 78, 50, 49, 100, 85, 46, 74, 83, 46, 65, 95, 83, 82, 74, 77, 
    60, 80, 94, 74, 87, 88, 74, 70, 95, 97, 66, 47, 73, 51, 70, 73, 67, 79, 55, 76, 
    65, 87, 53, 56, 74, 69, 60, 85, 73, 53, 47, 53, 82, 80, 98, 71, 99, 61, 88, 52, 
    54, 64, 62, 100, 77, 86, 82, 52, 59, 55, 85, 86, 80, 62, 57, 62, 89, 46, 86, 95, 
    100, 48, 63, 71, 64, 98, 87, 82, 94, 82, 46, 95, 68, 65, 76, 61, 84, 94, 60, 51, 
    82, 71, 46, 58, 98, 92, 70, 100, 88, 54, 61, 72, 51, 96, 81, 96, 46, 95, 68, 72, 
    65, 49, 77, 64, 60, 50, 47, 82, 59, 58, 58, 78, 70, 88, 83, 85, 67, 76, 66, 96, 
    93, 99, 100, 97, 64, 79, 93, 80, 97, 51, 97, 97, 52, 79, 88, 96, 71, 64, 67, 86, 
    69, 57, 65, 84, 46, 72, 74, 63, 83, 91, 70, 50, 74, 88, 91, 97, 81, 77, 73, 59, 
    93, 74, 45, 82, 75, 65, 77, 58, 74, 90, 83, 100, 62, 82, 48, 58, 77, 84, 95, 55, 
    99, 75, 100, 70, 64, 83, 60, 74, 46, 63, 64, 46, 55, 69, 65, 74, 49, 96, 70, 47, 
    89, 79, 77, 47, 80, 65, 55, 66, 78, 71, 65, 54, 98, 92, 60, 82, 66, 96, 50, 56, 
    52, 56, 100, 79, 45, 56, 62, 98, 63, 53, 53, 98, 76, 65, 86, 75, 75, 91, 92, 79, 
    77, 79, 52, 73, 63, 54, 58, 97, 73, 47, 59, 51, 55, 69, 78, 86, 70, 61, 46, 66, 
    50, 84, 57, 55, 51, 53, 63, 92, 76, 81, 45, 74, 64, 70, 89, 87, 97, 100, 64, 93, 
    67, 69, 58, 52, 63, 46, 55, 53, 69, 98, 71, 48, 99, 75, 63, 47, 95, 71, 82, 52, 
    52, 84, 61, 83, 49, 58, 92, 47, 92, 59, 72, 55, 64, 99, 62, 45, 68, 90, 54, 64, 
    60, 77, 45, 61, 98, 78, 84, 48, 51, 89, 91, 100, 71, 49, 73, 94, 96, 83, 46, 72, 
    76, 54, 59, 65, 77, 83, 56, 99, 98, 76, 92, 50, 79, 96, 58, 63, 88, 93, 67, 63, 
    61, 53, 86, 75, 77
]


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
    print(moustache(poids))
    #etablir_releve(poids)
if __name__ == "__main__":
    prog()