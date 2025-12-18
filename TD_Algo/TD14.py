from random import randint
LesCouleurs = ["Coeur","Carreau","Pique","Treffle"]
LesValeurs = { "2" :1,"3" :2,"4" :3,"5" :4,"6" :5,"7" :6,"8" :7,"9" :8, "10" :9,"Valet" :10,"Dame" :11,"Roi" :12,"As" :13 }

class Carte:
    def __init__(this,val,coul):
        this.valeur=val
        this.couleur=coul
    
    def __str__(self):
        return self.valeur+" de "+self.couleur

    def comparer(self,c2):
        if LesValeurs[self.valeur]>LesValeurs[c2.valeur]:
            return 1
        elif LesValeurs[self.valeur]<LesValeurs[c2.valeur]:
            return 2
        else:
            return 0
    
class JDC:
    def __init__(self,desCartes:list[Carte]=None):
        self.cartes = []
        if desCartes == None:
            for coul in LesCouleurs:
                for val in LesValeurs: # Parcours par défaut les clés 
                    self.cartes.append(Carte(val,coul))
        else:
            for c in desCartes:
                self.cartes.append(c)
    
    def melanger(self):
        lim = len(self.cartes)
        for _ in range(lim):
            a = randint(0,lim-1)
            b= randint(0,lim-1)
            self.cartes[a],self.cartes[b],self.cartes[a]
            
    def __str__(self):
        s=f"jeu de {len(self.cartes)} cartes:\n"
        for c in self.cartes:
            s=s+str(c) +'\n'
        return s
    
class Joueur:
    def __init__(self,name):
        self.name = name

class Partie:
    def __init__(self,j1,j2):
        self.joueur1=j1
        self.joueur2=j2
        self.tas=JDC([])
    
    #def distribuer(self,p:Partie,j:Joueur):
        
        
if __name__=="__main__":
    c1=Carte("2","Carreau")
    c2=Carte("7","Treffle")
    print(c1)
    print(c2)
    jeu1=JDC()
    jeu2=JDC([Carte("Dame","Coeur"),Carte("Roi","Pique")])
    print(jeu1)
    print(jeu2)
    jeu1.melanger()
    print(jeu1)
