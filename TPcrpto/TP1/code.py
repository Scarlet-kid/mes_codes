import string
alphabet = []
for i in range(97,97+26):
    alphabet.append(chr(i))
    
def frequence(file):
    lstFrequence = []
    with open(file,'r') as f:
        contenu = f.read()
        longueur = len(contenu)
        print(f'{longueur}')


def prog():
    #print(alphabet)
    print(frequence('texte.txt'))
    
if __name__ == '__main__':
    prog()