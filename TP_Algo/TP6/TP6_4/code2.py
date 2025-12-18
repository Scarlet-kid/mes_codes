import os

def lire_ppm(nom_fichier):
    with open(nom_fichier, "r") as f:
        tokens = []
        for ligne in f:
            ligne = ligne.strip()
            if not ligne or ligne.startswith("#"):
                continue
            tokens.extend(ligne.split())

    it = iter(tokens)
    magic = next(it)
    if magic != "P3":
        raise ValueError("Format PPM non supporté (il faut du P3 ASCII)")

    largeur = int(next(it))
    hauteur = int(next(it))
    maxval = int(next(it))

    pixels = []
    for _ in range(largeur * hauteur):
        r = int(next(it))
        g = int(next(it))
        b = int(next(it))
        pixels.append((r, g, b))

    return largeur, hauteur, maxval, pixels


def rgb_vers_gris_2d(largeur, hauteur, pixels):
    gris = [[0 for _ in range(largeur)] for _ in range(hauteur)]
    i = 0
    for y in range(hauteur):
        for x in range(largeur):
            r, g, b = pixels[i]
            i += 1
            val = int(0.299 * r + 0.587 * g + 0.114 * b)
            gris[y][x] = val
    return gris


def detecter_contours(largeur, hauteur, gris, seuil=20):
    pbm = [[0 for _ in range(largeur)] for _ in range(hauteur)]

    for y in range(hauteur - 1):
        for x in range(largeur - 1):
            g = gris[y][x]
            diff_droite = abs(g - gris[y][x + 1])
            diff_bas = abs(g - gris[y + 1][x])

            if diff_droite > seuil or diff_bas > seuil:
                pbm[y][x] = 1
            else:
                pbm[y][x] = 0

    return pbm


def ecrire_pbm(nom_fichier, largeur, hauteur, pbm):
    with open(nom_fichier, "w") as f:
        f.write("P1\n")
        f.write(f"{largeur} {hauteur}\n")
        for y in range(hauteur):
            ligne = " ".join(str(pbm[y][x]) for x in range(largeur))
            f.write(ligne + "\n")


def ppm_vers_pbm_contours(entree, sortie, seuil=20):
    largeur, hauteur, maxval, pixels = lire_ppm(entree)
    gris = rgb_vers_gris_2d(largeur, hauteur, pixels)
    pbm = detecter_contours(largeur, hauteur, gris, seuil=seuil)
    ecrire_pbm(sortie, largeur, hauteur, pbm)


if __name__ == "__main__":
    # dossier où se trouve le script .py
    dossier_script = os.path.dirname(os.path.abspath(__file__))

    # on demande le nom du fichier PPM à l'utilisateur
    nom_ppm = input("Nom du fichier PPM (par ex. chat.ppm) : ").strip()

    # chemin complet vers ce fichier dans le même dossier que le script
    chemin_entree = os.path.join(dossier_script, nom_ppm)

    # nom de sortie (même base + _contours.pbm)
    base, _ = os.path.splitext(nom_ppm)
    chemin_sortie = os.path.join(dossier_script, base + "_contours.pbm")

    try:
        ppm_vers_pbm_contours(chemin_entree, chemin_sortie, seuil=20)
        print("Image PBM créée :", chemin_sortie)
    except FileNotFoundError:
        print("Erreur : je ne trouve pas le fichier", chemin_entree)
    except Exception as e:
        print("Erreur :", e)
