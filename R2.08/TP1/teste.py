import matplotlib.pyplot as plt

prix = [5, 10, 15, 20, 25, 30] 
clients = [84, 58, 30, 19, 7, 4]

def moyennel(z):
    return sum(z) / len(z)

def ecart_type(z):
    m = moyennel(z)
    variance = sum((val - m)**2 for val in z) / len(z)
    return variance**0.5

def covariance(z, y):
    """Calcule la covariance de z et y[cite: 86]."""
    mz = moyennel(z)
    my = moyennel(y)
    return sum((z[i] - mz) * (y[i] - my) for i in range(len(z))) / len(z)
def coefdir(z, y):
    """Calcule le coefficient directeur de la droite de régression[cite: 87]."""
    var_z = ecart_type(z)**2
    return covariance(z, y) / var_z

# --- (h) Fonction coeford ---
def coeford(z, y):
    return moyennel(y) - coefdir(z, y) * moyennel(z)

# --- (a) & (i) Fonction nuage_affine ---
def nuage_affine(z, y):
    """Affiche le nuage de points et la droite de régression[cite: 81, 90]."""
    a = coefdir(z, y)
    b = coeford(z, y)
    mz = moyennel(z)
    my = moyennel(y)
    
    plt.figure(figsize=(10, 6))
    
    # (a) Nuage de points
    plt.scatter(z, y, color='blue', label='Données (Clients/Prix)')
    
    # (c) Point moyen G [cite: 83]
    plt.plot(mz, my, 'ro', markersize=10, label=f'Point moyen G ({round(mz,2)}, {round(my,2)})')
    
    # (i) Droite de régression
    z_min, z_max = min(z), max(z)
    y_min, y_max = a * z_min + b, a * z_max + b
    plt.plot([z_min, z_max], [y_min, y_max], color='green', label='Droite de régression')
    
    # (i) Équation de la droite au point (25, 80) 
    equation_txt = f"y = {round(a, 2)}x + {round(b, 2)}"
    plt.text(25, 80, equation_txt, color='red', fontsize=12, fontweight='bold')
    
    # (i) Titres et Axes [cite: 92, 93]
    plt.title("Evolution des prix en fonction des clients")
    plt.xlabel("nb de clients")
    plt.ylabel("Prix")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.show()

# --- Affichage des résultats (Calculs vérifiés) ---
print("--- Résultats des calculs ---")
print(f"Moyenne (Prix) : {moyennel(prix)}")
print(f"Moyenne (Clients) : {moyennel(clients)}")
print(f"Écart-type (Prix) : {round(ecart_type(prix), 2)}")
print(f"Écart-type (Clients) : {round(ecart_type(clients), 2)}")
print(f"Coefficient directeur (a) : {round(coefdir(prix, clients), 4)}")
print(f"Ordonnée à l'origine (b) : {round(coeford(prix, clients), 4)}")

# Lancement du graphique
nuage_affine(prix, clients)