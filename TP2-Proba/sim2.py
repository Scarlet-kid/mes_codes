import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from code import binomiale, Phi

p = 0.01

# --- 1. Tracé des fonctions de répartition (n = 1000 et n = 100) ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for ax, n in zip(axes, [1000, 100]):
    m = n * p
    sigma = sqrt(n * p * (1 - p))
    
    # Plage d'affichage adaptée
    k_max = int(m + 4 * sigma)
    k_vals = list(range(k_max + 1))
    
    # Fonction de répartition exacte F(k) = P(X <= k)
    F_vals = []
    cumul = 0.0
    for k in k_vals:
        cumul += binomiale(n, p, k)
        F_vals.append(cumul)
    
    # Courbe continue de la loi normale
    x_vals = np.linspace(-0.5, k_max + 0.5, 300)
    normale_vals = [Phi((x - m) / sigma) for x in x_vals]
    
    # Tracé
    ax.step(k_vals, F_vals, where="post", label="Loi binomiale (escalier)", color="royalblue", linewidth=2)
    ax.plot(x_vals, normale_vals, label="Approximation normale", color="crimson", linestyle="--")
    
    ax.set_title(f"n = {n}, p = {p}")
    ax.set_xlabel("k")
    ax.set_ylabel("F(k)")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend()

plt.tight_layout()

# --- 2. Calcul pour n = 100 de P(Y <= -0.5) ---
n_test = 100
m_test = n_test * p
sigma_test = sqrt(n_test * p * (1 - p))
proba_neg = Phi((-0.5 - m_test) / sigma_test)

print(f"--- Question 6 ---")
print(f"Pour n = 100 : P(Y <= -0.5) = {proba_neg:.4f} (soit environ {proba_neg * 100:.2f} %)")

plt.show()