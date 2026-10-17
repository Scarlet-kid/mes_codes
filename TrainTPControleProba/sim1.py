import matplotlib.pyplot as plt
import numpy as np
from code import binomiale, joueur

n = 200
p = 0.01
#le p cest quoi oft ?
nb_simulations = 10000

#Simulation des 10000 joueurs.
resultats = [joueur(n,p) for _ in range(nb_simulations)]

# fréquences observées et proba théorique pour k de 0 à 8.
valeurs_k = np.arange(0,9)
frequences = [resultats.count(k)/nb_simulations for k in valeurs_k]
probas_theoriques = [binomiale(n,p,k) for k in valeurs_k]

#Tracé graphique
plt.figure(figsize=(10,6))
plt.bar(valeurs_k,frequences,width=0.5, alpha=0.6,label="Fréquence simulées de 10000 joueurs",color="skyblue",edgecolor="black")
plt.plot(valeurs_k,frequences,'ro',label="Probabilité théorique",markersize=8)
plt.xlabel("Nombre d'objet légendaire k")
plt.ylabel('Fréquence/probabilité')
plt.title("comparaison simulation vs théorie")
plt.xticks(valeurs_k)
plt.legend()
plt.grid(axis='y',linestyle='--',alpha=0.7)
plt.show()
