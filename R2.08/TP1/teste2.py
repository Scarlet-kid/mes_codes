import matplotlib.pyplot as plt
from numpy import mean, linspace

def cov(lst_x,lst_y):
    lst_xiyi=[]
    for i in range(len(lst_x)):
        lst_xiyi.append(lst_x[i]*lst_y[i])
    return mean(lst_xiyi)-mean(lst_x)*mean(lst_y)
    
def var(lst_x):
    lst_carres=[x**2 for x in lst_x]
    return mean(lst_carres)-mean(lst_x)

def nuage(lst_x, lst_y):

    a=cov(lst_x,lst_y)/var(lst_x)
    b=mean(lst_y)-a*mean(lst_x)

    x_t=linspace(5,30,100) # x de 5 à 30
    y_t=a*x_t+b

    # affiche un nuage de points
    plt.scatter(lst_x, lst_y)
    plt.xlabel('x')
    plt.ylabel('y')
    #plt.grid()
    
    plt.plot(mean(lst_x),mean(lst_y),'ro',c='green')

    """
    Pour calculer y=ax+b:
    =====================

    a=cov(x,y)/var(x)
    b=moy(y)-a*moy(x)

    variance(x)=moyenne des carrés - carré de la moyenne
    covariance(x,y)=moyenne des xi*yi - moy(x)*moy(y)
    """

    
    
    #fig,ax=plt.subplots()   
    plt.plot(x_t,y_t, color="red")
    plt.show()

def main():
    x=[5,10,15,20,25,30]
    y=[84,58,30,19,7,4]

    var(x)
    nuage(x,y)


if __name__ == "__main__":
    main()