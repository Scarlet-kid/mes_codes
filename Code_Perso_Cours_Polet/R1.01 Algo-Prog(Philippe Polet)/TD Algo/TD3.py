def afficherEntete(debut : int= 0, fin : int= 10) -> None :
    print("x", end = "\t")
    for nombre in range(debut, fin+1) :
        print(nombre, end = "\t")
    print()
    
    
def afficherLigne(numero : int, debut : int= 0, fin : int= 10)-> None :
    print(numero,end="\t")
    for nombre in range(debut, fin+1) :
        print(nombre * numero, end = "\t")
    print()


#def afficherLigne(numero : int, debut : int= 0, fin : int= 10)-> None :
#    res = 0 
#    for i in range(debut, fin+1) :
#        res = numero * i
#        print(res, end = "\t")
        
def tableauMultiplication(debut : int= 0, fin : int=10)-> None :
    afficherEntete(debut,fin)
    for i in range(debut, fin+1) :
        afficherLigne(i,debut,fin)

def afficherCaractere(c : int) -> None :
    res = None
    var = c
    for i in range(0,c) :
        res = "*" * c
        if var != c :
            res += "." * i
        c -=1
        print(res)
        

if __name__ == "__main__" :
    afficherCaractere(6)