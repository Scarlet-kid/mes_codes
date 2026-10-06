class Etudiant:
    def __init__(self,nom:str,prenom:str,date:int,moyenne:float,promo:int):
        self.nom = nom
        self.prenom = prenom
        self.date = date
        self.moyenne = moyenne
        self.promo = promo

    def __str__(self):
        return f"{self.nom} {self.prenom}, né(e) en {self.date}, moyenne: {self.moyenne}, promo: {self.promo}"

def saisie_etu_info():
    nom = str(input("Le nom de l'étudiant:"))
    prenom = str(input("Le prénom de l'étudiant:"))
    date = int(input("La date de naissance de l'étudiant:"))
    moyenne = float(input("Saisir la moyenne de l'étudiant:"))
    promo = int(input("L'étudiant fait parti de quelle promo?:"))
    etudiant_creer =  Etudiant(nom,prenom,date,moyenne,promo)
    return etudiant_creer

def main():

    def list_etudiant()->list:
        liste = []
        liste.append(saisie_etu_info())
        return liste

    def ajout_etudiant(liste)->list[list]:
        n = int(input("Combien d'étudiants voulez vous ajouter?:"))
        for i in range(n):
            print(f'Etudiant numéros {i+1}')
            liste.append(saisie_etu_info())
        return liste

    def recherche_etudiant(liste:list[list]):
        name = str(input("Saisir le nom de l'étudiant que vous souhaitez rechercher:"))
        for indice, etu in enumerate(liste):

            if etu.nom == name:
                return indice
            else:
                return -1



    #print(saisie_etu_info())
    #print(list_etudiant())
    l1 = list_etudiant()
    print(ajout_etudiant(l1))
    print(recherche_etudiant(l1))

if __name__ == "__main__":
    main()