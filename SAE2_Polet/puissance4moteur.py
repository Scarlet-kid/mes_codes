import IA1
import IA2
import pygame
from copy import deepcopy

#definition de variables globales
Noir = (0,0,0)
Blanc = (255,255,255)
Gris = (128,128,128)
Bleu = (0,0,255)
Rouge = (255,0,0)
Vert = (0,255,0)
Orange = (225,127,0)
Rose = (255,0,127)
Jaune = (255,255,0)

Marron = (160,60,0)


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

def afficherPartieGraphique(p:dict,f):
    pygame.draw.rect(f,Bleu,[100,100,700,600])
    
    for i in range(6):
        for j in range (7):
            if p["grille"][5-i][j] == 1:
                pygame.draw.circle(f,Jaune,(150+j*100,150+i*100),45)
            elif p["grille"][5-i][j] == 2:
                pygame.draw.circle(f,Rouge,(150+j*100,150+i*100),45)
            else:
                pygame.draw.circle(f,Blanc,(150+j*100,150+i*100),45)
    pygame.display.update()
    pygame.time.set_timer(pygame.USEREVENT, 2000)
    finished = False
    while not finished:
        for e in pygame.event.get():
            if e.type == pygame.USEREVENT:
                finished = True
    return None

def afficherPartie(p:dict,f):
    print("0123456")
    for i in range(6):
        for j in range (7):
            if p["grille"][5-i][j] == 1:
                print("X",end="")
            elif p["grille"][5-i][j] == 2:
                print("O",end="")
            else:
                print(".",end="")
        print()
        
def permuterJoueur(p:dict):
    if  p["tourDe"] == 1:
        p["tourDe"] = 2
    else:
        p["tourDe"] = 1

def placer(p:dict,j:dict,c:int)->int:
    print(c)
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
        
        
def jouerUnTour(p:dict,afficher,f):
    if p[p["tourDe"]]["nbPion"]>0:
        print("au tour de ",p[p["tourDe"]]["nom"]," de jouer:")
        
        #pour empecher une corruption du plateau par un Bot
        pSaved = deepcopy(p)
        if p[p["tourDe"]]["num"]==1 :
            print("IA1")
            col =IA1.choix(pSaved)
        else:
            print("IA2")
            col = IA2.choix(pSaved)
        lig = placer(p,p[p["tourDe"]],col)
        if lig>=0:
            p[p["tourDe"]]["nbPion"]-=1
            p["bad"]=0
            testerVictoire(p,p[p["tourDe"]]["num"],lig,col)
            p["dernierCoup"] = (col,lig)
            permuterJoueur(p)
            afficher(p,f)
        else :
            print("mauvaise colonne")
            p["bad"]=p["bad"]+1
            if p["bad"] == 3:
                p["gagnant"]=3-p[p["tourDe"]]["num"]
        return p["gagnant"]==0
    else:
        return False
    
def cbIdemDir(p:dict,v:int,l:int,c:int,dl:int,dc:int)->int:
    if -1<l+dl<6 and -1<c+dc<7 :
        if p["grille"][l+dl][c+dc]== v:
            return 1+cbIdemDir(p,v,l+dl,c+dc,dl,dc)
        else :
            return 0
    return 0
        
def testerVictoire(p,v,l,c):
    #test horizontal
    compteur = cbIdemDir(p,v,l,c,0,-1)+cbIdemDir(p,v,l,c,0,1)
    if compteur>2:
        print("horizontal :",compteur)
        p["gagnant"]=v
    #test vertical
    compteur = cbIdemDir(p,v,l,c,-1,0)+cbIdemDir(p,v,l,c,1,0)
    if compteur>2:
        print("vertical :",compteur)
        p["gagnant"]=v
    #test diag descendante
    compteur = cbIdemDir(p,v,l,c,1,-1)+cbIdemDir(p,v,l,c,-1,1)
    if compteur>2:
        print("diag desc :",compteur)
        p["gagnant"]=v
    #test diag montante
    compteur = cbIdemDir(p,v,l,c,1,1)+cbIdemDir(p,v,l,c,-1,-1)
    if compteur>2:
        print("diag asc :",compteur)
        p["gagnant"]=v
    
 
def testerGame():
    mode = input("mode affichage : 1=>console 2=>graphique")
    if mode == "2" :
        foncAffichage=afficherPartieGraphique
        pygame.init()
    
        fenetre = pygame.display.set_mode([900,800])
        fenetre.fill([255,255,255])
        pygame.display.update()
    else:
        fenetre = None
        foncAffichage = afficherPartie
    game = creationPartie()
    afficherPartie(game,fenetre)
    ok = True
    while(ok) :
        
        ok = jouerUnTour(game,foncAffichage,fenetre)
    print("fin de partie")
    if game["gagnant"]!=0 :
        print("Bravo! Victoire de ",game[game["gagnant"]]["nom"])
    else :
        print("C'est une égalité")
    if mode=="2":
        quitter = False
        while not quitter:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    quitter = True
          
                if event.type == pygame.QUIT:
                        quitter = True
        pygame.quit()
      
                    
if __name__ == "__main__":
    testerGame()