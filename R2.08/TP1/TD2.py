from code import *

print("moyenne de x :",moyenne([i for i in range(5,31,5)]))
print("moyenne de y :",moyenne([84,58,30,19,7,4]))
print("ecart-type de x:",ecart([i for i in range(5,31,5)]))
print("ecart-type de y:",ecart([84,58,30,19,7,4]))

def covariance(x:list[float],y:list[float]):
    maLong = long(x)
    moyX = moyenne(x)
    moyY = moyenne(y)

    res = 0
    for i in range(long(x)):
        res+=(x[i]*y[i])
    
    return (res/maLong) - (moyX*moyY)

print("La covariance est :",covariance([i for i in range(5,31,5)],[84,58,30,19,7,4]))

def coefdir(x:list[float],y:list[float])->float:
    return covariance(x,y)/variance(x)

print("Le coefficient directeur est :",coefdir([i for i in range(5,31,5)],[84,58,30,19,7,4]))

def coeford(x:list[float],y:list[float]):
    pass



    