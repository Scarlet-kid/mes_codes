class Point:
    def __init__(self, vx=0, vy=0):
        self.x = vx
        self.y = vy

def modifPoint(p):
    p.x = p.x + 0.5
    p.y = p.y + 0.5

def prog():
    centre = Point()
    print("Centre : (",centre.x,",",centre.y,")")
    modifPoint(centre)
    print("Centre : (",centre.x,",",centre.y,")")

if __name__ == "__main__":
    prog()



