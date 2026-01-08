# --- 1. La fonction qui note une fenêtre de 4 cases ---
def evaluer_fenetre(fenetre):
    score = 0
    
    # Pions IA (1)
    if fenetre.count(1) == 4:
        score += 10000
    elif fenetre.count(1) == 3 and fenetre.count(0) == 1:
        score += 100
    elif fenetre.count(1) == 2 and fenetre.count(0) == 2:
        score += 1

    # Pions Adversaire (2)
    if fenetre.count(2) == 4:
        score -= 10000
    elif fenetre.count(2) == 3 and fenetre.count(0) == 1:
        score -= 100
    elif fenetre.count(2) == 2 and fenetre.count(0) == 2:
        score -= 1
        
    return score

# --- 2. La fonction qui parcourt tout le plateau ---
def score_position(grille):
    score_total = 0

    # Horizontal (-)
    for l in range(0, 6):
        for c in range(0, 4):
            fenetre = [grille[l][c], grille[l][c+1], grille[l][c+2], grille[l][c+3]]
            score_total += evaluer_fenetre(fenetre)

    # Vertical (|)
    for l in range(0, 3):
        for c in range(0, 7):
            fenetre = [grille[l][c], grille[l+1][c], grille[l+2][c], grille[l+3][c]]
            score_total += evaluer_fenetre(fenetre)

    # Diagonale Descendante (\)
    for l in range(0, 3):
        for c in range(0, 4):
            fenetre = [grille[l][c], grille[l+1][c+1], grille[l+2][c+2], grille[l+3][c+3]]
            score_total += evaluer_fenetre(fenetre)

    # Diagonale Montante (/)
    for l in range(3, 6):
        for c in range(0, 4):
            fenetre = [grille[l][c], grille[l-1][c+1], grille[l-2][c+2], grille[l-3][c+3]]
            score_total += evaluer_fenetre(fenetre)

    return score_total

# --- 3. ZONE DE TEST ---

# On crée un plateau vide (que des 0)
plateau = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

# SCÉNARIO : L'IA (1) a 3 pions alignés horizontalement en bas à gauche
plateau[5][0] = 1
plateau[5][1] = 1
plateau[5][2] = 1
plateau[5][3] = 1
# La case plateau[5][3] est vide (0), donc ça fait "1-1-1-0"

# SCÉNARIO : L'Adversaire (2) essaie une diagonale montante (/)
plateau[5][6] = 2
plateau[4][5] = 2
plateau[3][4] = 2
# La case suivante serait vide

print("Calcul du score en cours...")
resultat = score_position(plateau)
print("Score final du plateau : ", resultat)