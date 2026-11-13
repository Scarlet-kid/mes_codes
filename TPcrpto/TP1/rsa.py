from random import random


def est_premier(n:int):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            return False
    return True

import random
def premier():

    n = [i for i in range(2,100) if est_premier(i)]

    return random.sample(n,2)

def pgcd(a,b):
    if b ==0:
        return a
    return pgcd(b,a%b)


def euclide_etendu(a, b):

    # Initialisation du tableau (Ligne 0 et Ligne 1)
    r0, u0, v0 = a, 1, 0  # Ligne avec m
    r1, u1, v1 = b, 0, 1  # Ligne avec c

    # Boucle de mise à jour du tableau
    while r1 != 0:
        q = r0 // r1

        # Calcul de la nouvelle ligne
        r_temp = r0 - q * r1
        u_temp = u0 - q * u1
        v_temp = v0 - q * v1

        # Décalage des lignes
        r0, u0, v0 = r1, u1, v1
        r1, u1, v1 = r_temp, u_temp, v_temp

    return r0, u0, v0


def inverse_modulaire(c, m):
    """
    Calcule l'inverse d de c modulo m (c*d = 1 mod m)
    """
    g, u, v = euclide_etendu(m, c)
    if g != 1:
        return None  # N'existe pas si pas premiers entre eux
    else:
        return v % m  # S'assure que d est positif dans [0, m-1]

def CD(m):
    # Choisir un c premier avec m
    c = 3
    while pgcd(c, m) != 1:
        c += 2

    # Calculer d avec la méthode du tableau de Bézout
    d = inverse_modulaire(c, m)

    return c, d

def main():
    """n = int(input("enter the number: "))
    print(est_premier(n))"""
    print(premier())
if __name__ == '__main__':
    main()