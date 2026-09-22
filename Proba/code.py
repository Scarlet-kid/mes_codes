import random
import matplotlib.pyplot as plt
import numpy
lstSomme = []
lstHist = []
x = numpy.array(3,20) -0.5
for j in range(1000):
    for i in range(3):
        lstSomme.append(random.randint(1,6))
    lstHist.append(sum(lstSomme))
    lstSomme.clear()
plt.hist(lstHist,bins=x)
plt.show()