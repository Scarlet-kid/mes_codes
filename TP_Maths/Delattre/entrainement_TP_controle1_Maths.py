def diviseur_nombre(nb):
    diviseurs = list()
    for i in range(1, nb + 1):
        if nb % i == 0:
            diviseurs.append(i)
    return diviseurs

def est_Premier(nb):
    return len(diviseur_nombre(nb)) == 2

def catalogue(nb1, nb2):
    nb_premier = list()
    for i in range(nb1, nb2 + 1):
        if est_Premier(i):
            nb_premier.append(i)
    return nb_premier

def ecart(nb1, nb2):
    if est_Premier(nb1) and est_Premier(nb2):
        return nb2 - nb1
    else:
        print('Les nombres passés en paramtre ne sont pas premier')

def twins(nb1,nb2):
    lst = list()
    nb_premier= catalogue(nb1, nb2)
    for i in range(len(nb_premier) - 1):
        lst_2 = []
        if ecart(nb_premier[i],nb_premier[i+1]) == 2:
            lst_2.append(nb_premier[i])
            lst_2.append(nb_premier[i+1])
            lst.append(lst_2)
    return lst

if __name__ == "__main__":
    #print(diviseur_nombre(2))
    #print(est_Premier(4))
    print(catalogue(4,23))
    print(twins(4,23))