#!/usr/bin/env python3
import os

# Demander le nom du fichier PGM
nom_fichier = input("Nom du fichier PGM (ex : im1.pgm) : ")

# Ouvrir le fichier en lecture texte
f = open(nom_fichier, "r")

# 1) Lire la première ligne : "P2"
magic = f.readline().strip()
if magic != "P2":
    print("Erreur : ce programme ne gère que le format PGM ASCII (P2)")
    f.close()
    exit()

# 2) Lire les dimensions : "largeur hauteur"
ligne_dim = f.readline().strip()
largeur, hauteur = map(int, ligne_dim.split())

# 3) Lire la valeur maximale des niveaux de gris
ligne_max = f.readline().strip()
maxval = int(ligne_max)

# 4) Lire le reste : toutes les valeurs de pixels
donnees_pixels = f.read().split()
f.close()

if len(donnees_pixels) != largeur * hauteur:
    print("Erreur : nombre de pixels incohérent avec les dimensions")
    print("largeur * hauteur =", largeur * hauteur, "mais on a", len(donnees_pixels), "valeurs")
    exit()

# Conversion en entiers
pixels = [int(v) for v in donnees_pixels]

# 5) Calcul du négatif : nouveau = maxval - ancien
pixels_neg = [maxval - v for v in pixels]

# 6) Construire le nom du fichier de sortie : im1.pgm -> im1Reverse.pgm
racine, ext = os.path.splitext(nom_fichier)
nom_sortie = racine + "Reverse" + ext

# 7) Écrire le nouveau fichier PGM
g = open(nom_sortie, "w")
g.write("P2\n")
g.write(f"{largeur} {hauteur}\n")
g.write(str(maxval) + "\n")

for i, v in enumerate(pixels_neg):
    g.write(str(v))
    if (i + 1) % largeur == 0:
        g.write("\n")
    else:
        g.write(" ")

g.close()

print("Fichier négatif créé :", nom_sortie)
