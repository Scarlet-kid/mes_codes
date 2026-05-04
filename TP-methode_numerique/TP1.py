def methode_1(f, a, b, eps, nbIter):
    for i in range(nbIter): 
        c = (a + b) / 2   
        precision_actuelle = abs(b - a)
        if precision_actuelle < eps:
            return (c, precision_actuelle)
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    derniere_precision = abs(b - a)
    return ((c, derniere_precision))

def methode_2(f, a, b, eps, nbIter):
    for i in range(nbIter):
        f_a = f(a)
        f_b = f(b)
        c = a - f_a * (b - a) / (f_b - f_a)
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        precision_actuelle = abs(b - a)
        if precision_actuelle < eps:
            return (c, precision_actuelle)
    return (c, precision_actuelle)

def methode_3(f, x0, eps, nbIter):
    xn = x0
    for i in range(nbIter):
        xn_plus_1 = f(xn)
        precision_actuelle = abs(xn_plus_1 - xn)
        xn = xn_plus_1
        if precision_actuelle < eps:
            return (xn, precision_actuelle)
            
    return (xn, precision_actuelle)

def methode_4(f, df, x0, eps, nbIter):
    xn = x0
    for i in range(nbIter):
        f_prime_xn = df(xn)
        if f_prime_xn == 0:
            break

        xn_plus_1 = xn - f(xn) / f_prime_xn

        precision_actuelle = abs(xn_plus_1 - xn)

        xn = xn_plus_1

        if precision_actuelle < eps:
            return (xn, precision_actuelle)
            
    return (xn, precision_actuelle)

def methode_5(f, a, b, eps, nbIter):
    x_prev = a
    xn = b
    
    for i in range(nbIter):
        f_xn = f(xn)
        f_x_prev = f(x_prev)

        xn_plus_1 = xn - f_xn * (xn - x_prev) / (f_xn - f_x_prev)
        
        precision_actuelle = abs(xn_plus_1 - xn)

        x_prev = xn
        xn = xn_plus_1

        if precision_actuelle < eps:
            return (xn, precision_actuelle)

    return (xn, precision_actuelle)

def comparaison(f, g, df, a, b, eps, nb):
    """
    Affiche un tableau comparatif des précisions pour les 5 méthodes.
    """
    print(f"{'nb_Iter':<8} | {'Méthode_1':<10} | {'Méthode_2':<10} | {'Méthode_3':<10} | {'Méthode_4':<10} | {'Méthode_5':<10}")
    print("-" * 75)

    for i in range(1, nb + 1):
        # On appelle chaque méthode avec i itérations
        # Note : On récupère uniquement la précision (index 1 du tuple de sortie)
        res1 = methode_1(f, a, b, eps, i)[1]
        res2 = methode_2(f, a, b, eps, i)[1]
        res3 = methode_3(g, b, eps, i)[1] # g est la fonction de point fixe
        res4 = methode_4(f, df, b, eps, i)[1]
        res5 = methode_5(f, a, b, eps, i)[1]

        # Formatage scientifique pour correspondre au tableau du TP
        print(f"{i:<8} | {res1:<10.3e} | {res2:<10.3e} | {res3:<10.3e} | {res4:<10.3e} | {res5:<10.3e}")

# --- Paramètres pour tester comme dans le document ---
def f(x): return x**2 - 2
def df(x): return 2*x
def g(x): return 0.5 * (x + 2/x)

# Appel de la fonction
# comparaison(f, g, df, 1, 2, 10**-10, 8)

def df(x): return 2*x

def g(x):
    return 0.5 * (x + 2/x)

def f(x):
    return x**2 - 2
def prog():
    res1 = methode_1(f,1,2,10**-10,8)
    #print(res1)
    res2 = methode_2(f,1,2,10**-10,8)
    #print(res2)
    #print(methode_3(g,2,10**-10,8))
    print(methode_4(f,df,2,10**-10,8))
if __name__ == "__main__":
    prog()
