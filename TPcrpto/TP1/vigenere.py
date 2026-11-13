alphabet = []
for i in range(97,97+26):
    alphabet.append(chr(i))

def mot_to_num(texte:str): # code ascii de chaque lettre du mot
    numLst = []
    for lettre in texte:
        numLst.append(ord(lettre))
    return numLst

def key_to_num(texte:str): # liste de l'indice de chaque lettre du mot dans l'alphabet
    IndexList = []
    for lettre in texte:
        IndexList.append(alphabet.index(lettre))
    return IndexList

def num_to_mot(asciiList:list[int]): #le mot correspondant a une littre de code ascii.
    LettreList = []
    for lettre in asciiList:
        LettreList.append(chr(lettre))
    mot = ''.join(LettreList)
    return mot

def chiffrement_vigenere(texte:str,cle:str)->str:
    ascii_msg = mot_to_num(texte)
    indice_cle = key_to_num(cle)

    ascii_chiffre = []
    len_cle = len(indice_cle)

    for i in range (len(ascii_msg)):
        code_m = ascii_msg[i]
        k = indice_cle[i%len_cle]

        nouveau_code = 97 +((code_m-97+k)%26)
        ascii_chiffre.append(nouveau_code)

    return num_to_mot(ascii_chiffre)
    # A comprendre plus en détail.

import math
#Pour le pgcd, utiliser la définition réursive.
def pgcd(n,p):
    res = math.gcd(n,p)
    return res

def pgcd_groupe(lst_int:list[int])->int:
    return math.gcd(lst_int)

#e codage du texte ’machinchosetrucmuche’ en utilisant la cl´e de chiffrement ’karl’

def main():
    #print(mot_to_num('lolo'))
    #print(key_to_num('karl'))
    #print(num_to_mot([109, 97, 99, 104, 105, 110, 99, 104, 111, 115, 101]))
    mot = "machinchosetrucmuch"
    cle = "karl"
    print(chiffrement_vigenere(mot,cle))


if __name__ == '__main__':
    main()