def square(a:float) -> float:
    return a*a

def calculer(x : int) -> int :
    return square(x)*10+25

#var = int(input("Choisissez un nombre"))
#print(calculer(var))

def construire(a : int, b : int) -> int :
    return (a//10)*1000 +b*10 + a%10

#var = int(input("Choisissez un nombre"))
#var2 = int(input("Choisissez un deuxième nombre"))
#print(construire(var, var2))

def saisieInt(bmin : int, bmax : int) -> None :
    print(("Saisie un chiffre entre",bmin,"et",bmax))
    var = int(input())
    while var > bmax or var < bmin :
        var = int(input("Ton chiffre n'est pas compris entre le minimum et le maximum, rechoisie un chiffe"))
    print("Tu as choisis un bon chiffre qui est :",var)
        
#saisieInt(1,60)

def principal() :
    var1 = saisieInt(10,99)
    var2 = saisieInt(10,99)
    print("le resultat est : ",construire(var1,var2))

if __name__ == "__main__" :
    principal()