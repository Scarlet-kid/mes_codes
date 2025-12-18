import turtle
import random

def creerFenetre()->turtle.Turtle:
    return turtle.Turtle()

def dessinerCarre(t:turtle.Turtle,couleur:str,x:int,y:int,taille:int):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.pencolor(couleur)
    t.forward(taille)
    t.left(90)
    t.forward(taille)
    t.left(90)
    t.forward(taille)
    t.left(90)
    t.forward(taille)
    t.left(90)
    t.penup()

def dessinerSegment(t:turtle.Turtle, couleur:str,x1:int,y1:int,x2:int,y2:int):
    t.penup()
    t.goto(x1,y1)
    t.pendown()
    t.pencolor(couleur)
    t.goto(x2,y2)
    t.penup()

def effacerTout(t:turtle.Turtle):
    t.clear()

"""tortue=creerFenetre()
tortue.speed(2)
dessinerCarre(tortue,"red",0,100,50)
dessinerSegment(tortue,"blue",50,25,200,300)"""


def placement_aleatoire(grille, n_lignes, n_colonnes):
    nb_cellules = random.randint(1, n_lignes * n_colonnes // 2)
    for _ in range(nb_cellules):
        i = random.randint(0, n_lignes - 1)
        j = random.randint(0, n_colonnes - 1)
        grille[i][j] = 1  # 1 = cellule vivante

def creerFenetre():
    fenetre = turtle.Screen()
    fenetre.title("Jeu de la vie")
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    return t

def dessinerCarre(t, couleur, x, y, taille):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(couleur)
    t.begin_fill()
    for _ in range(4):
        t.forward(taille)
        t.left(90)
    t.end_fill()
    t.penup()

def dessinerGrille(t, grille, taille):
    for i, ligne in enumerate(grille):
        for j, cellule in enumerate(ligne):
            x = j * taille
            y = -i * taille
            couleur = "black" if cellule else "white"
            dessinerCarre(t, couleur, x, y, taille)

# Exemple d’utilisation
n_lignes, n_colonnes = 10, 10
grille = [[0 for _ in range(n_colonnes)] for _ in range(n_lignes)]
placement_aleatoire(grille, n_lignes, n_colonnes)
tortue = creerFenetre()
dessinerGrille(tortue, grille, 20)
turtle.done()