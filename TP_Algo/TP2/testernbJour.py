from estBissextile import *

def testerNbJours():
    if(nbJours(1,2000)==31):
        print("test de 01/2000 OK")
    else:
        print("test de 01/2000 ECHEC")
    if(nbJours(2,2000)==29):
        print("test de 02/2000 OK")
    else:
        print("test de 02/2000 ECHEC")
    if(nbJours(2,2001)==28):
        print("test de 02/2001 OK")
    else:
        print("test de 02/2001 ECHEC")
    if(nbJours(3,2000)==31):
        print("test de 03/2000 OK")
    else:
        print("test de 03/2000 ECHEC")
    if(nbJours(4,2000)==30):
        print("test de 04/2000 OK")
    else:
        print("test de 04/2000 ECHEC")
    if(nbJours(5,2000)==31):
        print("test de 05/2000 OK")
    else:
        print("test de 05/2000 ECHEC")
    if(nbJours(6,2000)==30):
        print("test de 06/2000 OK")
    else:
        print("test de 06/2000 ECHEC")
    if(nbJours(7,2000)==31):
        print("test de 07/2000 OK")
    else:
        print("test de 07/2000 ECHEC")
    if(nbJours(8,2000)==31):
        print("test de 08/2000 OK")
    else:
        print("test de 08/2000 ECHEC")
    if(nbJours(9,2000)==30):
        print("test de 09/2000 OK")
    else:
        print("test de 09/2000 ECHEC")
    if(nbJours(10,2000)==31):
        print("test de 10/2000 OK")
    else:
        print("test de 10/2000 ECHEC")
    if(nbJours(11,2000)==30):
        print("test de 11/2000 OK")
    else:
        print("test de 11/2000 ECHEC")
    if(nbJours(12,2000)==31):
        print("test de 12/2000 OK")
    else:
        print("test de 12/2000 ECHEC")

def prog():
    testerNbJours()

if __name__=="__main__":
    prog()