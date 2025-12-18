# conversion_cassis_gris.py

def lire_ppm(nom_fichier):
    """Lit un fichier PPM (format P3) et renvoie (largeur, hauteur, maxval, liste_pixels)."""
    with open(nom_fichier, "r") as f:
        tokens = []

        for ligne in f:
            ligne = ligne.strip()
            # Ignorer les lignes vides et les commentaires
            if not ligne or ligne.startswith("#"):
                continue
            tokens.extend(ligne.split())

    # En-tête
    magic = tokens[0]
    if magic != "P3":
        raise ValueError("Format PPM non supporté (seul P3 est accepté)")

    largeur = int(tokens[1])
    hauteur = int(tokens[2])
    maxval = int(tokens[3])

    # Le reste : R V B R V B ...
    valeurs = list(map(int, tokens[4:]))

    return largeur, hauteur, maxval, valeurs


def ecrire_ppm_gris(nom_fichier, largeur, hauteur, maxval, pixels_gris):
    """Écrit un fichier PPM P3 en niveaux de gris."""
    with open(nom_fichier, "w") as f:
        f.write("P3\n")
        f.write(f"{largeur} {hauteur}\n")
        f.write(f"{maxval}\n")

        # Écrire les pixels (G G G par pixel)
        cpt = 0
        for g in pixels_gris:
            f.write(f"{g} {g} {g} ")
            cpt += 1
            # Retour à la ligne après quelques pixels pour garder le fichier lisible
            if cpt % 5 == 0:
                f.write("\n")


def convertir_en_gris(entree="cassis.ppm", sortie="cassisNG.ppm"):
    largeur, hauteur, maxval, valeurs = lire_ppm(entree)

    pixels_gris = []
    # Parcourir les valeurs par groupes de 3 : R, V, B
    for i in range(0, len(valeurs), 3):
        R = valeurs[i]
        V = valeurs[i + 1]
        B = valeurs[i + 2]
        G = (R + V + B) // 3  # niveau de gris entier
        pixels_gris.append(G)

    ecrire_ppm_gris(sortie, largeur, hauteur, maxval, pixels_gris)
    print(f"Conversion terminée : {entree} → {sortie}")


# Appel de la fonction principale
convertir_en_gris()
