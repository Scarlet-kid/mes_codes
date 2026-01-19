def f(a:int, b:int)->None :
    c:int
    c=a
    a=b
    b=c

def prog()->None :
    a:int
    b:int
    a=5
    b=10
    print("a= ",a,"b= ",b)
    f(a,b)
    print("a= ",a,"b= ",b)

if __name__=="__main__":
    prog()