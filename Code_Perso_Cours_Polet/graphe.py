class Graphe:
    def __init__(self,nbsommets):
        self.adj = [[0]*nbsommets for _ in range(nbsommets)]
        self.labels = []
        self.dico = dict()
        for i in range(len(self.adj[0])):
            self.labels.append(str(i))
            self.dico[str]