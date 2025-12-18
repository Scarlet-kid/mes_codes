from estBissextile import estBissextile

def testerBissextile():
    
    if(estBissextile(2016)):
        print("test de 2016 OK")
    else:
        print("test de 2016 ECHEC")
        
    if(estBissextile(2008)):
        print("test de 2008 OK")
    else:
        print("test de 2008 ECHEC")
        
    if(not estBissextile(1900)):
        print("test de 1900 OK")
    else:
        print("test de 1900 ECHEC")
        
    if(estBissextile(2000)):
        print("test de 2000 OK")
    else:
        print("test de 2000 ECHEC")
    
    if(estBissextile(2001)):
        print("test de 2001 OK")
    else:
        print("test de 2001 ECHEC")

def prog():
    testerBissextile()

if(__name__=="__main__"):
    prog()