def estBissextile(year:int):
    return year%4==0 and year%100!=0 or year%400==0

def moisValide(mois:int):
    return 1 <= mois <= 12

def nbJours(mois:int, year:int):
    if (mois==2 and estBissextile(year)):
        return 29
    
    elif(mois==2 and (not estBissextile(year))):
        return 28
    
    elif(mois==1):
        return 31
    
    elif(mois==3):
        return 31
    
    elif(mois==4):
        return 30
    
    elif(mois==5):
        return 31
    
    elif(mois==6):
        return 30  
    
    elif(mois==7):
        return 31
    
    elif(mois==8):
        return 31
    
    elif(mois==9):
        return 30
    
    elif(mois==10):
        return 31
    
    elif(mois==11):
        return 30
    
    elif(mois==12):
        return 31
    
def dateValide(jour:int,mois:int,year:int):
    if estBissextile(year) and mois==2:
        return moisValide(mois) and 1<=jour<=nbJours(mois,year)
    
    elif not estBissextile(year) and mois==2:
        return moisValide(mois) and 1<=jour<=nbJours(mois,year)
    
    elif mois==1:
        return moisValide(mois) and 1<=jour<=nbJours(mois,year)
    
    elif mois==3:
        return moisValide(mois) and 1<=jour<=nbJours(mois,year)
    
    elif mois==4:
        return moisValide(mois) and 1<=jour<=nbJours(mois,year)
    
    elif mois==5:
        return moisValide(mois) and 1<=jour<=nbJours(mois,year)
    
    elif mois==6:
        return moisValide(mois) and 1<=jour<=nbJours(mois,year)
    
    elif mois==7:
        return moisValide(mois) and 1<=jour<=nbJours(mois,year)
    
    elif mois==8:
        return moisValide(mois) and 1<=jour<=nbJours(mois,year)
    
    elif mois==9:
        return moisValide(mois) and 1<=jour<=nbJours(mois,year)
    
    elif mois==10:
        return moisValide(mois) and 1<=jour<=nbJours(mois,year)
    
    elif mois==11:
        return moisValide(mois) and 1<=jour<=nbJours(mois,year)
    
    elif mois==12:
        return moisValide(mois) and 1<=jour<=nbJours(mois,year)

def utlValideDate():
    
    valide=False
    compt=0
    
    while(valide!=True):
        jour=int(input("Saisir le jour:"))
        mois=int(input("Saisir le mois:"))
        year=int(input("Saisir l'année:"))
        bien=dateValide(jour,mois,year)
        if not(bien):
            print("Il ne s'agit pas d'une date valide.")
            compt+=1
            continue
        else:
            valide=bien
            compt+=1
            print(f"Bravo : la date : {jour}/{mois}/{year} est valide! Nombre de tentative {compt}")
            break
        
        
    
    return f"vous avez eu une date valide en {compt} tentative(s)"

print(utlValideDate())

    