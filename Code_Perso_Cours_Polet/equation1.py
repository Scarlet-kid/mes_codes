def solveEq1(a,b):
    if a==0:
        raise Exception("coefficient degre 1 nul")
    else:
        return -b/a

def prog():
    va = float(input("a?:"))
    vb = float(input("b?:"))
    try:
        x = solveEq1(va, vb)
        print('la solution est : ', x)

    except Exception as e:
        print(e,',l\' equation n\' admet pas de solution')

if __name__ == '__main__':
    prog()