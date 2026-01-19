#> <


class etudiant:
    def __init__(self,nom,prenom,age,moyenne,promo):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne
        self.promo = promo
        
    def __str__(self):
        return f"etudiant : {self.nom} {self.prenom} age : {self.age} moyenne : {self.moyenne} promo : {self.promo}"
    
def creer():
    nom = input("nom ")
    prenom = input("prenom ")
    age = int(input("age "))
    moyenne = float(input("moyenne "))
    promo = int(input("promo "))
    return etudiant(nom,prenom,age,moyenne,promo)

etu = [etudiant("harboux","mathis",18,15,2),etudiant("sehim","yesim",18,2,1)]

def afficher(etu):
    for i in etu:
        print(i)
        
        
def ajoute(etu):
    x = creer()
    etu.append(x)
    return afficher(etu)


def recherche(etu,nom):
    for i in range (len(etu)):
        if etu[i].nom == nom:
            return i
        
def retirer(etu,nom):
    afficher(etu)
    x = recherche(etu,nom)
    etu.pop(x)
    print("après suppression : ")
    return afficher(etu)
    
def trier(etu):
    for i in range (1,len(etu)):
        p = 0
        if etu[i].moyenne > etu[i + 1].moyenne and p < i:
            