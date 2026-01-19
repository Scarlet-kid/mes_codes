from random import *

def faireTrouver(val):
    
    compt:int=0
    utl:int=None
    
    while (utl!=val):
        
        utl=int(input("Saisir un nombre entre 1 et 99:"))
        compt+=1
        
        if (utl>val):
            print("Trop grand")
        elif (utl<val):
            print("Trop petit")
    
    print("Vous avez trouvé le juste nombre qui est {}".format(val))
    return compt # le return contient oft le résultat de la fonction.

"""
C'est le résultat final de la fonction qui peut etre stocké dans une variable.
Quand on applique a une variable une fonction,c'est la valeur de son return ca contient oft.
"""
        
def progPrincipal():
    valeur=randint(1,99)
    score=faireTrouver(valeur)
    print("Bravo, vous avez trouve en ", score, "coups")

if (__name__=="__main__"):
     progPrincipal()