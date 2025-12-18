# ppm_vers_pgm.py

def lire_ppm(nom_fichier):
    """Lit un fichier PPM (format texte P3) et renvoie (largeur, hauteur, maxval, liste_RVB)."""
    tokens = []

    with open(nom_fichier, "r") as f:
        for ligne in f:
            ligne = ligne.strip()
            # On ignore les lignes vides et les commentaires
            if not ligne or ligne.startswith("#"):
                continue
            tokens.extend(ligne.split())

    # En-tête
    magic = tokens[0]
    if magic != "P3":
        raise ValueError("Seul le format P3 (PPM ASCII) est supporté")

    largeur = int(tokens[1])
    hauteur = int(tokens[2])
    maxval = int(tokens[3])

    # Le reste : R V B R V B ...
    valeurs = list(map(int, tokens[4:]))

    if len(valeurs) != 3 * largeur * hauteur:
        raise ValueError("Nombre de valeurs incohérent avec les dimensions de l'image")

    return largeur, hauteur, maxval, valeurs


def ecrire_pgm(nom_fichier, largeur, hauteur, maxval, niveaux_gris):
    """Écrit un fichier PGM (format texte P2) à partir d'une liste de niveaux de gris."""
    with open(nom_fichier, "w") as f:
        f.write("P2\n")
        f.write(f"{largeur} {hauteur}\n")
        f.write(f"{maxval}\n")

        # On écrit les valeurs de G, on met des retours à la ligne régulièrement
        cpt = 0
        for g in niveaux_gris:
            f.write(f"{g} ")
            cpt += 1
            if cpt % 20 == 0:   # 20 pixels par ligne pour la lisibilité
                f.write("\n")


def convertir_ppm_en_pgm(entree, sortie):
    largeur, hauteur, maxval, valeurs = lire_ppm(entree)

    niveaux_gris = []
    # On parcourt les valeurs 3 par 3 : (R, V, B)
    for i in range(0, len(valeurs), 3):
        R = valeurs[i]
        V = valeurs[i + 1]
        B = valeurs[i + 2]
        G = (R + V + B) // 3   # niveau de gris entier
        niveaux_gris.append(G)

    ecrire_pgm(sortie, largeur, hauteur, maxval, niveaux_gris)
    print(f"Conversion terminée : {entree} → {sortie}")


# Exemple d'utilisation :
# mettre un fichier image.ppm dans le même dossier,
# puis adapter les noms si besoin.
convertir_ppm_en_pgm("Cassis.ppm", "CassisNG.pgm")
