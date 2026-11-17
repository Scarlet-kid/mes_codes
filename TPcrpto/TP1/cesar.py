import random
alphabet = [chr(i) for i in range(ord('a'),ord('a')+26)]


def cesar():
    cle_chiffrement = random.randint(0,25)

    cle_dechiffrement = (26 - cle_chiffrement)%26
    
    return cle_chiffrement,cle_dechiffrement

def cryptage_cesar(mot,cle):
    pass

if __name__ == "__main__":
    print(cesar())