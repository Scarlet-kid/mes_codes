def dichotomie(f,a,b,e):
    
    n = 0
    c = a+b/2
    while f(c) != 0:
        n += 1
        if f(a) * f(c) <0:
            b = c
        else:
            a = c
    return (c,n)
def f(x):
    return x**2 -2

print(dichotomie(f,1,2,0.1))

