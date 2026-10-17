from math import *
from random import *
import matplotlib.pyplot as plt
import numpy as np

def au_moins_un(n,p):
    return 1 - (1-p)**n

def nb_coffres(p,seuil):
    n = 1
    while au_moins_un(n,p) < seuil:
        n += 1
    return n

def esperance(valeurs,probas):
    s = 0
    for i in range(len(valeurs)):
        s += valeurs[i] * probas[i]
    return s

def variance(valeurs,probas):
    s2 = 0
    e = esperance(valeurs,probas)
    for i in range(len(valeurs)):
        s2 += valeurs[i] **2 * probas[i]
    
    return s2 - e**2

def esperance_ecart_type(valeurs,probas):
    return esperance(valeurs,probas), sqrt(variance(valeurs,probas))

def binomiale(n,p,k):
    return comb(n,k) * p**k * (1-p)**(n-k)

def joueur(n,p):
    x = 0 
    for _ in range(n):
        if random() < p: # PK inferieur oft.
            x+=1
    return x

def densite(x,m,sigma):
    return (1/(sigma*sqrt(2*pi))) * exp(-0.5*((x-m)/sigma)**2)

def Phi(z):
    return 0.5 *(1+erf(z/sqrt(2)))

def proba_exacte(n,p,k):
    return sum(binomiale(n,p,k) for i in range (k+1))

def proba_approchee(n,p,k,correction):
    m = n*p
    sigma = sqrt(n*p*1-p)
    val = k+0.5 if correction else k
    z = (val-m)/sigma
    return Phi(z)


def erreur_max(n, p):
    m = n * p
    s = sqrt(n * p * (1 - p))
    F = 0.0
    err = 0.0
    for k in range(n + 1):
        F += binomiale(n, p, k)
        err = max(err, abs(F - Phi((k + 0.5 - m) / s)))
    return err

def prog():
    #print(au_moins_un(100,0.01))
    #print(nb_coffres(0.01,0.5))*
    #print(nb_coffres(0.01,0.9))
    #print(esperance_ecart_type([1,5,20,100], [0.80,0.15,0.04,0.01]))
    P0,P1 = binomiale(200,0.01,0),binomiale(200,0.01,1)
    print(P0,P1,1-(P0+P1))

    
if __name__ == '__main__':
    print(prog())