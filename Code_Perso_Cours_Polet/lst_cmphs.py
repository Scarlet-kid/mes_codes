if __name__ == "__main__":
    maListe = [x**3 for x in [y for y in range(1,11) if y%2==0] if (x**3)%3==0]
    #print(maListe)
    maListe = [(x, y, x and y) for x in [True, False] for y in [True, False]]
    print(maListe)