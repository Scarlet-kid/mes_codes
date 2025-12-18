import pygame


def drawCB(cb:list[list[int]],fenetre):
    myfont = pygame.font.SysFont("monospace", 20)
    clair = (250,240,240)
    fonce = (120,120,120)
    blanc = (255,255,255)
    noir = (0,0,0)
    pygame.draw.rect(fenetre,fonce,[49,49,402,402])
    for j in range(10):
        lab = myfont.render(str(j),1,[0,0,0])
        fenetre.blit(lab,[60+40*j,20])
    for i in range(10):
        lab = myfont.render(chr(ord('A')+i),1,[0,0,0])
        fenetre.blit(lab,[20,60+40*i])
        for j in range(10):
            if (i+j) % 2 == 0:
                color = clair
            else:
                color = fonce
                
            pygame.draw.rect(fenetre,color,[50+40*j,50+40*i,40,40])
        
            if cb[i][j]==1:
                pygame.draw.circle(fenetre,blanc,(70+40*j,70+40*i),15)
            elif cb[i][j]==2:
                pygame.draw.circle(fenetre,noir,(70+40*j,70+40*i),15)
    pygame.display.update()
    
def effacerPion(fen,pos):
    fonce = (120,120,120)
    pygame.draw.circle(fen,fonce,(70+40*pos[1],70+40*pos[0]),15)
    pygame.display.update()
    
def afficherPion(fen,pos,joueur):
    blanc = (255,255,255)
    noir = (0,0,0)
    if joueur == 1:
        couleur = blanc
    else:
        couleur = noir
    pygame.draw.circle(fen,couleur,(70+40*pos[1],70+40*pos[0]),15)
    pygame.display.update()


def createMatrix(nl:int=10,nc:int=10)->list[list[int]]:
    m:list[list[int]] = list()
    for i in range(nl):
        m.append(list())
        for j in range(nc):
            m[i].append(0)
    return m

def initCB()->list[list[int]]:
    cb:list[list[int]] = createMatrix()
    
    for i in range(4):
        for j in range(0,10,2):
            cb[i][j+(i+1)%2] = 2
            cb[i+6][j+(i+1)%2] = 1
    return cb




def isBlack(row: int,col: int)->bool:
    return (row+col)%2!=0

def printCB(cb:list[list[int]])->None:
    print("  ",end="")
    for j in range(10):
        print(j,end=" ")
    print()
    for i in range(10):
        print(" -"+"--"*10)
        print(chr(ord('A')+i),end="")
        for j in range(10):
            if cb[i][j]==0:
                c = ' '
            elif cb[i][j]==1:
                c = 'B'
            else:
                c = 'N'
            print("|"+c,end="")
        print("|")
    print(" -"+"--"*10)
    
def saisieCorrecte(texte:str="?",mini=0,maxi=9):
    val = int(input(texte))
    if val<mini or val>maxi:
        print("valeur incorrecte: veuillez ressaisir...")
        return saisieCorrecte(texte, mini,maxi)
    else :
        return val

def caseExistante(l:int,c:int)->bool:
     return l<10 and l>=0 and c<10 and c>=0

def caseLibre(damier:list[list[int]], l:int, c:int)->bool:
    return damier[l][c]==0

 
def saisieCoord()->tuple:
    print("coordonnees de la case (ie. B4)? ")
    cd = input().upper()
    a,b = cd
    dl = ord(a)-ord('A')
    dc = int(b)
    if caseExistante(dl,dc):
        return dl,dc
    else:
        print("coordonnées invalides, ressaisir!")
        return saisieCoord()
    

def deltaOK(j:int)->int:
    if j==2:
        return 1
    else:
        return -1
    
def opposant(j:int)->int:
    if j==1:
        return 2
    else:
        return 1
 
def jouerUnCoup(damier:list[list[int]],joueur:int=1):
    print("entrer la case de dep?")
    dl,dc = saisieCoord()
    print("entrer la case d'arrivee?")
    al,ac = saisieCoord()
    if(damier[dl][dc]!=joueur):
        print(f'{dl=} {dc=} {damier[dl][dc]=}')
        print("case de départ erronnée, recommencez!")
        jouerUnCoup(damier,joueur)
    if(not isBlack(al,ac)):
        print("case d'arrivée blanche, recommencez!")
        jouerUnCoup(damier,joueur)
    if(not damier[al][ac]==0):
        print("case d'arrivée non libre, recommencez!")
        jouerUnCoup(damier,joueur)
    if abs(al-dl)==1 :
        #deplacement simple potentiel
        print("deplacement simple potentiel")
        if(al-dl!=deltaOK(joueur)):
            print("mauvais sens, recommencez!")
            jouerUnCoup(damier,joueur)
        if(abs(ac-dc)!=1):
            print("ce n'est pas un deplacement valide, recommencez!")
            jouerUnCoup(damier,joueur)
        damier[al][ac]=damier[dl][dc]
        damier[dl][dc]=0
        return True
            
        
    elif abs(al-dl)==2 :
        #deplacement prise de pion potentiel
        print("deplacement prise de pion potentiel")
        if(abs(ac-dc)!=2):
            print("ce n'est pas un deplacement valide, recommencez!")
            jouerUnCoup(damier,joueur)
        if(damier[(al+dl)//2][(ac+dc)//2]!=opposant(joueur)):
            print("vous ne mangez pas de pion adverse, recommencez!")
            jouerUnCoup(damier,joueur)
        damier[(al+dl)//2][(ac+dc)//2]=0
        damier[al][ac]=damier[dl][dc]
        damier[dl][dc]=0
        return True
    
def getCase():
    click = False
    while not click:
        #print('.',end='')
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # click gauche
#             print("click gauche detecte")
            mx,my = pygame.mouse.get_pos()
            if mx>49 and mx<451 and my>49 and my<451:
                col = (mx-50)//40
                lig = (my-50)//40
                click = True
        if event.type == pygame.QUIT:
            pygame.quit()

    return lig,col

                    
 
def playTurn(joueur:int,damier:list[list[int]],fen):
    print(f"{joueur=}")
    print("selectionner la case de départ...")
    dl,dc = getCase()
    print(f"{dl=} {dc=}")
    print("selectionner la case d arrivee...")
    al,ac = getCase()
    print(f"{al=} {ac=}")
    try:
        if(damier[dl][dc]!=joueur):
            raise Exception("case de départ erronnée mauvais joueur, recommencez!")
        if(not isBlack(al,ac)):
            raise Exception("case d'arrivée blanche, recommencez!")
        if(not damier[al][ac]==0):
            raise Exception("case d'arrivée non libre, recommencez!")
        if abs(al-dl)==1 :
            #deplacement simple potentiel
            print("deplacement simple potentiel")
            if(al-dl!=deltaOK(joueur)):
                raise Exception("mauvais sens, recommencez!")
            if(abs(ac-dc)!=1):
                raise Exception("ce n'est pas un deplacement valide, recommencez!")
            damier[al][ac]=damier[dl][dc]
            damier[dl][dc]=0
            afficherPion(fen,(al,ac),joueur)
            effacerPion(fen,(dl,dc))
            return True
                
            
        elif abs(al-dl)==2 :
            #deplacement prise de pion potentiel
            print("deplacement prise de pion potentiel")
            if(abs(ac-dc)!=2):
                raise Exception("ce n'est pas un deplacement valide, recommencez!")
            if(damier[(al+dl)//2][(ac+dc)//2]!=opposant(joueur)):
                raise Exception("vous ne mangez pas de pion adverse, recommencez!")
                
            damier[(al+dl)//2][(ac+dc)//2]=0
            damier[al][ac]=damier[dl][dc]
            damier[dl][dc]=0
            effacerPion(fen,((al+dl)//2,(ac+dc)//2))
            afficherPion(fen,(al,ac),joueur)
            effacerPion(fen,(dl,dc))
            return True
        else :
            raise Exception("ce n'est pas un deplacement valide, recommencez!")
        
    except Exception as probleme:
        print(probleme)
        return playTurn(joueur,damier,fen)


pygame.init()
win = pygame.display.set_mode((500,500))
pygame.draw.rect(win,(255,255,255),[0,0,500,500])
pygame.display.update()   
damier = initCB()    
drawCB(damier,win)

joueur = 1
while(True):
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
    #drawCB(damier,win)
    playTurn(joueur,damier,win)
    #drawCB(damier,win)
    joueur=opposant(joueur)