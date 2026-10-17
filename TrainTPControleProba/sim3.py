import matplotlib.pyplot as plt
import numpy as np
from code import erreur_max  # La fonction déjà donnée dans le sujet

#150 valeurs de proba entre deux bornes:
p_liste = np.linspace(0.002,0.3,150)

#on calcul l'erreur max pour chaque p pour n=200  et 1000
erreurs_200 = [erreur_max(200,p) for p in p_liste]
erreurs_1000 = [erreur_max(1000,p) for p in p_liste]

#Tracé
plt.plot(p_liste,erreurs_200,label="n = 200")
plt.plot(p_liste,erreurs_1000,label="n = 1000")
plt.xlabel("probabilité")
plt.ylabel("erreur max")
plt.legend()
plt.show()