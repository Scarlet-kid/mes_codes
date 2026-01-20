import time
from copy import deepcopy

import IA1
import IA2

def creationPartie()->dict:
    partie : dict = {}
    grille : list[list[int]]= []
    for i in range(6):
        grille.append([])
        for _ in range(7):
            grille[i].append(0)
    partie["grille"] = grille
    partie[1] = {"nom":"J1","couleur":"jaune","nbPion":21,"num":1}
    partie[2] = {"nom":"J2","couleur":"rouge","nbPion":21,"num":2}
    partie["gagnant"] = 0
    partie["tourDe"] = 1
    partie["dernierCoup"] = None
    partie["bad"] = 0
    return partie


def permuterJoueur(p:dict):
    if  p["tourDe"] == 1:
        p["tourDe"] = 2
    else:
        p["tourDe"] = 1


def placer(p:dict,j:dict,c:int)->int:
    if 0<=c<7:
        l = 0
        ok = False
        while not ok and l<6:
            if p["grille"][l][c] == 0:
                p["grille"][l][c]=j["num"]
                ok = True
            else:
                l=l+1
        if ok:
            return l
        else :
            return -1
    else :
        return -1


def cbIdemDir(p:dict,v:int,l:int,c:int,dl:int,dc:int)->int:
    if -1<l+dl<6 and -1<c+dc<7 :
        if p["grille"][l+dl][c+dc]== v:
            return 1+cbIdemDir(p,v,l+dl,c+dc,dl,dc)
        else :
            return 0
    return 0


def testerVictoire(p,v,l,c):
    compteur = cbIdemDir(p,v,l,c,0,-1)+cbIdemDir(p,v,l,c,0,1)
    if compteur>2:
        p["gagnant"]=v

    compteur = cbIdemDir(p,v,l,c,-1,0)+cbIdemDir(p,v,l,c,1,0)
    if compteur>2:
        p["gagnant"]=v

    compteur = cbIdemDir(p,v,l,c,1,-1)+cbIdemDir(p,v,l,c,-1,1)
    if compteur>2:
        p["gagnant"]=v

    compteur = cbIdemDir(p,v,l,c,1,1)+cbIdemDir(p,v,l,c,-1,-1)
    if compteur>2:
        p["gagnant"]=v


def colonnes_jouables(grille):
    return [c for c in range(7) if grille[5][c] == 0]


def calculer_scores(p):
    if p["gagnant"] == 1:
        return 1 + p[1]["nbPion"], 0
    if p["gagnant"] == 2:
        return 0, 1 + p[2]["nbPion"]
    return 0, 0


def jouer_match(choix_j1, choix_j2):
    p = creationPartie()

    temps_j1 = []
    temps_j2 = []
    coups = 0

    while p["gagnant"] == 0 and coups < 42:
        if not colonnes_jouables(p["grille"]):
            break

        p_saved = deepcopy(p)

        debut = time.perf_counter()
        if p["tourDe"] == 1:
            col = choix_j1(p_saved)
        else:
            col = choix_j2(p_saved)
        fin = time.perf_counter()

        if p["tourDe"] == 1:
            temps_j1.append((fin - debut) * 1000)
        else:
            temps_j2.append((fin - debut) * 1000)

        lig = placer(p, p[p["tourDe"]], col)
        if lig < 0:
            p["gagnant"] = 2 if p["tourDe"] == 1 else 1
            break

        p[p["tourDe"]]["nbPion"] -= 1
        testerVictoire(p, p[p["tourDe"]]["num"], lig, col)
        permuterJoueur(p)
        coups += 1

    s1, s2 = calculer_scores(p)
    return p["gagnant"], coups, temps_j1, temps_j2, s1, s2


def serie(nb_matchs=10):
    # Si nombre impair, on ajoute 1
    if nb_matchs % 2 != 0:
        print("Nombre impair → arrondi au supérieur")
        nb_matchs += 1

    print(f"\nTests : {nb_matchs} matchs (IA1 vs IA2)")
    print("=" * 60)

    # Compteurs de victoires
    victoires_ia1 = 0
    victoires_ia2 = 0
    egalites = 0
    
    # Listes pour les temps
    temps_ia1 = []
    temps_ia2 = []
    
    # Scores totaux
    score_ia1 = 0
    score_ia2 = 0

    # Jouer tous les matchs
    for i in range(nb_matchs):
        # Première moitié : IA1 commence
        if i < nb_matchs // 2:
            gagnant, coups, t1, t2, s1, s2 = jouer_match(IA1.choix, IA2.choix)
            commence = "IA1 commence"
        # Deuxième moitié : IA2 commence
        else:
            gagnant, coups, t2, t1, s2, s1 = jouer_match(IA2.choix, IA1.choix)
            commence = "IA2 commence"
            # Inverser le gagnant car les rôles sont inversés
            if gagnant == 1:
                gagnant = 2
            elif gagnant == 2:
                gagnant = 1

        # Ajouter les temps
        temps_ia1 += t1
        temps_ia2 += t2
        
        # Ajouter les scores
        score_ia1 += s1
        score_ia2 += s2

        # Compter les victoires
        if gagnant == 1:
            victoires_ia1 += 1
            resultat = "IA1 gagne"
        elif gagnant == 2:
            victoires_ia2 += 1
            resultat = "IA2 gagne"
        else:
            egalites += 1
            resultat = "Égalité"

        # Afficher le résultat du match
        print(f"Match {i+1:02d} [{commence}] → {resultat} en {coups} coups | score IA1={s1} IA2={s2}")

    # Affichage final
    print("\n" + "=" * 60)
    print("RÉSULTATS FINAUX")
    print("=" * 60)
    print(f"IA1 : {victoires_ia1}/{nb_matchs}")
    print(f"IA2 : {victoires_ia2}/{nb_matchs}")
    print(f"Égalités : {egalites}")

    print("\n--- TEMPS DE CALCUL ---")
    moyenne_ia1 = sum(temps_ia1) / len(temps_ia1)
    max_ia1 = max(temps_ia1)
    moyenne_ia2 = sum(temps_ia2) / len(temps_ia2)
    max_ia2 = max(temps_ia2)
    print(f"IA1 : moy {moyenne_ia1:.2f} ms | max {max_ia1:.2f} ms")
    print(f"IA2 : moy {moyenne_ia2:.2f} ms | max {max_ia2:.2f} ms")

    print("\n--- SCORE ---")
    print(f"Score total IA1 : {score_ia1}")
    print(f"Score total IA2 : {score_ia2}")
    print("=" * 60)


if __name__ == "__main__":
    n = input("Nombre de matchs (pair, défaut 10) : ").strip()
    serie(10 if n == "" else int(n))