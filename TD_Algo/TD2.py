from math import sqrt,pow

def absolue(x : float) -> float :
    if x > 0 :
        return x
    else :
        return -x
    
def equation(a : int, b : int) -> int :
    return -b/a

def equation2(a : int, b : int, c : int) -> int :
    liste = []
    delta = b**2 - 4*a*c
    if delta < 0 :
        return []
    elif delta == 0 :
        return -b/2*a
    elif delta > 0 :
        return [(-b+sqrt(delta))/2*a, (-b-sqrt(delta))/2*a]

def equilateral(a : int, b : int, c :int)-> bool :
    return a == b and a == c 
    
def isocele(a : int, b : int, c : int) :
    return a == b or b == c or c == a 
    
def triangle_rectangle(a : int, b : int, c : int) :
    return c**2 == b**2 + a**2 or b**2 == c**2 + a**2 or a**2 == c**2 + b**2 

def principal():
    var1 = int(input("Choisissez une longueur"))
    var2 = int(input("Choisissez une deuxième longueur"))
    var3 = int(input("Choisissez une troisièmelongueur"))
    if equilateral(var1,var2,var3) :
        print(" le triangle est equilateral")
    elif triangle_rectangle(var1,var2,var3) :
        if isocele(var1,var2,var3) :
            print("rectangle, isocele")
        else : 
            print(" le triangle est rectangle")
    elif isocele(var1,var2,var3) :
        print(" le triangle est isocele")
    else :
        print(" aucune des valeurs ne correspond a un triangle connu, il est donc quelconque")




if __name__ == "__main__" :
    principal()
    #print(triangle_rectangle(4,3,5))

