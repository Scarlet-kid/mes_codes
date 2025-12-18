"""
Jeu Puissance 4 avec interface graphique Pygame
Chaque joueur clique sur une colonne pour placer son jeton. 
Le premier à aligner 4 jetons gagne.
"""

import pygame  # Bibliothèque pour l'affichage graphique
import sys     # Pour quitter le programme

# ---- Constantes ----
LIGNES: int = 6      # Nombre de lignes de la grille
COLONNES: int = 7   # Nombre de colonnes de la grille
TAILLE_CASE: int = 40  # Taille d'une case en pixels
RAYON: int = TAILLE_CASE // 2 - 5  # Rayon du jeton
LARGEUR: int = COLONNES * TAILLE_CASE  # Largeur de la fenêtre
HAUTEUR: int = (LIGNES + 1) * TAILLE_CASE  # Hauteur de la fenêtre (+1 pour la zone du joueur)
TAILLE_FENETRE: tuple[int, int] = (LARGEUR, HAUTEUR)

# Couleurs utilisées
BLEU: tuple[int, int, int] = (0, 0, 255)
NOIR: tuple[int, int, int] = (0, 0, 0)
ROUGE: tuple[int, int, int] = (255, 0, 0)
JAUNE: tuple[int, int, int] = (255, 255, 0)

# ---- Fonctions ----
def creer_grille() -> list[list[str]]:
    # Crée et retourne une grille vide (6 lignes x 7 colonnes)
    # Utilisation : grille = creer_grille()
    return [[" " for _ in range(COLONNES)] for _ in range(LIGNES)] # _ par convention vu qu'on a pas l'intention d'utiliser les valeurs des indices.
    """
    Crée une grille vide (liste de listes) de 6 lignes et 7 colonnes
    Chaque case contient " " (vide)
    """

def jouer_coup(grille: list[list[str]], colonne: int, pion: str) -> int | None:
    # Place le jeton ("Rouge" ou "Jaune") dans la colonne choisie
    # Le jeton tombe dans la première case libre en partant du bas
    # Retourne l'indice de la ligne où le jeton est placé, ou None si la colonne est pleine
    # Utilisation : ligne = jouer_coup(grille, colonne, pion)
    for i in range(LIGNES-1, -1, -1):
        if grille[i][colonne] == " ":
            grille[i][colonne] = pion
            return i  # retourne la ligne où le pion a été placé
    return None  # colonne pleine
    """
    Place le jeton du joueur dans la colonne choisie
    Le jeton tombe dans la première case libre en partant du bas
    Retourne la ligne où le jeton est placé, ou None si la colonne est pleine
    """

def verifier_victoire(grille: list[list[str]], pion: str) -> bool:
    # Vérifie si le joueur a gagné (4 jetons alignés)
    # Teste toutes les directions : horizontal, vertical, diagonales
    # Retourne True si le joueur a gagné, False sinon
    # Utilisation : if verifier_victoire(grille, pion): ...
    # Horizontal
    for i in range(LIGNES):
        for j in range(COLONNES-3):
            if all(grille[i][j+k] == pion for k in range(4)):
                return True
    # Vertical
    for i in range(LIGNES-3):
        for j in range(COLONNES):
            if all(grille[i+k][j] == pion for k in range(4)):
                return True
    # Diagonale /
    for i in range(3, LIGNES):
        for j in range(COLONNES-3):
            if all(grille[i-k][j+k] == pion for k in range(4)):
                return True
    # Diagonale \
    for i in range(LIGNES-3):
        for j in range(COLONNES-3):
            if all(grille[i+k][j+k] == pion for k in range(4)):
                return True
    return False
    """
    Vérifie si le joueur a gagné (4 jetons alignés)
    Teste toutes les directions : horizontal, vertical, diagonales
    Retourne True si victoire, False sinon
    """

def dessiner_grille(grille: list[list[str]], screen: pygame.Surface) -> None:
    # Dessine la grille et les jetons sur la fenêtre Pygame
    # Les cases vides sont noires, les jetons sont colorés
    # Utilisation : dessiner_grille(grille, screen)
    for c in range(COLONNES):
        for r in range(LIGNES):
            # Dessine le fond bleu de la case (x, y, largeur, hauteur)
            pygame.draw.rect(screen, BLEU, (c*TAILLE_CASE, (r+1)*TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))
            couleur = NOIR
            if grille[r][c] == "Rouge":
                couleur = ROUGE
            elif grille[r][c] == "Jaune":
                couleur = JAUNE
            # Calcul des coordonnées du centre du cercle (jeton)
            pygame.draw.circle(screen, couleur, (c * TAILLE_CASE + TAILLE_CASE // 2, (r + 1) * TAILLE_CASE + TAILLE_CASE // 2), RAYON)
            # Coordonnées (x,y) du centre du cercle : (c*TAILLE_CASE + TAILLE_CASE//2, (r+1)*TAILLE_CASE + TAILLE_CASE//2) en pixels
    pygame.display.update() # Pour mettre a jour l'affichage des cercles dans notre interface
    """
    Dessine la grille et les jetons sur la fenêtre Pygame
    Les cases vides sont noires, les jetons sont colorés
    """

# ---- Main ----
def main() -> None:
    # Fonction principale du jeu
    # Initialise la fenêtre, la grille et gère la boucle de jeu
    # Utilisation : main() (appelée automatiquement si le fichier est exécuté)
    pygame.init()
    screen = pygame.display.set_mode(TAILLE_FENETRE) # Notre fenetre de jeu
    pygame.display.set_caption("Puissance 4") # le titre de la fenetre
    font = pygame.font.SysFont("monospace", 20) # La police d'écriture.
    grille = creer_grille()
    game_over = False          
    joueur = "Rouge" # Le joueur appelé a commencer la partie.
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Ferme proprement Pygame (libère la fenêtre, l'audio, etc.)
                pygame.quit()
                # Demande à Python de terminer le programme immédiatement
                # (lève SystemExit). On appelle sys.exit() après pygame.quit() pour
                # s'assurer que les ressources Pygame sont bien libérées d'abord.
                sys.exit()
            if event.type == pygame.MOUSEMOTION: # evénement lié au déplacement de la souris.
                # Affiche le pion au dessus pour voir où il tombera
                screen.fill(NOIR, rect=(0,0,LARGEUR, TAILLE_CASE)) # Donne la couleur noire au niveau de la bande d'indication.0,0 pour le coin supérieur gauche.
                # LARGEUR pour que ca occupe toute la première ligne puisque LARGEUR = COLONNES * TAILLE_CASE
                # hauteur = TAILLE_CASE → hauteur d'une case (on réserve la première "ligne" en haut pour l'indicateur).
                posx = event.pos[0] # stocke donc la position horizontale de la souris dans la variable 
                couleur = ROUGE if joueur == "Rouge" else JAUNE
                pygame.draw.circle(screen, couleur, (posx, TAILLE_CASE//2), RAYON) # sert à dessiner l'aperçu du jeton au-dessus de la grille : la valeur est en pixels depuis le bord gauche de la fenêtre. 
                pygame.display.update() # Mise à jour.
            if event.type == pygame.MOUSEBUTTONDOWN: # Déclenché lors d'un clic
                # Efface la zone d'indication en haut pour faire disparaître l'aperçu
                screen.fill(NOIR, rect=(0, 0, LARGEUR, TAILLE_CASE)) # Fait apparaitre un rectangle.
                # Calcule la colonne cliquée (x en pixels → numéro de colonne)
                colonne = event.pos[0] // TAILLE_CASE  # Le numéro de la colonne.
                # Vérification de sécurité : éviter les clics hors colonnes
                if colonne < 0 or colonne >= COLONNES:
                    continue

                # Place le jeton dans la grille (si la colonne n'est pas pleine)
                ligne = jouer_coup(grille, colonne, joueur)
                if ligne is not None:
                    # Redessine immédiatement la grille pour que le jeton apparaisse
                    dessiner_grille(grille, screen)

                    # Vérifie la victoire après placement
                    if verifier_victoire(grille, joueur):
                        screen.fill(NOIR)
                        text = font.render(f"Joueur {joueur} gagne!", True, ROUGE if joueur=="Rouge" else JAUNE)
                        screen.blit(text, (10, HAUTEUR//2 - 10))
                        pygame.display.update()
                        pygame.time.wait(5000)
                        game_over = True
                    # Change de joueur
                    joueur = "Jaune" if joueur == "Rouge" else "Rouge"
        dessiner_grille(grille, screen)
    """
    Fonction principale du jeu
    Initialise la fenêtre, la grille et gère la boucle de jeu
    """

# Lancement du jeu si le fichier est exécuté directement
if __name__ == "__main__":
    main()