from random import randint
# Utilisateur prend un nombre entre 1 et 99.

# Forcer l'utilisateur a choisir un nombre entre 1 et 99
while True :
    try :
        utl=int(input("Entrez le nombre choisit entre 1 et 99:"))
        assert 1<=utl<=99
                
    except ValueError:
        print("Entrez un nombre svp")
        
    except AssertionError:
        print("Entrez un nombre entre 1 et 99 svp")
        
    else:
        print("Le programme peut continuer")
        break
# ----------------------------------Fin----------------------------------
    
compt:int=0
bot:int=None
min=1
max=99

while (bot!=utl):
    bot:int=(min+max)//2
    compt+=1
    print("Jai choisi {}".format(bot))
    
    try:
        pos=int(input("Plus petit(1),Plus grand(2) ou trouvé(3):"))
        assert pos in (1,2,3)
        
    except (ValueError,AssertionError):
        print("Entrée invalide")
        compt-=1
        continue 
        
    if pos==1:
        max = bot-1
    elif pos==2:
        min= bot+1
    elif pos==3:
        break

print("Juste nombre {} trouvé".format(utl))
print("J'ai trouvé le juste nombre en {} coup(s)".format(compt))
