from liste_chaine_python import*
def Insert(lst:list,val:int)->None:
    p = 0
    fini = False
    # On recherche la position
    while not fini:
        if p == len(lst):
            fini = True
        elif(lst[p]>val):
            fini = True
        else:
            p = p + 1
    lst.append(None)
    # On va faire le décalage
    for i in range(len(lst)-1,p,-1):
        lst[i] = lst[i-1]
    # On insert la valeur
    lst[i-1] = val     

# teste = [1,2,5,6,13]
# Insert(teste,0)
# print(teste)

def insertInSorted2(lst,v)->None:
    if lst.tete==None:
        lst.tete=Element(v,None )
    elif  lst.tete.valeur > v:
        lst.tete=Element(v,lst.tete)
    else:
        curseur=lst.tete
        fini = False
        while not fini:
            if curseur.suivant!=None:
                if curseur.suivant.valeur>v:
                    fini=True
                else:
                    curseur = curseur.suivant
            else:
                fini=True
        curseur.suivant=Element(v,curseur.suivant)
    lst.nb=lst.nb+1

maListe = Liste()
afficherListe(maListe)
insertInSorted2(maListe,10)
afficherListe(maListe)
insertInSorted2(maListe,15)
afficherListe(maListe)
insertInSorted2(maListe,1)
afficherListe(maListe)
insertInSorted2(maListe,9)
afficherListe(maListe)
insertInSorted2(maListe,9)
afficherListe(maListe)
    
