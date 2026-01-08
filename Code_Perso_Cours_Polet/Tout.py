
import random
import math
# La notion de déballage
"""str1 = "hello wolrd"
a,b,c,d,e,f,g,h,i,j,k=str1
print('a=',a,"c=",c,'k=',k)"""

"""def calculB(x:int)->int:
    if(x<0):
        return-x
    else:
        return x
def calculA(x:int)->int:
    return 2*calculB(x)
def prog():
    x = calculA(-2)
    print("x=",x)
if(__name__=="__main__"):
    prog()"""
    
"""def somme(n:int)->int:
    if(n>1):
        return n+somme(n-1)
    else:
        return n
def prog():
    print(somme(4))
if(__name__=="__main__"):
    prog()"""

"""def isSorted(tab:list)->bool:
   
    ok:bool 
    i:int
    ok=True
    i = 1
    while i<len(tab) and ok :
        if(tab[i-1]<=tab[i]):
        # on avance dans le tableau
            i = i+1
        else:
            #on sait que tab n'est pas trié
            ok = False
    return ok

if(__name__=="__main__"):
    print(isSorted([1,2,3,4,5]))"""
    
"""def triInsertion(lst:list):
    tmp:float
    i:int
    j:int
    for i in range(1,len(lst)):
        tmp=lst[i]
        j=i
        while j>0 and lst[j-1]>tmp:
            lst[j]=lst[j-1]
            j=j-1
        lst[j] = tmp 
if __name__ == "__main__":
    tab=[6,3,5,7,2]
    print(triInsertion(tab))
    print(tab)"""


"""def construireListe(taille:int,valeur:float):
    res = []
    for i in range(0,taille):
        res.append(valeur)
    return res
print(construireListe(10,random.randint(0,9)))"""

"""def intercal(a,b):
    a_str=str(a)
    b_str= str(b)
    return a_str[0]+b_str+a_str[1]
print(intercal(56,21))"""

def number(a,b):
    utl=int(input((f"Saisir un entier entre {a} et {b}:")))
    while not a<=utl<=b:
        utl=int(input((f"Saisir un entier entre {a} et {b}:")))
    return utl
#print(number(1,9))

def Valeur_absolu(a):
    if a<0:
        return -a
    if a>0:
        return a
    else:
        return a

def equaPremierDegre(a,b):
    if b>0:
        return -b/a
    if b<0:
        return b/a
    else:
        return 0

"""def table():
    for i in range(11):
        print(i,end="\t")
    for j in range(11):
        print(j)
    print(i*j,end="")

print(table()) # A revoir comme code."""

"""def etoile(c):
   for i in range(c):
       e = "*" * (c-i)
       point = "."*i
       print(e+point)
       
print(etoile(6))"""

"""def afficher_table_multiplication():
    # En-tête
    print("   X", end="")
    for i in range(11):
        print(f"{i:>4}", end="")
    print()

    # Corps du tableau
    for i in range(11):
        print(f"{i:>4}", end="")
        for j in range(11):
            print(f"{i * j:>4}", end="")
        print()

afficher_table_multiplication()"""

"""def fibonacci_iteratif(n):
    if n==0:
        return 0
    if n==1:
        return 1
    a,b=0,1
    for _ in range(2,n+1):
        a,b=b,a+b
    return b
print((fibonacci_iteratif(10)))"""


def recherche_dichotomique(tab,valeur):
    debut=0
    fin=len(tab)-1
    while(debut<=fin):
        milieu = (debut+fin)//2
        if tab[milieu] == valeur:
            return milieu
        if tab[milieu] < valeur:
            debut = milieu + 1
        else:
            fin = milieu -  1
    return -1

liste = [1, 3, 5, 7, 9, 11, 13]
print(recherche_dichotomique(liste, 7))  # Affiche 3

#fonction partie entière itérative pour x réel

def pe(x):
    i=0
    if x>=0:
        while i<=x:
            i=i+1
        return i-1
    else:
        while i>=x:
            i=i-1
    return i
#partie entière récursive pour x réel positif
def per(x):
    if 0<=x<1:
        return 0
    else:
        if x>=1:
            return per(x-1)+1
        else:
            return per(x+1)-1
        
def points(x):
    if x<40:
        return 0
    else:
        return pe((x-30)/10)*5

def de(x,y):
   if y==0:
      return False
   else:
      return pe(x/y),x-y*pe(x/y)

def minimum(A):
   a=A[0]
   for i in A:
      if i<a:
         a=i
   return a

def appartient(A,x):
   i=0
   while x!=A[i] and i <=len(A)-2:
      i+=1
   if x==A[i]:
      return True
   else:
      return False
  
def appartient(A,x):
   i=0
   while x!=A[i] and i <=len(A)-2:
      i+=1
   if x==A[i]:
      return True
   else:
      return False
  
def recherchr_dichotomique(liste:list,n:int):
    debut=0
    fin=len(liste)-1
    while(debut<=fin):
        milieu = (debut+fin)//2
        if liste[milieu] == n:
            return milieu
        if liste[milieu]<n:
            debut=milieu+1
        else:
            fin=milieu-1
    return -1