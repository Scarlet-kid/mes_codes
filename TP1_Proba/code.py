from math import*
from random import*
import matplotlib.pyplot as plt

def generer_gamme_prix(n:int)->list[int]:
    lst = []
    for i in range(n):
        lst.append(round(uniform(0,500),2))
    return lst

def liste_chiffre_centimes(lst:list[int]):
    return [round((prix*100)%10) for prix in lst]

def frequences_centimes(lst:list[int]):
    maL = []
    for x in range(10):
        maL.append(lst.count(x)/len(lst))
    return maL

def gain(n: int) -> int:
    gains = {
        0: 0,
        1: -1,
        2: -2,
        3: 2,
        4: 1,
        5: 0,
        6: -1,
        7: -2,
        8: 2,
        9: 1
    }
    return gains[n]

def simuler_achat(gamme_prix):
   
    centimes = liste_chiffre_centimes(gamme_prix)
    freqs = frequences_centimes(centimes)
    
    u = random()
    
    somme_cumulee = 0
    for k in range(10):
        somme_cumulee += freqs[k]
        if u <= somme_cumulee:
            return k
    
    return 9

def simuler_n_achats(n, gamme_prix):
    somme_centimes = 0
    for _ in range(n):
        somme_centimes += simuler_achat(gamme_prix)
        
    return somme_centimes % 10

def simuler_n_achats_p_clients(n, p, gamme):
    gain_total = 0
    for _ in range(p):
        centimes_client = simuler_n_achats(n, gamme)
        gain_total += gain(centimes_client)
    return gain_total

def frequence_gain(liste_gains):
    gains_uniques = sorted(set(liste_gains))
    return [(g, liste_gains.count(g)) for g in gains_uniques]

def histo(liste_gains):
    plt.figure()
    plt.hist(liste_gains, edgecolor='black', alpha=0.7)
    plt.xlabel("chiffres des centimes")
    plt.ylabel("effectifs")
    plt.show()

from statistics import mean, pstdev

def reponse(nb_articles_gamme, nb_articles_panier, nb_clients, nb_tests):

    gamme = generer_gamme_prix(nb_articles_gamme)
    
    gains = []
    for _ in range(nb_tests):
        gain_test = simuler_n_achats_p_clients(nb_articles_panier, nb_clients, gamme)
        gains.append(gain_test)
    
    histo(gains)
    
    minimum = min(gains)
    moyenne = mean(gains)
    ecart_type = pstdev(gains)
    maximum = max(gains)
    
    return [minimum, moyenne, ecart_type, maximum]


if __name__ == '__main__':
    #print(generer_gamme_prix(10))
    Malst = generer_gamme_prix(10)
    #print(Malst)
    #liste_chiffre_centimes(Malst)

    '''x=generer_gamme_prix(100)
    b=frequences_centimes(liste_chiffre_centimes(x))'''
    '''print(b)
    print(len(b))'''

    #print(gain(len(Malst)))
    print(histo([-5, 3, 10, 7, 8, 10, 9, -3, -2, -4, 3, 7, 5, -5, -7]))

    
"""
Voici la réponse et l'analyse pour la **question 2 du grand 3** (Commenter les résultats et répondre au problème posé) :

### Commentaire des résultats

* **Moyenne proche de 0** : Sur un grand nombre de transactions (`nb_tests` élevé), la somme moyenne des gains/pertes tend vers $0$ centime.
* **Distribution symétrique** : L'histogramme suit une distribution centrée sur zéro (loi normale selon le théorème central limite).
* **Compensation réciproque** : Les arrondis en faveur du client (terminaisons en 1, 2, 6, 7 centimes) compensent statistiquement les arrondis en faveur du commerçant (terminaisons en 3, 4, 8, 9 centimes).



---

### Réponse au problème posé

1. **La règle est-elle favorable ou défavorable aux clients ?**
Elle est **neutre sur le long terme**. Aucun des deux acteurs (client ou commerçant) ne subit de perte ni ne réalise de bénéfice significatif de façon systématique.
2. **Le supermarché peut-il contourner la règle pour augmenter son chiffre d'affaires ?**
* Avec une distribution uniforme des prix (prix fixés au hasard), **non**, il n'y a aucun gain.
* **En pratique** : Le commerçant pourrait théoriquement optimiser ses prix en fixant ses tarifs avec des fins de prix stratégiques (ex: terminer systématiquement les prix par `,99 €` ou `,98 €` pour provoquer des arrondis par excès de +1 ou +2 centimes lors d'achats à l'unité). Cependant, dès qu'un panier contient plusieurs articles, la combinaison des centimes redevient quasi-aléatoire.
"""