import csv
with open("etudiant.csv","r") as fichier:
    mesDonnees = list(csv.DictReader(fichier))
print("dictionnaire ordonné recupéré :", mesDonnees)
print("-"*40)
print(mesDonnees[1]["Nom"])