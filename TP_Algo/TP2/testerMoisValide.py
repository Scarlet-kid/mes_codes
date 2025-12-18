from estBissextile import moisValide

def testerMoisValide():
    for i in range(13):
        if moisValide(i):
            print(i,"OK")

    if (not moisValide(0)):
        print("Teste OK!")
    else:
        print("Teste échoué")
        
    if (not moisValide(13)):
        print("Teste OK!")
    else:
        print("Teste échoué")

def prog():
    testerMoisValide()

if __name__=="__main__":
    prog()
    