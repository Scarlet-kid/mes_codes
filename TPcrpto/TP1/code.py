from random import shuffle
alphabet = [chr(i) for i in range(ord('a'),ord('a')+26)]

    
def frequence(file):
    lstFrequence = []
    with open(file,'r') as f:
        contenu = f.read()
    longueur = len(contenu)
    for elt in alphabet:
        fLettre = contenu.count(elt)/longueur
        lstFrequence.append([elt,round(fLettre,3)])
    return lstFrequence

def tri_liste(lst:list[list]):
    l = list()
    f = sorted(lst,key=lambda x:x[1],reverse=True)
    for i in f:
        l.append(i[0])
    return l

def tri_liste2(lst:list[list]):
    maLst = []
    for i in lst:
        maLst.append([i[1],i[0]])
    l = sorted(maLst,reverse=True)
    k = []
    for elt in l:
        k.append(elt[1])
    return k

def permutation(alphabet:list):
    res = alphabet.copy()
    shuffle(res)
    return res

def cle(alphabet:list):
    monDico = {}
    perm = permutation(alphabet)
    for i in range(len(alphabet)):
        monDico[alphabet[i]] = perm[i]
    return monDico

def chiffrement_aleatoire(file,cle:dict):
    with open(file,'r+') as f :
        contenu = f.read()
    new = "".join(cle[c] for c in contenu)
    with open(file,'r+') as f :
        f.write(new)


def chiffrement_aleatoire(file, cle_dico: dict):
    with open(file, 'r', encoding='utf-8') as f:
        contenu = f.read().lower()
    new = "".join(cle_dico.get(c, c) for c in contenu)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new)


def chiffrer_dechiffrer():
    # 1. Fréquences des lettres du texte d'origine
    freq_lettres_france = tri_liste2(frequence('test.txt'))
    print(freq_lettres_france)

    # 2. Clé de chiffrement aléatoire
    cle_chiffrement = cle(alphabet)
    print(cle_chiffrement)

    # 3. Chiffrement du texte dans test.txt
    chiffrement_aleatoire('test.txt', cle_chiffrement)

    # 4. Fréquences des lettres du texte chiffré
    freq_texte_chiffre = tri_liste2(frequence('test.txt'))
    print(freq_texte_chiffre)

    # 5. Déduction de la clé de déchiffrement par analyse fréquentielle
    cle_dechiffrement = {}
    for i in range(len(alphabet)):
        lettre_chiffree = freq_texte_chiffre[i]
        lettre_supposee_claire = freq_lettres_france[i]
        cle_dechiffrement[lettre_chiffree] = lettre_supposee_claire

    # 6. Déchiffrement du texte avec la clé estimée
    chiffrement_aleatoire('test.txt', cle_dechiffrement)

    # A recomprendre avant le tp
def prog():
    #print(alphabet)
    #print(frequence('texte.txt'))
    lstFrequence = frequence('texte.txt')
    #freq_lettres_france = tri_liste(lstFrequence)
    #print(freq_lettres_france)
    #print(tri_liste2(lstFrequence))
    #print(permutation(alphabet))
    #print(cle(alphabet))
    #chiffrement_aleatoire('test.txt',cle(alphabet))
    print(chiffrer_dechiffrer())

if __name__ == '__main__':
    prog()