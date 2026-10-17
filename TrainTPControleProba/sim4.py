import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from code import densite  # fct densite(x, m, sigma) de la q4
valeurs = [1, 5, 20, 100]
probas = [0.80, 0.15, 0.04, 0.01]
np.random.seed(3)
tailles = [5,30,300]
for i in range(3):
    n = tailles[i]
    M=[np.mean(np.random.choice(valeurs,n,p=probas)) for j in range(10000)]
    x = np.linspace(min(M),max(M),300)
    plt.subplot(1,3,i+1)
    plt.hist(M,bins=50,density=True)
    plt.plot(x,[densite(t,3.35,10.46/sqrt(n)) for t in x])
    plt.title(f"n={n}")
    print(n,len([t for t in M if t <=3.35])/10000)
    
plt.show()