def isSorted(tab:list): # renvoie un booléen
    # True : si triée, False: Sinon
    ok:bool # booleen passant à faux si deux valeurs ne sont pas ordonnées
    i:int # compteur de boucle pour avancer dans la liste
    ok = True
    i=1
    while i<len(tab) and ok:
        if (tab[i-1]<=tab[i]):
            # On avance dans le tableau
            i+=1
        else:
            # On sait que tab n'est pas trié
            ok=False
    return ok
# On niveau de tout ce qui est trie commencer par indice de dep 1 est mieux.