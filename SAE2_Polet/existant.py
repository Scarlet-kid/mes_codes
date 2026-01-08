import math
import random

# ==========================================
# 1. CONSTANTES & CONFIGURATION
# ==========================================
VIDE = 0
IA = 1        # L'ordinateur (Pion Jaune 🟡)
HUMAIN = 2    # Toi (Pion Rouge 🔴)

# Profondeur de réflexion de l'IA (plus c'est haut, plus c'est fort mais lent)
PROFONDEUR_IA = 4 

# ==========================================
# 2. FONCTIONS DE NAVIGATION (Déjà vues)
# ==========================================

def colonnes_valides(grille):
    return [c for c in range(7) if grille[0][c] == VIDE]

def chercher_ligne_vide(grille, col):
    for l in range(5, -1, -1):
        if grille[l][col] == VIDE:
            return l
    return None

# ==========================================
# 3. LE CERVEAU (Evaluation & Minimax)
# ==========================================

def evaluer_fenetre(fenetre):
    score = 0
    # IA (1) -> Veut maximiser son score
    if fenetre.count(IA) == 4:
        score += 10000
    elif fenetre.count(IA) == 3 and fenetre.count(VIDE) == 1:
        score += 100
    elif fenetre.count(IA) == 2 and fenetre.count(VIDE) == 2:
        score += 1

    # HUMAIN (2) -> L'IA déteste que tu aies des points
    if fenetre.count(HUMAIN) == 4:
        score -= 10000
    elif fenetre.count(HUMAIN) == 3 and fenetre.count(VIDE) == 1:
        score -= 100
    elif fenetre.count(HUMAIN) == 2 and fenetre.count(VIDE) == 2:
        score -= 1
        
    return score

def score_position(grille):
    score_total = 0
    # Horizontal
    for l in range(6):
        for c in range(4):
            fenetre = [grille[l][c], grille[l][c+1], grille[l][c+2], grille[l][c+3]]
            score_total += evaluer_fenetre(fenetre)
    # Vertical
    for l in range(3):
        for c in range(7):
            fenetre = [grille[l][c], grille[l+1][c], grille[l+2][c], grille[l+3][c]]
            score_total += evaluer_fenetre(fenetre)
    # Diag Descendante
    for l in range(3):
        for c in range(4):
            fenetre = [grille[l][c], grille[l+1][c+1], grille[l+2][c+2], grille[l+3][c+3]]
            score_total += evaluer_fenetre(fenetre)
    # Diag Montante
    for l in range(3, 6):
        for c in range(4):
            fenetre = [grille[l][c], grille[l-1][c+1], grille[l-2][c+2], grille[l-3][c+3]]
            score_total += evaluer_fenetre(fenetre)
    return score_total

def minimax(grille, profondeur, is_maximizing):
    score_actuel = score_position(grille)
    
    # Conditions d'arrêt
    if profondeur == 0 or score_actuel >= 5000 or score_actuel <= -5000:
        return score_actuel
    
    cols_possibles = colonnes_valides(grille)
    if not cols_possibles: return 0 # Match nul

    if is_maximizing: # Tour de l'IA
        max_eval = -math.inf
        for c in cols_possibles:
            l = chercher_ligne_vide(grille, c)
            grille[l][c] = IA
            eval = minimax(grille, profondeur - 1, False)
            grille[l][c] = VIDE
            max_eval = max(max_eval, eval)
        return max_eval
    else: # Tour de l'Humain (simulé)
        min_eval = math.inf
        for c in cols_possibles:
            l = chercher_ligne_vide(grille, c)
            grille[l][c] = HUMAIN
            eval = minimax(grille, profondeur - 1, True)
            grille[l][c] = VIDE
            min_eval = min(min_eval, eval)
        return min_eval

def meilleur_coup_ia(grille):
    meilleur_score = -math.inf
    meilleure_col = random.choice(colonnes_valides(grille)) # Choix par défaut
    
    for c in colonnes_valides(grille):
        l = chercher_ligne_vide(grille, c)
        grille[l][c] = IA
        score = minimax(grille, PROFONDEUR_IA, False)
        grille[l][c] = VIDE
        
        if score > meilleur_score:
            meilleur_score = score
            meilleure_col = c
            
    return meilleure_col

# ==========================================
# 4. INTERFACE DE JEU (NOUVEAU !)
# ==========================================

def afficher_plateau(grille):
    print("\n  0   1   2   3   4   5   6")
    print("+---+---+---+---+---+---+---+")
    for l in range(6):
        ligne_visuelle = "|"
        for c in range(7):
            if grille[l][c] == IA:
                ligne_visuelle += " 🟡|"
            elif grille[l][c] == HUMAIN:
                ligne_visuelle += " 🔴|"
            else:
                ligne_visuelle += "   |"
        print(ligne_visuelle)
        print("+---+---+---+---+---+---+---+")
    print("")

def verifier_victoire(grille):
    """Regarde si quelqu'un a gagné maintenant."""
    score = score_position(grille)
    if score >= 5000:
        return IA
    if score <= -5000:
        return HUMAIN
    return None

def lancer_jeu():
    # Création plateau vide
    plateau = [[0 for _ in range(7)] for _ in range(6)]
    tour_humain = True # L'humain commence
    
    print("=== PUISSANCE 4 : HUMAIN vs ROBOT ===")
    
    while True:
        afficher_plateau(plateau)
        
        # --- TOUR HUMAIN ---
        if tour_humain:
            try:
                col = int(input("👉 A toi (Colonne 0-6) : "))
                if col not in colonnes_valides(plateau):
                    print("❌ Colonne pleine ou invalide !")
                    continue # On redemande
            except ValueError:
                print("❌ Entre un chiffre !")
                continue

            ligne = chercher_ligne_vide(plateau, col)
            plateau[ligne][col] = HUMAIN
        
        # --- TOUR ORDI ---
        else:
            print("🤖 L'IA réfléchit...")
            col = meilleur_coup_ia(plateau)
            ligne = chercher_ligne_vide(plateau, col)
            plateau[ligne][col] = IA
            print(f"L'IA a joué colonne {col}")

        # --- VERIFICATION VICTOIRE ---
        gagnant = verifier_victoire(plateau)
        if gagnant == IA:
            afficher_plateau(plateau)
            print("💀 PERDU ! L'IA a gagné !")
            break
        elif gagnant == HUMAIN:
            afficher_plateau(plateau)
            print("🎉 BRAVO ! Tu as battu l'IA !")
            break
        elif len(colonnes_valides(plateau)) == 0:
            afficher_plateau(plateau)
            print("😐 MATCH NUL !")
            break
            
        # On change de tour
        tour_humain = not tour_humain

# ==========================================
# 5. LANCEMENT
# ==========================================
lancer_jeu()