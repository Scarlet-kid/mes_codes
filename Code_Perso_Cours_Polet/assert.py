def puissance(x:float,n:int)->float:
    assert type(n) == int, 'type incompatible'
    if n == 0:
        return 1
    else:
        return x * puissance(x,n-1)

print(puissance(3,2.5))

def puissance(x,n):
    res = 1
    for i in range(n):
        res *= x
    return res

print(puissance(2,1))
