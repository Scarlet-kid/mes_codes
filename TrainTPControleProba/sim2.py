from code import proba_exacte,Phi
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
def trace_repartition(n,p):
    m,s = n*p, sqrt(n*p*(1-p))
    k = list(range(-2,int(m+4*s)+2))
    F = [proba_exacte(n,p,j) for j in k]
    x= np.linspace(-2,k[-1],400)
    plt.step(k,F,where="post",label="binomiale")
    plt.plot(x,[Phi((t-m)/s) for t in x],label="normale")
    plt.title(f"n={n}, p={p}")
    plt.legend()
    
#le subplot cest pour les sous figures
plt.subplot(1,2,1)
trace_repartition(1000,0.01)
plt.subplot(1,2,2)
trace_repartition(100,0.01)
plt.show()
    
    