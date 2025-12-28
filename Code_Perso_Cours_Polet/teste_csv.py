with open("etudiant.csv","r") as fichier:
    lesLignes = fichier.readlines()
entete = lesLignes[0].strip("\n\r").split(',')
print("liste des attributs:",entete)
print("-"*39)
donnees = []
for numLigne in range(1,len(lesLignes)):
    donnees.append(lesLignes[numLigne].strip("\n\r").split(','))
print("liste des etudiants: ",donnees)
print("-"*39)
table = []
for etudiant in donnees:
    dico = {}
    for i in range(len(entete)):
        dico[entete[i]] = etudiant[i]
    table.append(dico)
print("la liste de dictionnaires : ",table)
print("-"*39)