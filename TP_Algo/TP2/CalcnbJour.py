def estBissextile(year:int):
    return year % 4 and year % 100 or year % 400

def moisValide(mois:int, year:int):
    return 1 <= mois <= 12

def nbJours(mois:int, year:int):
    if mois == 2:
        return 29 if estBissextile(year) else 28
    
    elif mois in (1,3,5,7,8,10,12):
        return 31
    
    elif mois in (4,6,9,11):
        return 30
    
    else:
        return 0 #mois invalide

def dateValide(jour:int, mois:int, year:int):
    if year <= 0:
        return False
    
    if not moisValide(mois):
        return False
    
    if jour < 1:
        return False
    
    return jour <= nbJours(mois, year)

def nbJoursAnnee(year:int):
    return 366 if estBissextile(year) else 365

def joursDepuisAn1(jour:int, mois:int, year:int):
    # Le nombre de jour écoulé entre 01/01/0001 et la date incluse
    total = 0
    
    for a in range(1,year):
        total += nbJoursAnnee(a)
        
    for m in range(1,mois):
        total += nbJours(m,year)
        
    total += jour
    
def nbJoursEntre(j1:int, m1:int, y1:int, j2:int, m2:int, y2:int):
    """Nombre de jours écoulés entrre deus dates valides."""
    if not dateValide(j1,m1,y1) or not dateValide(j2,m2,y1):
        raise ValueError("AU moins une date est invalide.")
    
    d1 = joursDepuisAn1(j1,m1,y1)
    d2 = joursDepuisAn1(j2,m2,y2)
    
    return abs(d2 - d1)

print("Entrez la date numéro 1 :")
jour1 = int(input("Jour : "))
mois1 = int(input("Mois : "))
year1 = int(input("Année : "))

print("Entrez la date numéro 2 :")
jour2 = int(input("Jour : "))
mois2 = int(input("Mois : "))
year2 = int(input("Année : "))

try:
    nbjour = nbJoursEntre(jour1, mois1, year1, jour2, mois2, year2)
    print(f"Il s'est écoulé {nbjour} jour(s) entre {jour1}/{mois1}/{year1} et {jour2}/{mois2}/{year2}.")
except ValueError as e:
    print(e)