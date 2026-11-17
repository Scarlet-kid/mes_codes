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


def euclide_etendu(a: int, b: int):
    r0, u0, v0 = a, 1, 0
    r1, u1, v1 = b, 0, 1
    while r1 != 0:
        q = r0 // r1
        r0, u0, v0, r1, u1, v1 = r1, u1, v1, r0 - q * r1, u0 - q * u1, v0 - q * v1
    return r0, u0, v0

def CD(m: int) -> tuple[int, int]:
    """
    Question 5 du TP RSA :
    Prend en entrée un entier m = (p-1)*(q-1)
    Renvoie c et d tels que pgcd(c, m) == 1 et c * d ≡ 1 (mod m)
    """
    # 1. On choisit c premier avec m
    c = 3
    while pgcd(c, m) != 1:
        c += 2

    # 2. On calcule d = inverse de c modulo m (via Bézout)
    g, u, v = euclide_etendu(m, c)
    d = v % m

    return c, d

def key() -> tuple[list[int], list[int]]:
    """Génère le couple de clés [n, c] (publique) et [n, d] (privée)."""
    p, q = premier()
    n = p * q
    m = (p - 1) * (q - 1)
    c, d = CD(m)
    cle_publique = [n, c]
    cle_privee = [n, d]
    return cle_publique, cle_privee

# --- QUESTION 8 ---
def chiffrement_rsa(mot: list[int], cle: list[int]) -> list[int]:
    """Chiffre (ou déchiffre) un mot représenté par une liste d'entiers avec la clé [n, exp]."""
    n, exp = cle[0], cle[1]
    mot_code = []
    for lettre in mot:
        mot_code.append(pow(lettre, exp, n))
    return mot_code

# --- QUESTION 9 ---
def programme_principal_rsa():
    """Programme principal pour tester le chiffrement et le déchiffrement RSA."""
    # 1. Génération d'un mot de 7 lettres au hasard (entiers de 0 à 25)
    mot_original = [random.randint(0, 25) for _ in range(7)]
    
    # 2. Génération des clés
    cle_pub, cle_priv = key()
    
    # 3. Chiffrement avec la clé publique
    mot_chiffre = chiffrement_rsa(mot_original, cle_pub)
    
    # 4. Déchiffrement avec la clé privée
    mot_dechiffre = chiffrement_rsa(mot_chiffre, cle_priv)
    
    # 5. Affichage conforme aux exigences du TP
    print(f"Le mot genere au hasard est : {mot_original}")
    print(f"La cle publique generee est : {cle_pub}")
    print(f"La cle privee generee est   : {cle_priv}")
    print(f"Le mot chiffre avec la cle publique est : {mot_chiffre}")
    print(f"Le mot dechiffre avec la cle privee est : {mot_dechiffre}")

if __name__ == "__main__":
    programme_principal_rsa()
