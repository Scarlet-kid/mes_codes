import matplotlib.pyplot as plt
import numpy as np
from code import binomiale, joueur
n = 200
p = 0.01
nb_simulations = 10000

resultats = [joueur(n, p) for _ in range(nb_simulations)]

# Fréquences observées et probabilités théoriques pour k de 0 à 8
valeurs_k = np.arange(0, 9)
frequences = [resultats.count(k) / nb_simulations for k in valeurs_k]
probas_theoriques = [binomiale(n, p, k) for k in valeurs_k]

# Tracé graphique
plt.figure(figsize=(10, 6))
plt.bar(valeurs_k, frequences, width=0.5, alpha=0.6, label="Fréquences simulées (10 000 joueurs)", color="skyblue", edgecolor="black")
plt.plot(valeurs_k, probas_theoriques, 'ro', markersize=8, label=r"Probabilités théoriques $\mathbb{P}(X=k)$")
#plus on repete l'experience ^lus mes proportions s'approche des valeurs théoriques.

plt.xlabel("Nombre d'objets légendaires (k)")
plt.ylabel("Fréquence / Probabilité")
plt.title(f"Comparaison simulation vs théorie (n={n}, p={p})")
plt.xticks(valeurs_k)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()