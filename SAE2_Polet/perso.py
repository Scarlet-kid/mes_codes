from copy import deepcopy

def placer(p: dict, j: dict, c: int) -> int:
    if 0 <= c < 7:
        l = 0
        ok = False
        while not ok and l < 6:
            if p["grille"][l][c] == 0:
                p["grille"][l][c] = j["num"]
                ok = True
            else:
                l = l + 1
        if ok:
            return l # Ligne ou le jeton a été placé
        else:
            return -1 # Colonne pleine 
    else:
        return -1 # Grille pleine

def cbIdemDir(p: dict, v: int, l: int, c: int, dl: int, dc: int) -> int:  #Nombre de pion aligné dans une meme direction.
    """Compte les pions dans une direction"""
    if -1 < l + dl < 6 and -1 < c + dc < 7: #Si on est dans la grille.
        if p["grille"][l + dl][c + dc] == v: # La case suivante a t'elle le meme pion ?
            return 1 + cbIdemDir(p, v, l + dl, c + dc, dl, dc) # Oui on fait +1, 
        else:
            return 0 # Non on arrete pas le meme pion
    return 0 # Hors grille

def testerVictoire(p, v, l, c): # Voit si le dernier coup joué cree un alignement de 4 pion
    compteur = cbIdemDir(p, v, l, c, 0, -1) + cbIdemDir(p, v, l, c, 0, 1) #L' horizontal.
    if compteur > 2: #En plus du pion courant on an plus de deux pion a coté : victoire
        p["gagnant"] = v # Gagnant prend la valeur du joueur qui a gagné un ou deux
    compteur = cbIdemDir(p, v, l, c, -1, 0) + cbIdemDir(p, v, l, c, 1, 0) # On va en arriere on va en avant on reste sur la meme colonne(la verticale).
    if compteur > 2:
        p["gagnant"] = v
    compteur = cbIdemDir(p, v, l, c, 1, -1) + cbIdemDir(p, v, l, c, -1, 1) #diagonale haut-gauche et diagonale bas-droite
    if compteur > 2:
        p["gagnant"] = v
    compteur = cbIdemDir(p, v, l, c, 1, 1) + cbIdemDir(p, v, l, c, -1, -1) #diagonale haut-droite et diagonale bas-gauche
    if compteur > 2:
        p["gagnant"] = v

def colonnes_jouables(grille):
    """Retourne les colonnes pas pleines"""
    return [c for c in range(7) if grille[5][c] == 0] #OK

def coup_gagnant(partie, col, joueur):
    grille = partie["grille"]
    lig = -1
    for l in range(6):
        if grille[l][col] == 0:
            lig = l
            break

    if lig == -1: 
        return False # Colonne pleine

    grille[lig][col] = joueur # On pose le pion
    p_temp = {"grille": grille, "gagnant": 0} # testerVictoire attend a recevoir un dico
    testerVictoire(p_temp, joueur, lig, col)  # testons si il y'a victoire.
    grille[lig][col] = 0               # On nettoie.
    return p_temp["gagnant"] == joueur

def coup_suicide(grille, col, moi, adv): # Si je joue la est ce que je suis mort au coup d'après ?
    # Je joue mon coup
    lig = -1
    for l in range(6):
        if grille[l][col] == 0:
            lig = l
            grille[l][col] = moi # Je pose mon pion pour de faux.modification de la vraie grille, beaucoup plus rapide.
            break

    if lig == -1:
        return True # Colonne pleine

    # L'adversaire peut-il gagner juste après ?
    for c in colonnes_jouables(grille): #On voit tous les colonnes jouables.
        for l2 in range(6):
            if grille[l2][c] == 0:
                grille[l2][c] = adv # SImulation d'un coup joué par l'adversaire.
                p = {"grille": grille, "gagnant": 0} 
                testerVictoire(p, adv, l2, c)# On voit s'il gagne, la fonction testerVictoire s'attend a recevoir un dic
                grille[l2][c] = 0 # On nettoie son coup.
                if p["gagnant"] == adv: # Si adv gagne
                    grille[lig][col] = 0 # On annule mon coup avant de partir
                    return True # C'est un coup sucide.
                break

    grille[lig][col] = 0 # On enleve mon pion 
    return False # C'est safe je perd pas.

def creer_piege(grille, col, joueur):
    lig = -1
    for l in range(6):
        if grille[l][col] == 0:
            lig = l
            break
    if lig == -1:
        return False # Colonne pleine ou grille pleine globalement.

    grille[lig][col] = joueur
    menaces = 0

    for dl, dc in [(0,1),(1,0),(1,1),(1,-1)]:
        cpt = cbIdemDir({"grille": grille}, joueur, lig, col, dl, dc) + cbIdemDir({"grille": grille}, joueur, lig, col, -dl, -dc)
        # Combien de pion ai-je aligné dans le meme sens autour de moi?
        # Un rapport car on implemente une double-menace.
        # Si dans un sens il a deux pion aligné dans la meme direction en plus du pion courant et dans l'autre sens aussi alors double menace
        if cpt == 2:
            menaces += 1

    grille[lig][col] = 0 # J'enleve mon pion.(backtracking)
    return menaces >= 2

def calculer_score_position(grille, col, joueur):
    lig = -1
    for l in range(6):
        if grille[l][col] == 0:
            lig = l
            break
    if lig == -1:
        return -999 # COlonne pleine ou grille pleine en général score tre bas ne joue pas.

    score = 0
    grille[lig][col] = joueur

    if col == 3:
        score += 40 # Centre cest top
    elif col in (2,4):
        score += 20 # a coté du centre plus ou moins top
    elif col in (1,5):
        score += 10 # a proximité des bord moins top
    else:
        score += 5 # Les bord l'un des pires scénario

    for dl, dc in [(0,1),(1,0),(1,1),(1,-1)]:
        cpt = cbIdemDir({"grille": grille}, joueur, lig, col, dl, dc) + cbIdemDir({"grille": grille}, joueur, lig, col, -dl, -dc)
        if cpt == 1: # Deux pions aligné
            score += 20
        elif cpt == 2: # Trois pions aligné 
            score += 80

    if lig <= 2:
        score += 15 # On favorise les structures basses.

    grille[lig][col] = 0 # Je nettoie mon pion
    return score

def choix(partie):
    moi = partie["tourDe"] # je regarde qui je suis pour savoir quell pion manipuler
    adv = 3 - moi
    grille = partie["grille"]
    coups = colonnes_jouables(grille)

    # 1. Je gagne
    for c in coups: # La priorité cest de gagner peut importe les risques, di je gagne la partie se termine(killshot).
        if coup_gagnant(partie, c, moi):
            return c

    # 2. Je bloque
    for c in coups: # Si l'adv peut gagner je le bloque prioritairement 
        if coup_gagnant(partie, c, adv):
            return c

    # 3. Piège sans suicide
    for c in coups: # Si je peux creer un piege sans que cela fasse gagner l'adv au second tour alors je joue dans cet optique
        if not coup_suicide(grille, c, moi, adv) and creer_piege(grille, c, moi):
            return c

    # 4. Meilleur score sans suicide
    best_col = coups[0] # Par défaut 
    best_score = -10**9 # Un très petit nombre pour commencer 

    for c in coups:
        if coup_suicide(grille, c, moi, adv):
            continue # On ignore les coups qui nous tue.
        s = calculer_score_position(grille, c, moi) # Si je peux rien faire, je calcul le coup qui me fera rapporter le plus de point et je le joue
        if s > best_score:
            best_score = s
            best_col = c

    return best_col