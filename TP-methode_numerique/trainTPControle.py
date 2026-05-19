from matplotlib import pyplot as plt
from math import sqrt,pi,e

def f1(n):
    return -3 * n**2 + 2 * n + 100

def f2(n):
    return -3*n**2

def compare(f, g):
    lst = [10, 100, 1000, 10000, 100000, 1000000]
    for elt in lst:
        print("n = ",elt)
        print("\t","f1(n) = ",f1(elt))
        print("\t","f2(n) = ",f2(elt))

def graphe1():
    plt.figure()
    lst = [i for i in range(51)]
    plt.title("Comparaison des deux suites sur l'imtervalle [0; 50]")
    plt.plot(lst, [f1(i) for i in range(51)],label="-3x^2 -2x + 100", linestyle="-",color = "red")
    plt.plot(lst, [f2(i) for i in range(51)], label = "-3x^2",marker = ".", linestyle = "None", color = "blue")
    plt.legend()
    plt.show()

def graphe1():
    plt.figure()
    lst = [i for i in range(51)]
    plt.title("Comparaison des deux suites sur l'imtervalle [0; 50]")
    plt.plot(lst, [f1(i) for i in range(51)],label="-3x^2 -2x + 100", linestyle="-",color = "red")
    plt.plot(lst, [f2(i) for i in range(51)], label = "-3x^2",marker = ".", linestyle = "None", color = "blue")
    plt.legend()
    plt.show()

def f3(n):
    return (n+1)/(sqrt(n)+1)

def f4(n):
    return sqrt(n)

def graphe2():
    plt.figure()
    lst = [i for i in range(1001)]
    plt.title("Comparaison des deux suites sur l'imtervalle [0 : 1000]")
    plt.plot(lst, [f3(i) for i in range(1001)],label="n+1/sqrt(n)+1", linestyle="-",color = "red")
    plt.plot(lst, [f4(i) for i in range(1001)], label = "sqrt(n)",marker = ".", linestyle = "None", color = "blue")
    plt.legend()
    plt.show()

def f5(n):
    return (3*n -1)/(n**2+n+1)
def f6(n):
    return 3/(n)

def graphe3():
    plt.figure()
    lst = [i for i in range(1,31)]
    plt.title("Comparaison des deux suites sur l'imtervalle [1 : 30]")
    plt.plot(lst, [f5(i) for i in range(1,31)],label="(3n-1)/n^2 + n + 1", linestyle="-",color = "red")
    plt.plot(lst, [f6(i) for i in range(1,31)], label = "3/n",marker = ".", linestyle = "None", color = "blue")
    plt.legend()
    plt.show()

def graphe4():
    plt.figure()
    lst = [i for i in range(501)]
    plt.title("Comparaison des deux suites sur l'imtervalle [0 : 501]")
    plt.plot(lst, [(n**2-n+1)/(n**2+n+1) for n in range(501)],label="(n**2-n+1)/(n**2+n+1)", linestyle="-",color = "red")
    plt.plot(lst, [1 for i in range(501)], label = "1",marker = ".", linestyle = "None", color = "blue")
    plt.legend()
    plt.show()

def factoriel(n):
    rep = 1
    for i in range(1,n+1):
        rep *= i
    return rep

def stirling(n):
    return (sqrt(2*pi*n)) * ((n/e)**n)

def graphe5():
    plt.figure()
    lst = [3,10,25]
    plt.title("Comparaison des deux suites sur l'imtervalle [0 : 501]")
    plt.plot(lst, [factoriel(n) for n in (lst)],label="n!", linestyle="-",color = "red")
    plt.plot(lst, [stirling(n) for n in (lst)], label = "(sqrt(2*pi*n)) * ((n/e)**n)",marker = ".", linestyle = "None", color = "blue")
    plt.legend()
    plt.show()


def prog():
    #print(compare(f1,f2))
    #print(graphe1())
    #print(graphe2())
    #print(graphe3())
    #print(graphe4())
    print(graphe5())
if __name__ == "__main__":
    prog()