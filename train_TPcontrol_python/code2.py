"""mat = []
with open('essai.txt','r+') as file:
    for li in file:
        s = li.strip('\n\r')
        l = s.split(";")
        mat.append(l)
    print(mat)"""

# Sauvegarder dans un fichier binaire en gros l'ecriture
import pickle
dico = {'a':[1, 2.0 , 3, "e"], 'b':('string',2), 'c':None}
lis = [1,2,3]
with open('data.bin', 'wb') as fb:
    pickle.dump(dico, fb)
    pickle.dump(lis, fb)

# Lecture d'un fichier binaire:
with open('data.bin', 'rb') as fb:
    dico = pickle.load(fb)
    lis = pickle.load(fb)