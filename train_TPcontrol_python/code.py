def matrice():
    # Création d'une matrice 4x10 pour stocker :
    # Ligne 0 : premiers lancers
    # Ligne 1 : deuxièmes lancers
    # Ligne 2 : scores par tour
    # Ligne 3 : scores cumulés
    lancers = [[None for _ in range(10)] for _ in range(4)]
    return lancers

def gerer_saisie(lancers):
    sup1 = 0
    sup2 = 0
    for tour in range(9):
        print(f"--- Tour {tour + 1} ---")
        while True:
            try:
                lancer1 = int(input("Le score du premier lancé (0-10): "))
                if 0 <= lancer1 <= 10:
                    break
                else:
                    print("Erreur: Le score doit être entre 0 et 10")
            except ValueError:
                print("Erreur: Veuillez entrer un nombre valide")
        
        lancers[0][tour] = lancer1
        
        if lancer1 == 10:
            print("Strike !")
            lancers[1][tour] = None # Pas de 2ème lancer pour un strike (sauf tour 10)
        else:
            while True:
                try:
                    lancer2 = int(input("Saisir le score du deuxième lancé: "))
                    if 0 <= lancer2 <= (10 - lancer1):
                        break
                    else:
                        print(f"Erreur: Le score doit être entre 0 et {10 - lancer1}")
                except ValueError:
                    print("Erreur: Veuillez entrer un nombre valide")
            
            lancers[1][tour] = lancer2
            if lancer1 + lancer2 == 10:
                print("Spare !")
    
    print("--- Tour 10 ---")
    tour = 9
    while True:
        try:
            lancer1 = int(input("Saisir le score du premier lancé (0-10): "))
            if 0 <= lancer1 <= 10:
                break
            else:
                print("Erreur: Le score doit être entre 0 et 10")
        except ValueError:
            print("Erreur: Veuillez entrer un nombre valide")
    
    lancers[0][tour] = lancer1
    
    if lancer1 == 10: # Strike au 1er lancer du tour 10
        print("Strike ! Vous avez 2 lancers supplémentaires.")
        lancers[1][tour] = None
        while True:
            try:
                sup1 = int(input("Lancer supplémentaire 1 (0-10): "))
                if 0 <= sup1 <= 10:
                    break
                else:
                    print("Erreur: Le score doit être entre 0 et 10")
            except ValueError:
                print("Erreur: Veuillez entrer un nombre valide")
        
        while True:
            try:
                sup2 = int(input("Lancer supplémentaire 2 (0-10): "))
                if 0 <= sup2 <= 10:
                    break
                else:
                    print("Erreur: Le score doit être entre 0 et 10")
            except ValueError:
                print("Erreur: Veuillez entrer un nombre valide")
    
    else: # Pas de strike au 1er lancer
        max_pins_lancer2 = 10 - lancer1
        while True:
            try:
                lancer2 = int(input(f"Saisir le score du deuxième lancé (0-{max_pins_lancer2}): "))
                if 0 <= lancer2 <= max_pins_lancer2:
                    break
                else:
                    print(f"Erreur: Le score doit être entre 0 et {max_pins_lancer2}")
            except ValueError:
                print("Erreur: Veuillez entrer un nombre valide")
        
        lancers[1][tour] = lancer2
        
        if lancer1 + lancer2 == 10: # Spare au tour 10
            print("Spare ! Vous avez 1 lancer supplémentaire.")
            while True:
                try:
                    sup1 = int(input("Lancer supplémentaire (0-10): "))
                    if 0 <= sup1 <= 10:
                        break
                    else:
                        print("Erreur: Le score doit être entre 0 et 10")
                except ValueError:
                    print("Erreur: Veuillez entrer un nombre valide")
            # sup2 reste 0
        
        else: # Tour "ouvert" (Open frame)
            print("Tour terminé.")
            # sup1 et sup2 restent 0
            
    return sup1, sup2

def calculer_scores(lancers, sup1, sup2):
    score_cumule = 0
    for tour in range(10):
        score_tour = 0
        lancer1 = lancers[0][tour]
        lancer2 = lancers[1][tour]
        
        if tour == 9:
            if lancer1 == 10: # Strike
                score_tour = 10 + sup1 + sup2
            elif lancer1 + (lancer2 or 0) == 10: # Spare
                score_tour = 10 + sup1
            else: # Open
                score_tour = lancer1 + (lancer2 or 0)
        else:
            if lancer1 == 10: # Strike
                score_tour = 10
                bonus1 = lancers[0][tour + 1]
                
                if bonus1 == 10:
                    if tour == 8:
                        bonus2 = sup1
                    else:
                        bonus2 = lancers[0][tour + 2]
                else:
                    bonus2 = lancers[1][tour + 1]
            
                score_tour += bonus1 + (bonus2 or 0)
                
            elif lancer1 + (lancer2 or 0) == 10: # Spare
                score_tour = 10
                bonus1 = lancers[0][tour + 1]
                score_tour += bonus1
                
            else: # Open
                score_tour = lancer1 + (lancer2 or 0)
        
        lancers[2][tour] = score_tour
        score_cumule += score_tour
        lancers[3][tour] = score_cumule
    
    return lancers

def valider_score(score, max_score=10):
    try:
        score = int(score)
        if 0 <= score <= max_score:
            return score
        else:
            return None
    except ValueError:
        return None

def afficher_scores(lancers):
    print("\nMatrice des lancers et scores :")
    print("Premiers lancers:", lancers[0])
    print("Deuxièmes lancers:", lancers[1])
    print("Scores par tour:", lancers[2])
    print("Scores cumulés:", lancers[3])

def main():
    print("Bienvenue au jeu de bowling!")
    lancers = matrice()
    sup1, sup2 = gerer_saisie(lancers)
    lancers = calculer_scores(lancers, sup1, sup2)
    afficher_scores(lancers)
    print(f"\nScore final : {lancers[3][9]}")

if __name__ == "__main__":
    main()
