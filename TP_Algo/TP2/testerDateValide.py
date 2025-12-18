from estBissextile import *

def testerDateValide():
    if(dateValide(2,2,2000)):
        print("test de 02/02/2000 OK")
    else:
        print("test de 02/02/2000 ECHEC")
        
    if(not dateValide(32,1,2000)):
        print("test de 32/01/2000 OK")
    else:
        print("test de 32/01/2000 ECHEC")
        
    if(dateValide(29,2,2000)):
        print("test de 29/02/2000 OK")
    else:
        print("test de 29/02/2000 ECHEC")

    if(not dateValide(29,2,2001)):
        print("test de 29/02/2001 OK")
    else:
        print("test de 29/02/2001 ECHEC")
    
    if(not dateValide(-2,2,2000)):
        print("test de-2/02/2000 OK")
    else:
        print("test de-2/02/2000 ECHEC")

def prog():
    testerDateValide()

if __name__=='__main__':
    prog()