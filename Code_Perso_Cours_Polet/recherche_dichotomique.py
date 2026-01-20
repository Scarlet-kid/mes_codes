def recherche_dichotomique(tab,val):
    debut = 0
    fin = len(tab) - 1
    while(debut<=fin):
        milieu = (debut+fin)//2
        if tab[milieu] == val:
            return milieu
        if tab[milieu] <= val:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1

liste = [1, 3, 5, 7, 9, 11, 13]
print(recherche_dichotomique(liste, 7))  # Affiche 3