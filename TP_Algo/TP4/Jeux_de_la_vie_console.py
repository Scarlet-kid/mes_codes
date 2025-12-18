from random import randint
def grille_vide(l:int,c:int)->list:
    grille = []
    for i in range(l):
        lst_1=[]
        for j in range(c):
            lst_1.append("0")
        grille.append(lst_1)
    return grille

def initialiser_grille(grille:list[list])->list[list]:
    nb_cellule:int =int(input("Combien de cellule voulez-vous mettre dans la grille?:"))
    for k in range(nb_cellule):
        print("cellule",k)
        cord_1=int(input("ligne:"))
        cord_2=int(input("colonne:"))
        grille[cord_1][cord_2] = "1"
        print(grille)
    #return grille

def affichage(grille:list[list]):
    for i in grille:
        print( "".join(i))


def nb_voisin(grille,x,y):
    voisins = 0
    """x = int(input("Saisir la coordonnée de la ligne dont vous voulez connaitre le nombre de voisin:"))
    y = int(input("Saisir la coordonnée de la colonne dont vous voulez connaitre le nombre de voisin:"))"""
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i == x and j == y):
                continue
            if 0 <= i < len(grille) and 0 <= j < len(grille[0]):
                if grille[i][j] == 1:
                    voisins += 1
    return voisins

def generation_suivante(grille):
    lignes = len(grille)
    colonnes = len(grille[0])
    nouvelle_grille = [[0 for _ in range(colonnes)] for _ in range(lignes)]
    for i in range(lignes):
        for j in range(colonnes):
            voisins = nb_voisin(grille, i, j)
            if grille[i][j] == 1:
                if voisins == 2 or voisins == 3:
                    nouvelle_grille[i][j] = 1
                else:
                    nouvelle_grille[i][j] = 0
            else:
                if voisins == 3:
                    nouvelle_grille[i][j] = 1
                else:
                    nouvelle_grille[i][j] = 0
    return nouvelle_grille

def affichage_2(grille):
    l = len(grille)
    c = len(grille[0])
    separateur = "+" + "+".join(["---"] * c) + "+"
    print(separateur)
    for i in range(l):
        ligne_affiche = []
        for j in range(c):
            if grille[i][j] == 1 or grille[i][j] == "1":
                ligne_affiche.append(" * ")
            else:
                ligne_affiche.append("   ")
        print("|" + "|".join(ligne_affiche) + "|")
        print(separateur)

def last():
    ligne=int(input("Saisir le nombre de ligne de la grille:"))
    colonne=int(input("Saisir le nombre de colonne de la grille:"))
    Ma_grille = grille_vide(ligne,colonne)
    initialiser_grille(Ma_grille)
    print("Voila la grille actuelle")
    print(affichage_2(Ma_grille))
    nb=int(input("Saisir le nombre de cycle de répétition:"))
    for rep in range(nb):
        print("cycle",rep)
        generation_suivante(Ma_grille)
        print(affichage_2(Ma_grille))


if __name__ == "__main__":
    """ligne=int(input("Saisir le nombre de ligne de la grille:"))
    colonne=int(input("Saisir le nombre de colonne de la grille:"))
    Ma_grille = grille_vide(ligne,colonne)
    initialiser_grille(Ma_grille)
    print(affichage_2(Ma_grille))"""
    #print(Ma_grille)
    #print(Ma_grille)
    #affichage(Ma_grille)
    #print(Ma_grille)
    #print(nb_voisin(Ma_grille))
    last()
    
            
            