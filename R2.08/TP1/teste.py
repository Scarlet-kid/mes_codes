import matplotlib.pyplot as plt
## Question 1
def long(liste:list):
    cpt = 0
    for elmt in liste:
        cpt +=1
    return cpt
#print (long([1,2,3]))

# Question 2
def somme (liste: list):
    cpt =0
    for elmt in liste:
        cpt += elmt
    return cpt
#print (somme([1,2,3]))    

## QuESTion 3
def mini(liste):
    if not  liste: return None
    valeur_mini = liste[0] 
    for elmt in liste:
        if elmt < valeur_mini:
            valeur_mini = elmt
    return valeur_mini
             
#print (mini([1,2,3]))


# question 4
def maxi (liste:list):
    if not liste: return None
    valeur_maxi = liste[0]
    for elmt in liste:
        if elmt > valeur_maxi:
            valeur_maxi = elmt
    return valeur_maxi
#print(maxi([1,2,3]))


# Question 5
def moyenne (liste:list):
    n = long(liste)
    if n == 0: return 0
    moyen = somme(liste)/n
    return (moyen)
#print(moyenne([1,2,3]))
    
## Question 6
def ecart (liste:list):
    n = long(liste)
    moyen = moyenne(liste)
    if n ==0 :return 0
    somme_carre = 0
    for elmt in liste:
        somme_carre += (elmt - moyen)**2
    variance = somme_carre/ n
    return  (variance **0.5)
#print(ecart([1,2,3]))

## Querstion 7
def tri_bulle(liste):
    n = long(liste)
    for i in range(n):
        for j  in range(0,n-i-1):
            if liste[j] > liste[j+1]:
                liste[j],liste[j+1] = liste[j+1],liste[j]
    return liste
#print(tri_bulle([2,3,1]))

## Question 8
def mediane (liste:list):
    Trie= tri_bulle(liste)
    n = long(Trie)
    if n % 2 == 1:
        return Trie[n // 2]
    else:
        return (Trie[n // 2 - 1] + Trie[n // 2]) / 2
#print (mediane([1,2,3]))

## question 9
def quartiles (liste:list):
    Trie = tri_bulle(liste)
    n = long(Trie)
    q1 = Trie[(n + 3) // 4 - 1]  
    q2 = mediane(Trie)
    q3 = Trie[(3 * n + 3) // 4 - 1]
    return (q1, q2, q3)
#print (quartiles([1,2,3]))

## # Diagramme de Tukey

def moustache(liste):
    #  Recupération de mes données 
    mi = mini(liste)
    ma = maxi(liste)
    moy = moyenne(liste)
    q1, med, q3 = quartiles(liste)
    
    plt.figure(figsize=(10, 6))
    
    # 1 Dessin de la boite et des moustaches
    plt.plot([q1, q3, q3, q1, q1], [-1, -1, 1, 1, -1], color='blue')
    plt.plot([mi, q1], [0, 0], color='blue')
    plt.plot([q3, ma], [0, 0], color='blue')
    
    # 2 Traits verticaux
    plt.plot([mi, mi], [-0.5, 0.5], color='blue') 
    plt.plot([ma, ma], [-0.5, 0.5], color='blue')
    plt.plot([med, med], [-1, 1], color='blue', linewidth=2) 
    plt.plot([moy, moy], [-1, 1], color='red')              
    
    # 3 Textes et valeurs numériques
    plt.text(mi, -1.5, f"min\n({mi})", ha='center', va='top')
    plt.text(q1, -2.0, f"q1\n({q1})", ha='center', va='top')
    plt.text(med, -1.5, f"med\n({med})", ha='center', va='top')
    plt.text(q3, -2.0, f"q3\n({q3})", ha='center', va='top')
    plt.text(ma, -1.5, f"max\n({ma})", ha='center', va='top')
    
    # Texte pour la moyenne
    plt.text(moy, 1.2, f"({moy})\nmoy", color='red', ha='center', va='bottom')
    
    plt.title("diagramme de Tukey")
    plt.axis('off') 
    plt.ylim(-3, 3)  
    plt.show()

# --- Lecture du fichier poids.txt ---
poids_patients = []
with open("R2.08/TP1/poid.txt", "r") as f:
    for ligne in f:
        val = ligne.strip()
        if val:
            poids_patients.append(float(val))

# Calculs des éléments statistiques
n_taille = long(poids_patients)
v_min = mini(poids_patients)
v_max = maxi(poids_patients)
v_moy = moyenne(poids_patients)
v_ecart = ecart(poids_patients)
q_result = quartiles(poids_patients)

# Affichage des ré©sultats dans la console
print(f"La taille de la liste est: {n_taille}")
print(f"La valeur minimale est: {v_min}")
print(f"La valeur maximale est: {v_max}")
print(f"La moyenne est: {v_moy}")
print(f"L'Ã©cart-type est {v_ecart}")
print(f"Les quartiles sont ({q_result[0]}, {q_result[1]}, {round(q_result[2], 1)})")

# Lancement du graphique
#moustache(poids_patients)
print(moustache([i for i in range(1,101)]))