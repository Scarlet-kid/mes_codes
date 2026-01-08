"""mat = []
with open('essai.txt','r+') as file:
    for li in file:
        s = li.strip('\n\r')
        l = s.split(";")
        mat.append(l)
    print(mat)"""

# Sauvegarder dans un fichier binaire en gros l'ecriture
import pickle # pickle permet d'écrire des objet str, int etc python dans les fichiers binaires
dico = {'a':[1, 2.0 , 3, "e"], 'b':('string',2), 'c':None}
lis = [1,2,3]
with open('data.bin', 'wb') as fb:
    pickle.dump(dico, fb)
    pickle.dump(lis, fb)

# Lecture d'un fichier binaire:
with open('data.bin', 'rb') as fb:
    dico = pickle.load(fb)
    lis = pickle.load(fb)
    print(dico,lis)

data = [1,2,3,4]
with open('data.bin','wb') as f:
    pickle.dump(data,f) # pickle.dump(objet,la vairiable)

# Lire un objet avec pickle.load()
with open('data.bin','rb') as f:
    data = pickle.load(f)
print(data)
# un dump = un load

dico2 = {"nom":"Scarlet", "age":20}
liste = [10,20,30]

with open('data.bin','wb') as f:
    pickle.dump(dico2,f)
    pickle.dump(liste,f)

with open('data.bin','rb') as f:
    dico = pickle.load(f)
    liste = pickle.load(f)

print(dico)
print(liste)

# Ajouter des donnéess
with open('data.bin', 'ab') as f:
    pickle.dump(999, f)

with open("data.bin",'rb') as f:
    while True:
        try:
            print(pickle.load(f))
        except EOFError:
            break

etudiant = [
    {"nom" : "Ali", "note" : 14},
    {"nom" : "Sara", "note" : 16}
]
with open("etu.bin",'wb') as f:
    for e in etudiant:
        pickle.dump(e,f)

with open('etu.bin','rb') as f:
    try:
        while True:
            e = pickle.load(f)
            print(e["nom"], e["note"])

    except EOFError:
        pass
# OK ca va !