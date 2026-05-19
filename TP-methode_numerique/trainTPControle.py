from matplotlib import pyplot as plt

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
    plt.title("COmparaison des deux suites sur l'imtervalle [0;50]")

def prog():
    print(compare(f1,f2))

if __name__ == "__main__":
    prog()