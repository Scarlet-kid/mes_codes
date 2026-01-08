from graphviz import Digraph


class Node:
    def __init__(self, valeur, gauche=None, droit=None, parent=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
        self.parent = parent

    def hauteur(self):
        if self.gauche != None:
            hg = self.gauche.hauteur()
        else:
            hg = 0
        if self.droit != None:
            hd = self.droit.hauteur()
        else:
            hd = 0
        return 1 + max(hg, hd)

    def estFeuille(self):
        return self.gauche == self.droit == None

    def ajouter(self, val):
        if self.valeur > val:
            if self.gauche == None:
                self.gauche = Node(val, None, None, self)
            else:
                self.gauche.ajouter(val)
        else:
            if self.droit == None:
                self.droit = Node(val, None, None, self)
            else:
                self.droit.ajouter(val)

    def rechercher(self, val):
        # est ce que le noeud contient la valeur?
        if self.valeur == val:
            return self
        # on regarde si on a un fils susceptible de la contenir
        elif self.valeur > val:
            if self.gauche == None:
                return None
            else:
                return self.gauche.rechercher(val)
        else:
            if self.droit == None:
                return None
            else:
                return self.droit.rechercher(val)

    def mini(self):
        if self.gauche != None:
            return self.gauche.mini()
        else:
            return self

    def maxi(self):
        if self.droit != None:
            return self.droit.maxi()
        else:
            return self

    def __str__(self):
        ch = ''
        if self.gauche != None:
            ch = ch + self.gauche.__str__()
        ch = ch + str(self.valeur) + " "
        if self.droit != None:
            ch = ch + str(self.droit)
        return ch

    def toPdf(self, graphe, etiquette=None):
        noeud = str(self.valeur)
        graphe.node(noeud)
        #         print('ajout de ',noeud)
        if not (self.parent is None):
            #             print('a un parent')
            graphe.edge(str(self.parent.valeur), noeud, label=etiquette)
        #         print('pas de parent')
        if not (self.gauche is None):
            self.gauche.toPdf(graphe, "G")
        if not (self.droit is None):
            self.droit.toPdf(graphe, "D")


class ABR:
    def __init__(self, racine=None):
        self.racine = racine

    def mini(self):
        if self.racine == None:
            return None
        else:
            return self.racine.mini()

    def maxi(self):
        if self.racine == None:
            return None
        else:
            return self.racine.maxi()

    def estVide(self):
        return self.racine == None

    def hauteur(self):
        if self.racine == None:
            return 0
        return self.racine.hauteur()

    def ajouter(self, val):
        if self.racine == None:
            self.racine = Node(val)
        else:
            self.racine.ajouter(val)

    def rechercher(self, val):
        if self.racine != None:
            return self.racine.rechercher(val) != None
        else:
            return False

    def supprimerNoeud(self, supp):
        # le noeud existe t il?
        if supp != None:
            # cas 1 on supprime une feuille
            if supp.estFeuille():
                # il ne s agit pas de la racine
                # on retire la feuille de son parent
                if supp.parent != None:
                    if supp.parent.droit == supp:
                        supp.parent.droit = None
                    else:
                        supp.parent.gauche = None
                else:  # il s agit de la racine
                    self.racine = None
            # cas 2 on ne supprime pas une feuille
            else:
                # on recherche 1 remplacant dans la branch la plus grande
                hg, hd = (0, 0)
                if supp.droit != None:
                    hd = supp.droit.hauteur()
                if supp.gauche != None:
                    hg = supp.gauche.hauteur()
                # on remplace la valeur
                if hd > hg:
                    remp = supp.droit.mini()
                    supp.valeur = remp.valeur
                else:
                    remp = supp.gauche.maxi()
                    supp.valeur = remp.valeur
                # on supprime le noeud qui a servi de remplacant
                self.supprimerNoeud(remp)

    def supprimer(self, val):
        # on recherche un noeud contenant la valeur
        supp = self.racine.rechercher(val)
        if supp != None:
            self.supprimerNoeud(supp)

    def __str__(self):
        ch = "< "
        if self.racine != None:
            ch = ch + str(self.racine)
        ch = ch + ">"
        return ch

    def toPdf(self, title="arbre"):

        graphe = Digraph()
        if self.racine != None:
            self.racine.toPdf(graphe)
        graphe.render(title, view=True)


a = ABR()
a.ajouter(10)
a.ajouter(25)
a.ajouter(45)
a.ajouter(5)
a.ajouter(12)
a.ajouter(56)
a.ajouter(7)
a.ajouter(3)
a.ajouter(2)
a.ajouter(53)
a.ajouter(57)
a.toPdf("arbreComplet")
a.supprimer(25)
a.toPdf("arbreSans25")