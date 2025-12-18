"""utl  = input("Quel est votre age?:")
try:
    utl_int = int(utl)
except:
    print("L'age indiqué est incorrecte")
else: #Ce qui se passe en cas de réussite
    print("Tu as",utl_int,"ans")
finally: # Ce qui se passe dans tous les cas,réussite ou pas.
    print("FIN DU PROGRAMME....")

"""

"""nombre1 = 150
nombre2 = input("Choisir le nombre pour diviser:")
try:
    nombre2 = (int(nombre2))
    print("Résultat = {}".format(nombre1/nombre2))

except ZeroDivisionError:
    print("Vous ne pouvez pas diviser par 0")

except ValueError:
    print("Entrez un nombre!!!")

except:
    print("Valeur incorrecte")

else:
    print("Bravo tu as entré un nombre valide")
    
finally:
    print("Fin du programme...")
    """

try:
    age = input("Age:")
    age = int(age)
    assert age<25 # Je veux que age soit plus petit que 25. 

except AssertionError:
    print("J'ai attrapé l'exception")