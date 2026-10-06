from math import sqrt
class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def distanceTo(self,other)->float:
        return sqrt((self.x-other.x)**2+(self.y-other.y)**2)

class Polygone:
    def __init__(self,lp:list[Point]):
        self.lesPoints = list()
        for p in lp:
            self.lesPoints.append(Point(p.x,p.y))
        self.nbCotes = len(self.lesPoints)
    
    def perimetre(self)->float:
        if self.nbCotes<3:
            raise Exception("nombre de coté insuffisant")
        longueur = 0
        for i in range(1,self.nbCotes):
            longueur = longueur + self.lesPoints[i-1].distanceTo(self.lesPoints[i])
        longueur = longueur+lesPoints[-1].distanceTo(self.lesPoints[0])

# Question A
p1=Point(2,3)
p2=Point(4,5)
print(p1)
print(p2)

def Distance(point1,point2):
    return sqrt((point2.x-point1.x)**2 + (point2.y-point1.y)**2)

# Question B
pol1 = Polygone(8,10)
def peri_polygone():
    pass
point = [Point(),Point(1,0),Point(1,1)]

def prog():
    print(f"distance = {Distance(p1,p2)})
    print(f"distance = {p1.distanceTo(p2)}")

if __name__ == "__main__":
    prog()