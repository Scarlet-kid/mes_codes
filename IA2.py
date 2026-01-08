import math
import random

# ==========================================
# 1. LES OUTILS (A NE PAS TOUCHER)
# ==========================================

def colonnes_valides(grille):
    """Renvoie la liste des colonnes non pleines"""
    # On suppose que 0 est la case vide
    return [c for c in range(7) if grille[0][c] == 0]

def chercher_ligne_vide(grille, col):
    """Trouve la première case vide en partant du bas"""
    for l in range(5, -1, -1):
        if grille[l][col] == 0:
            return l
    return None

# ==========================================
# 2. L'EVALUATION (Adaptée à ta couleur)
# ==========================================

def evaluer_fenetre(fenetre, p_ia, p_adv):
    score = 0
    
    # --- BONUS : Mes pions (p_ia) ---
    if fenetre.count(p_ia) == 4:
        score += 10000
    elif fenetre.count(p_ia) == 3 and fenetre.count(0) == 1:
        score += 100
    elif fenetre.count(p_ia) == 2 and fenetre.count(0) == 2:
        score += 1

    # --- MALUS : Pions adverses (p_adv) ---
    if fenetre.count(p_adv) == 4:
        score -= 10000
    elif fenetre.count(p_adv) == 3 and fenetre.count(0) == 1:
        score -= 100
    elif fenetre.count(p_adv) == 2 and fenetre.count(0) == 2:
        score -= 1
        
    return score

def score_position(grille, p_ia, p_adv):
    score_total = 0
    
    # On scanne tout le plateau
    
    # Horizontal
    for l in range(6):
        for c in range(4):
            fenetre = [grille[l][c], grille[l][c+1], grille[l][c+2], grille[l][c+3]]
            score_total += evaluer_fenetre(fenetre, p_ia, p_adv)
    # Vertical
    for l in range(3):
        for c in range(7):
            fenetre = [grille[l][c], grille[l+1][c], grille[l+2][c], grille[l+3][c]]
            score_total += evaluer_fenetre(fenetre, p_ia, p_adv)
    # Diagonale Descendante
    for l in range(3):
        for c in range(4):
            fenetre = [grille[l][c], grille[l+1][c+1], grille[l+2][c+2], grille[l+3][c+3]]
            score_total += evaluer_fenetre(fenetre, p_ia, p_adv)
    # Diagonale Montante
    for l in range(3, 6):
        for c in range(4):
            fenetre = [grille[l][c], grille[l-1][c+1], grille[l-2][c+2], grille[l-3][c+3]]
            score_total += evaluer_fenetre(fenetre, p_ia, p_adv)
            
    return score_total

# ==========================================
# 3. LE MINIMAX (Cerveau)
# ==========================================

def minimax(grille, profondeur, is_maximizing, p_ia, p_adv):
    # On calcule le score par rapport à MOI (p_ia)
    score_actuel = score_position(grille, p_ia, p_adv)
    
    # Arrêt : Victoire, Défaite ou Profondeur 0
    if profondeur == 0 or score_actuel >= 5000 or score_actuel <= -5000:
        return score_actuel
    
    cols = colonnes_valides(grille)
    if not cols: return 0 # Match nul

    if is_maximizing: # C'est mon tour, je veux le meilleur score
        max_eval = -math.inf
        for c in cols:
            l = chercher_ligne_vide(grille, c)
            grille[l][c] = p_ia
            eval = minimax(grille, profondeur - 1, False, p_ia, p_adv)
            grille[l][c] = 0 # Annuler le coup
            max_eval = max(max_eval, eval)
        return max_eval
        
    else: # C'est le tour de l'adversaire, il veut le pire score pour moi
        min_eval = math.inf
        for c in cols:
            l = chercher_ligne_vide(grille, c)
            grille[l][c] = p_adv
            eval = minimax(grille, profondeur - 1, True, p_ia, p_adv)
            grille[l][c] = 0 # Annuler le coup
            min_eval = min(min_eval, eval)
        return min_eval

# ==========================================
# 4. LA FONCTION PRINCIPALE (A appeler par le moteur)
# ==========================================

def jouer(grille, couleur_bot):
    """
    C'est cette fonction que le moteur du prof va appeler.
    Elle reçoit la grille et TA couleur (1 ou 2).
    Elle doit renvoyer le numéro de la colonne (0 à 6).
    """
    
    # 1. On détermine qui est l'adversaire
    if couleur_bot == 1:
        couleur_adv = 2
    else:
        couleur_adv = 1
        
    # 2. On prépare le Minimax
    meilleur_score = -math.inf
    # Par sécurité, on choisit une colonne valide au hasard au cas où
    possibles = colonnes_valides(grille)
    meilleure_col = random.choice(possibles) 
    
    PROFONDEUR = 4 # Tu peux changer ça (3 c'est rapide, 5 c'est lent mais fort)

    # 3. On teste chaque colonne
    for c in possibles:
        l = chercher_ligne_vide(grille, c)
        
        # On simule le coup
        grille[l][c] = couleur_bot
        
        # On lance minimax (prochain tour = adversaire, donc False)
        score = minimax(grille, PROFONDEUR, False, couleur_bot, couleur_adv)
        
        # On annule le coup
        grille[l][c] = 0
        
        if score > meilleur_score:
            meilleur_score = score
            meilleure_col = c
            
    return meilleure_col