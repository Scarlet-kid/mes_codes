from copy import deepcopy

def placer(p: dict, j: dict, c: int) -> int:
    """Place un pion dans la colonne c"""
    if 0 <= c < 7:  # Colonne valide
        l = 0  # On commence par la ligne tout en bas
        ok = False
        while not ok and l < 6:  # Cherche la première case vide
            if p["grille"][l][c] == 0:  # Case vide ?
                p["grille"][l][c] = j["num"]  # Place le pion
                ok = True
            else:
                l = l + 1  # Monte d'une ligne
        if ok:
            return l  # Retourne la ligne où le jeton a été placé
        else:
            return -1  # Colonne pleine
    else:
        return -1  # Colonne invalide


def cbIdemDir(p: dict, v: int, l: int, c: int, dl: int, dc: int) -> int:
    """
    Compte pions identiques dans une direction
    v = valeur cherchée (1 ou 2)
    l,c = position actuelle
    dl,dc = direction (ex: dl=0,dc=1 = droite)
    """
    if -1 < l + dl < 6 and -1 < c + dc < 7:  # Case suivante existe ?
        if p["grille"][l + dl][c + dc] == v:  # Même pion ?
            return 1 + cbIdemDir(p, v, l + dl, c + dc, dl, dc)  # Continue
        else:
            return 0  # Pion différent ou vide
    return 0  # Hors grille


def testerVictoire(p, v, l, c):
    """Teste si le coup crée un alignement de 4 pions"""
    # Horizontal
    compteur = cbIdemDir(p, v, l, c, 0, -1) + cbIdemDir(p, v, l, c, 0, 1)
    if compteur > 2:
        p["gagnant"] = v
    
    # Vertical
    compteur = cbIdemDir(p, v, l, c, -1, 0) + cbIdemDir(p, v, l, c, 1, 0)
    if compteur > 2:
        p["gagnant"] = v
    
    # Diagonale montante
    compteur = cbIdemDir(p, v, l, c, 1, -1) + cbIdemDir(p, v, l, c, -1, 1)
    if compteur > 2:
        p["gagnant"] = v
    
    # Diagonale descendante.
    compteur = cbIdemDir(p, v, l, c, 1, 1) + cbIdemDir(p, v, l, c, -1, -1)
    if compteur > 2:
        p["gagnant"] = v

def colonnes_jouables(grille: list[list[int]]) -> list[int]:
    """
    Retourne les colonnes jouables, triées par priorité stratégique
    Ordre : centre d'abord (3), puis adjacents (2,4), puis bords
    """
    ordre = [3, 2, 4, 1, 5, 0, 6]
    return [c for c in ordre if grille[5][c] == 0]

def evaluer(partie: dict, moi: int) -> int:
    """
    Évalue le plateau selon plusieurs critères :
    - Victoire : +100000 / Défaite : -100000
    - Contrôle centre : +10 par pion
    - Alignements de 2 : +5
    - Alignements de 3 : +50 (moi) / -80 (adversaire)
    """
    grille = partie["grille"]
    adv = 3 - moi
    
    # Cas terminaux
    if partie.get("gagnant") == moi:
        return 100000  # Victoire
    if partie.get("gagnant") == adv:
        return -100000  # Défaite
    if all(grille[5][c] != 0 for c in range(7)):
        return 0  # Égalité (grille pleine)

    score = 0

    # CRITÈRE 1 : Bonus centre (colonne 3)
    for lig in range(6):
        if grille[lig][3] == moi:
            score += 10
        elif grille[lig][3] == adv:
            score -= 10
    
    # CRITÈRE 2 : Alignements horizontaux
    for i in range(6):
        for j in range(5):
            # Alignements de 2
            if grille[i][j] == moi and grille[i][j+1] == moi:
                score += 5
            if grille[i][j] == adv and grille[i][j+1] == adv:
                score -= 6
            
            # Alignements de 3
            if j < 4:
                if grille[i][j] == moi and grille[i][j+1] == moi and grille[i][j+2] == moi:
                    score += 50
                if grille[i][j] == adv and grille[i][j+1] == adv and grille[i][j+2] == adv:
                    score -= 80
    
    return score

# ALGORITHME MINIMAX AVEC ELAGAGE ALPHA-BETA

def minimax(partie: dict, profondeur: int, maximise: bool, moi: int, alpha: int, beta: int) -> int:
    """
    Algorithme Minimax avec élagage Alpha-Bêta
    
    Args:
        partie: État du jeu
        profondeur: Nombre de coups à explorer en avance
        maximise: True si c'est mon tour, False si adversaire
        moi: Mon numéro de joueur
        alpha: Meilleur score garanti pour le maximiseur
        beta: Meilleur score garanti pour le minimiseur
    
    Returns:
        Score de la position
    """
    adv = 3 - moi
    coups = colonnes_jouables(partie["grille"])
    
    # Conditions d'arrêt
    if profondeur == 0 or not coups or partie.get("gagnant", 0) != 0:
        return evaluer(partie, moi)
    
    if maximise:
        # Tour du maximiseur (moi)
        score_max = -999999
        
        for col in coups:
            p_copie = deepcopy(partie)
            p_copie["gagnant"] = 0
            lig = placer(p_copie, p_copie[moi], col)
            
            if lig >= 0:
                testerVictoire(p_copie, moi, lig, col)
                score = minimax(p_copie, profondeur - 1, False, moi, alpha, beta)
                score_max = max(score_max, score)
                alpha = max(alpha, score_max)
                
                # Élagage Alpha-Beta
                if alpha >= beta:
                    break  # Coupe Beta
        
        return score_max
    
    else:
        # Tour du minimiseur (adversaire)
        score_min = 999999
        
        for col in coups:
            p_copie = deepcopy(partie)
            p_copie["gagnant"] = 0
            lig = placer(p_copie, p_copie[adv], col)
            
            if lig >= 0:
                testerVictoire(p_copie, adv, lig, col)
                score = minimax(p_copie, profondeur - 1, True, moi, alpha, beta)
                score_min = min(score_min, score)
                beta = min(beta, score_min)
                
                # Élagage Alpha-Beta
                if alpha >= beta:
                    break  # Coupe Alpha
        
        return score_min

def choix(partie: dict) -> int:
    """
    Fonction appelée par le moteur
    
    Stratégie en 3 phases :
    1. Victoire immédiate ? → Jouer
    2. Bloquer victoire adverse ? → Bloquer
    3. Sinon → Minimax (profondeur 3)
    """
    moi = partie["tourDe"]
    adv = 3 - moi
    coups = colonnes_jouables(partie["grille"])
    
    if not coups:
        return 0  # Toutes les colonnes sont pleines (égalité)
    
    # PHASE 1 : Gagner immédiatement ?
    for col in coups:
        p_test = deepcopy(partie)
        p_test["gagnant"] = 0
        lig = placer(p_test, p_test[moi], col)
        
        if lig >= 0:
            testerVictoire(p_test, moi, lig, col)
            if p_test["gagnant"] == moi:
                return col  # Jouer là où il y a 3 pions alignés pour gagner
    
    # PHASE 2 : Bloquer l'adversaire ?
    for col in coups:
        p_test = deepcopy(partie)
        p_test["gagnant"] = 0
        lig = placer(p_test, p_test[adv], col)
        
        if lig >= 0:
            testerVictoire(p_test, adv, lig, col)
            if p_test["gagnant"] == adv:
                return col  # Bloquer l'adversaire si 3 jetons alignés
    
    # PHASE 3 : Minimax - cherche meilleur coup
    meilleur_col = coups[0]  # Par défaut la première colonne jouable
    meilleur_score = -999999  # Score très bas au départ
    
    for col in coups:
        p_test = deepcopy(partie)
        p_test["gagnant"] = 0
        lig = placer(p_test, p_test[moi], col)
        
        if lig >= 0:
            testerVictoire(p_test, moi, lig, col)
            
            # Simule 3 coups à l'avance
            score = minimax(p_test, 3, False, moi, -999999, 999999)
            # Profondeur : 3
            # False : tour adversaire ensuite
            # Alpha-Beta : -999999 et 999999
            
            if score > meilleur_score:
                meilleur_score = score
                meilleur_col = col  # Retiens cette colonne
    
    return meilleur_col  # Joue le meilleur coup trouvé