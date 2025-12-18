# francais.py

# Tu choisis ici les dimensions que tu veux :
largeur = int(input("Saisir la largeur souhaitée:"))
hauteur = int(input("Saisir la hauteur souhaitée:"))

nom_fichier = "francais.ppm"

with open(nom_fichier, "w") as f:
    # En-tête du format PPM (mode texte P3)
    f.write("P3\n")
    f.write(f"{largeur} {hauteur}\n")
    f.write("255\n")  # valeur max pour une composante de couleur

    # Générer les pixels du drapeau bleu-blanc-rouge
    for y in range(hauteur):
        ligne = []
        for x in range(largeur):
            # On coupe la largeur en 3 bandes verticales
            bande = (x * 3) // largeur

            if bande == 0:        # bleu
                r, g, b = 0, 0, 255
            elif bande == 1:      # blanc
                r, g, b = 255, 255, 255
            else:                 # rouge
                r, g, b = 255, 0, 0

            ligne.append(f"{r} {g} {b}")
        f.write(" ".join(ligne) + "\n")

print(f"Image du drapeau français générée dans le fichier {nom_fichier}")
