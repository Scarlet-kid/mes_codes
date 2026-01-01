"""if __name__ == "__main__":
    maListe = [x**3 for x in [y for y in range(1,11) if y%2==0] if (x**3)%3==0]
    #print(maListe)
    maListe = [(x, y, x and y) for x in [True, False] for y in [True, False]]
    print(maListe)"""

def f(x, y):
    if x==y:
        return 1
    else:
        return 0

def identity(taille):
    return [[f(l,c) for l in range(taille)]for c in range(taille)]

def transpose(m):
    return [[ligne[i] for ligne in m] for i in range(len(m[0]))]

if __name__=="__main__":
    i = identity(3)
    print(i)
