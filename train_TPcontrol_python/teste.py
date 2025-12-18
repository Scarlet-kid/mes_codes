import os

def modifier_etudiant_dans_fichier(fichier: str) -> None:
    if not os.path.exists(fichier):
        print(f"Le fichier {fichier} n'existe pas.")
        return

    # 1) Lire toutes les lignes
    with open(fichier, "r", encoding="utf-8") as f:
        lignes = f.readlines()

    if not lignes:
        print("Le fichier est vide.")
        return

    # 2) Afficher les étudiants avec un numéro
    print("Liste des étudiants dans le fichier :")
    for i, ligne in enumerate(lignes, start=1):
        print(f"{i}. {ligne.strip()}")

    # 3) Demander quel numéro modifier
    try:
        num = int(input("Numéro de l'étudiant à modifier : "))
    except ValueError:
        print("Numéro invalide.")
        return

    if num < 1 or num > len(lignes):
        print("Numéro hors limites.")
        return

    # 4) Resaisir les infos de l'étudiant
    print("Saisissez les nouvelles informations pour cet étudiant :")
    nouvel_etu = saisie_etu_info()   # tu l'as déjà définie

    # 5) Remplacer la ligne
    lignes[num - 1] = str(nouvel_etu) + "\n"

    # 6) Réécrire tout le fichier
    with open(fichier, "w", encoding="utf-8") as f:
        f.writelines(lignes)

    print("Les informations de l'étudiant ont été modifiées.")
