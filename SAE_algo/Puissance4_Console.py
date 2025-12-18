import time
# Jeu Puissance 4

# Demande le pseudo du joueur 1
Joueur_1_pseudo: str = input("Saisir le pseudo du joueur 1 : ")
print(f"Bonjour {Joueur_1_pseudo}, vous jouerez avec les pions Jaune (J)")
Joueur_1_lettre: str = "J"

# Demande le pseudo du joueur 2
Joueur_2_pseudo: str = input("Saisir le pseudo du joueur 2 : ")  
print(f"Bonjour {Joueur_2_pseudo}, vous jouerez avec les pions Rouge (R)")
Joueur_2_lettre: str = "R"

def creer_grille() -> list[list[str]]:
    """
    Crée une grille vide de 6 lignes et 7 colonnes
    Retourne : list[list[str]]
    """
    
    return [
                [" "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "],
                [" "," "," "," "," "," "," "]   
            ]

def afficher_grille(grille: list[list[str]]) -> None:
    """
    Affiche la grille de jeu
    Paramètre : grille (list[list[str]])
    Retourne : None
    """

    for ligne in grille:
        print("-"*15)
        print("|" + "|".join(ligne) + "|") # Joint tous les éléments de la liste avec le séparateur.
    print("-"*15)


def est_gagnant(grille: list[list[str]], jeton: str) -> bool:
    """
    Vérifie si le joueur (jeton) a 4 jetons alignés (horizontal, vertical ou diagonal).
    Paramètres :
        grille : list[list[str]]
        jeton : str
    Retourne : bool
    """
    lignes: int = len(grille)
    colonnes: int = len(grille[0])
    directions: list[tuple[int, int]] = [(0,1), (1,0), (1,1), (-1,1)]
    # (0,1) : horizontal → avancer en colonne vers la droite
    # (1,0) : vertical → avancer en ligne vers le bas
    # (1,1) : diagonale descendante → avancer en ligne et colonne vers le bas à droite ↘
    # (-1,1) : diagonale montante → reculer en ligne et avancer en colonne vers le haut à droite ↗
    for i in range(lignes): # parcourt toutes les lignes
        for j in range(colonnes): # parcourt toutes les colonnes
            if grille[i][j] == jeton: # Si la case contient le jeton d'un joueur
                for dx, dy in directions: # On teste chacune des 4 directions (dx, dy)
                    try:
                        if all(
                            0 <= i+dx*k < lignes and # vérifie qu'on reste dans les limites de la grille
                            0 <= j+dy*k < colonnes and # vérifie qu'on reste dans les limites de la grille
                            grille[i+dx*k][j+dy*k] == jeton # vérifie l'alignement des jetons
                            for k in range(4) # vérifie 4 positions dans la direction (dx, dy)
                            # Si pour tous les k (0..3) les trois conditions sont vraies, alors on a trouvé 4 jetons consécutifs et la fonction retourne True.
                        ):
                            return True
                    except Exception:
                        continue  # J'ai mis ca dans un try-except pour éviter les erreurs d'index hors limites.
                    # À chaque point où le joueur a un jeton, on regarde s'il y a 3 autres jetons identiques dans l'une des directions autorisées
    return False



def grille_pleine(grille: list[list[str]]) -> bool:
    """
    Vérifie si la grille est pleine (aucune case vide)
    Paramètre : grille (list[list[str]])
    Retourne : bool
    """
    return all(cell != " " for row in grille for cell in row)


def demander_colonne(grille: list[list[str]], joueur: str) -> int:
    """
    Demande au joueur la colonne où placer son jeton.
    Paramètres :
        grille : list[list[str]]
        joueur : str
    Retourne : int (indice de colonne)
    """
    while True:
        col_input: str = input(f"{joueur}, choisissez une colonne (1-7): ")
        if not col_input.isdigit():
            print("Veuillez entrer un nombre entier valide.")
            continue
        col: int = int(col_input) - 1
        if not (0 <= col < 7):
            print("Colonne invalide. Choisissez entre 1 et 7.")
            continue
        # Vérifie si la colonne est pleine
        if grille[0][col] != " ":
            print("Colonne pleine, choisissez une autre.")
            continue
        return col

 
def placer_jeton(grille: list[list[str]], col: int, jeton: str) -> tuple[int, int]:
    """
    Place le jeton dans la colonne choisie, à la première case libre en partant du bas.
    Paramètres :
        grille : list[list[str]]
        col : int
        jeton : str
    Retourne : tuple[int, int] (ligne, colonne)
    """
    for ligne in reversed(range(6)):
        if grille[ligne][col] == " ":
            grille[ligne][col] = jeton
            return ligne, col
    return None, None  # Ne devrait jamais arriver si la colonne est vérifiée


def jeu_puissance4() -> None:
    """
    Fonction principale du jeu Puissance 4
    Retourne : None
    """
    grille: list[list[str]] = creer_grille()
    afficher_grille(grille)
    joueurs: list[tuple[str, str]] = [[Joueur_1_pseudo, Joueur_1_lettre], (Joueur_2_pseudo, Joueur_2_lettre)]
    tour: int = 0
    while True:
        joueur_nom: str
        jeton: str
        # Système d'alternance des joueurs :
        # - joueurs est une liste de tuples [(Joueur_1_pseudo, "J"), (Joueur_2_pseudo, "R")]
        # - tour % 2 donne 0 ou 1 en alternance à chaque tour
        # - joueurs[0 ou 1] sélectionne le bon tuple (pseudo, lettre)
        # - joueur_nom, jeton = (...) décompose le tuple en deux variables
        joueur_nom, jeton = joueurs[tour % 2] # Alterne entre les deux joueurs
        print(f"\nC'est au tour de {joueur_nom} ({jeton})...")
        time.sleep(1)
        col: int = demander_colonne(grille, joueur_nom)
        placer_jeton(grille, col, jeton)  # Place le jeton dans la colonne choisie
        print(f"{joueur_nom} place son jeton en colonne {col+1}.")
        time.sleep(0.7)
        afficher_grille(grille)
        time.sleep(0.5)
        if est_gagnant(grille, jeton):
            print(f"Bravo, {joueur_nom} a gagné !")
            time.sleep(1)
            break
        if grille_pleine(grille):
            print("Match nul !")
            time.sleep(1)
            break
        tour += 1  # Passe au joueur suivant

if __name__ == "__main__":
    jeu_puissance4()