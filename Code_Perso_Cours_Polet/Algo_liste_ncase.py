def construireListe(taille:int,valeur:float)->list:
    res=[]
    for i in range(0, taille):
        res.append(valeur)
    return res
print(construireListe(7,5))
