from math import *
from random import *
import matplotlib.pyplot as plt
import numpy as np

def au_moins_un(n,p):
    return 1-(1-p) ** n

    

def nb_coffres(p, seuil):
    n = 0
    while au_moins_un(n, p) < seuil:
        n += 1
    return n

#La loi d'une variable aleatoire cest donné les valeurs et les prob associé.
def esperance_ecart_type(valeurs, probas):
    esperance = 0
    for i in range(len(valeurs)):
        esperance += valeurs[i] * probas[i]

    variance = 0
    for j in range(len(valeurs)):
        variance += probas[j] * (valeurs[j] - esperance)**2

    return esperance,sqrt(variance)


def binomiale(n, p, k):
    return comb(n, k) * (p**k) * ((1 - p)**(n - k))

def joueur(n, p):
    nb_legendaires = 0
    for _ in range(n):
        if random() < p:
            nb_legendaires += 1
    return nb_legendaires


def densite(x, m, sigma):
    return (1 / (sigma * sqrt(2 * pi))) * exp(-0.5 * ((x - m) / sigma)**2)

def Phi(z):
    return 0.5 * (1 + erf(z / sqrt(2)))

def proba_exacte(n, p, k):
    return sum(binomiale(n, p, i) for i in range(k + 1)) 

def proba_approchee(n, p, k, correction):
    m = n * p
    sigma = sqrt(n * p * (1 - p))
    val = (k + 0.5) if correction else k
    z = (val - m) / sigma
    return Phi(z)

from math import sqrt

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
    #print(au_moins_un(100,0.01)) # Il a pas raison.
    #print(esperance_ecart_type([1,5,20,100],[0.8,0.15,0.04,0.01])) # La moyenne et l'ecart-type
    # Calculer P(X=0)
    print(binomiale(200,0.01,0)) #Meme chose pour le P(X=1)
    #Pour le P(X>=2) = 1-P(X=0)+P(X=1)

if __name__ == '__main__':
    prog()