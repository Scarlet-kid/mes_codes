class Arbre_binaire:
    
    def __init__(self, etiquette=None, gauche=None, droit=None):
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit= droit
        
    def isEmpty(self):
        return self.etiquette == None
        
    def append(self, valeur):
        if self.isEmpty():
            self.etiquette = valeur
        
        elif valeur < self.etiquette:
            if self.gauche == None:
                self.gauche = Arbre_binaire(valeur)
            else:
                self.gauche.append(valeur)
        
        else:
            if self.droit == None:
                self.droit = Arbre_binaire(valeur)
            else:
                self.droit.append(valeur)
                
    def infixe(self):
        if self.gauche!=None:
            self.gauche.infixe()
        print(self.etiquette, end=" ")
        
        if self.droit != None:
            self.droit.infixe()

    def recherche(val):
        pass
        
if __name__=='__main__':
    a = Arbre_binaire()
    a.append(12)
    a.append(15)
    a.append(14)
    a.append(9)
    a.append(5)
    a.append(18)
    a.infixe()   