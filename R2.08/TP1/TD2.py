import code
from matplotlib import pyplot as plt

def nuage(x:list[float],y:list[float]):
    plt.scatter(x,y)

# Jai deja la fct moyenne

def pointMoyen(x:list[float],y:list[float])->tuple:
    return code.moyenne(x),code.moyenne(y)

def ecart_type(x:list[float],y:list[float])->tuple:
    return code.ecart(x),code.ecart(y)

def covariance(x:list[float],y:list[float]):
    maLong = code.long(x)
    moyX = code.moyenne(x)
    moyY = code.moyenne(y)

    res = 0
    for i in range(code.long(x)):
        res+=(x[i]*y[i])
    
    return (res/maLong) - (moyX*moyY)

def coefdir(x:list[float],y:list[float])->float:
    return covariance(x,y)/code.variance(x)

def coeford(x:list[float],y:list[float]):
    moyY,moyX = pointMoyen(x,y)
    return moyY - (coefdir(x,y)*moyX)

def nuage_affine(x:list[float],y:list[float]):
    plt.title(" Evolution des prix en fonction des clients")
    Nx,Ny  = pointMoyen(x,y)
    a = coefdir(x,y)
    b = coeford(x,y)
    nuage(x,y)
    plt.plot(Nx,Ny,'ro',c='red') #ro : plt.plot pour un seul point.
    plt.scatter(x,y)
    minX , maxX = code.mini(x),code.maxi(x)
    plt.plot([minX,maxX],[a*minX+b,a*maxX+b])
    plt.text(25,80,f"{round(coefdir(x,y),2)}x + {round(coeford(x,y),2)}\n{pointMoyen(x,y)}",c="red",ha="center")
    plt.xlabel("nb de clients")
    plt.ylabel("Prix")
    plt.show()
    
def nuage_affine2(x:list[float],y:list[float]):
    # 1. Calculs
    Nx, Ny = pointMoyen(x,y)
    a = coefdir(x,y)
    b = coeford(x,y)
    
    # 2. Graphique
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, label="Données réelles") # Un seul scatter suffit
    plt.plot(Nx, Ny, 'ro', label=f"Point moyen G({round(Nx,1)}, {round(Ny,1)})")
    
    # Droite de régression
    minX, maxX = min(x), max(x)
    plt.plot([minX, maxX], [a*minX + b, a*maxX + b], color="green", label="Régression")
    
    # 3. Texte de l'équation (placé dynamiquement)
    equation = f"y = {round(a,2)}x + {round(b,2)}"
    plt.text(minX, max(y), equation, c="red", fontweight="bold")
    
    # 4. Labels (Attention à la cohérence !)
    plt.title("Nombre de Clients en fonction du Prix")
    plt.xlabel("Prix (€)")
    plt.ylabel("Nombre de clients")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()

def prog():
    x = [i for i in range(5,31,5)]
    y = [84,58,30,19,7,4]
    #print(nuage(x,y))
    #print("moyenne de x :",code.moyenne(x))
    #print("moyenne de y :",code.moyenne(y))
    #print("ecart-type de x:",code.ecart([i for i in range(5,31,5)]))
    #print("ecart-type de y:",code.ecart([84,58,30,19,7,4]))
    #print("La covariance est :",covariance([i for i in range(5,31,5)],[84,58,30,19,7,4]))
    #print("Le coefficient directeur est :",coefdir([i for i in range(5,31,5)],[84,58,30,19,7,4]))
    nuage_affine(x,y)

if __name__ == "__main__":
    prog()


    