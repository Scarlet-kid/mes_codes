import matplotlib.pyplot as plt
import numpy as np
from code import erreur_max

# 150 valeurs de p réparties régulièrement entre 0.002 et 0.3
p_vals = np.linspace(0.002, 0.3, 150)

# Calcul des erreurs maximales pour n = 200 et n = 1000
erreurs_200 = [erreur_max(200, p) for p in p_vals]
erreurs_1000 = [erreur_max(1000, p) for p in p_vals]

# Tracé
plt.figure(figsize=(10, 6))
plt.plot(p_vals, erreurs_200, label="n = 200", color="tab:blue", linewidth=2)
plt.plot(p_vals, erreurs_1000, label="n = 1000", color="tab:orange", linewidth=2)

plt.xlabel("Probabilité p")
plt.ylabel("Erreur maximale commise")
plt.title("Erreur maximale d'approximation normale avec correction de continuité")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()