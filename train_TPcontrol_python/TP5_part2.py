from code import ligne
from tp_etu import *
import os

def Sauvegarder(lst:list[Etudiant])->None:
    with open ('etudiant.txt','w+') as file:
        for i in lst:
            file.write(str(i)+"\n")
        file.close()
        
def RecupereListeEtu(fichier):
    with open(fichier,'r+') as file:
        print(file.readlines())
        file.close()

def modifie(fichier: str) -> None:
    if not os.path.exists(fichier): # Tester l'existence du fichier
        print(f"Le fichier {fichier} n'existe pas.")
        return

    # 1) Lire toutes les lignes
    with open(fichier, "r", encoding="utf-8") as f:
        lignes = f.readlines() # Contenu du fichier sous forme d'une liste.

    if not lignes: # Cas du fichier vide
        print("Le fichier est vide.")
        return

    # 2) Afficher les étudiants avec un numéro:cas plus facile a gerer vraiment.
    print("Liste des étudiants dans le fichier :")
    for i, ligne in enumerate(lignes, start=1):
        print(f"{i}. {ligne.strip()}")

    # 3) Demander quel numéro modifier
    try:
        num = int(input("Numéro de l'étudiant à modifier : "))
    except ValueError:
        print("Numéro invalide.")
        return

    if num < 1 or num > len(lignes):
        print("Numéro hors limites.")
        return

    # 4) Resaisir les infos de l'étudiant
    print("Saisissez les nouvelles informations pour cet étudiant :")
    nouvel_etu = saisie_etu_info()   # tu l'as déjà définie

    # 5) Remplacer la ligne
    lignes[num - 1] = str(nouvel_etu) + "\n"

    # 6) Réécrire tout le fichier
    with open(fichier, "w", encoding="utf-8") as f:
        f.writelines(lignes)

    print("Les informations de l'étudiant ont été modifiées.")

def supprimer(fichier):
    # Tester l'existence du fichier:
    if not os.path.exists(fichier):
        return f'le fichier {fichier} n\'existe pas'

    # Lire toutes les lignes:
    with open(fichier,'r+') as file:
        data = file.readlines() # Contenu du fichier sous la forme d'une liste.
        file.close()

    #Cas du fichier vide:
    if not ligne:
        return f'Le fichier {fichier} est vide'
    # Afficher chaque etudiant avec un numéros
    for num,etu in enumerate(data,start=1):
        print(f'{num} : {etu.strip()}')

    #Demander le numéros a supprimer:
    try:
        suppr = int(input('Saisir le numéros de l\'étudiant a supprimer'))
    except ValueError:
        return "Numéros invalide"

    #Cas d'un numéros hors borne:
    if suppr < 1 or suppr > len(data):
        return 'Numéros hors borne'

    # Suprission en soi:
    data.pop(suppr-1)

    with open(fichier,'w+') as file:
        file.writelines(data)
        file.close()

    print("L'étudiant a été modifier avec succès")

def visualiser(fichier):
    # Tester si le fichier existe:
    if not os.path.exists(fichier):
        return f'le fichier {fichier} n\'exixte pas'

    # Objectif : visualiser les étudiants dans le fichier
    # Ouverture du fichier et stockage de ses données:
    with open(fichier,'r+') as file:
        data = file.readlines()
        file.close()

    # Cas du fichier vide:
    if not data:
        print("Aucun étudiant n'est présent dans le fichier")

    # Cas échéant:
    for num,etu in enumerate(data,start=1):
        print(f"{num} : {etu.strip()}")



if __name__=='__main__':
    #maListeEtu=list_etudiant()
    #ajout_etudiant(maListeEtu)
    #Sauvegarder(maListeEtu)
    #RecupereListeEtu('etudiant.txt')
    #modifie('etudiant.txt')
    #supprimer('etudiant.txt')
    visualiser('etudiant.txt')