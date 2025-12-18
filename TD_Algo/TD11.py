class Instant:
    def __init__(self,heure:int=0,minute:int=0,seconde:int=0):
        self.heure=heure
        self.minute=minute
        self.seconde=seconde
    
    def __str__(self):
        return f'{self.heure}:{self.minute}:{self.seconde}'
    
    """def __lt__(self, other):
        return (self.h, self.m, self.s) < (other.h, other.m, other.s)
"""
    
    """def print_Instant2(self):
        return f'{self.heure}h {self.minute}:min {self.seconde}:s'"""

"""def  read_Instant()->Instant:
    heure=input("Heure:")
    minute=input("Minute:")
    seconde=input("Seconde:")
    instant=Instant(heure,minute,seconde)
    return f'{instant.heure} {instant.minute} {instant.seconde}'
"""

def  read_Instant2()->Instant:
    heure=int(input("Saisir l'heure:"))
    minute=int(input("Saisir la minute:"))
    seconde=int(input("Saisir la seconde:"))
    return Instant(heure,minute,seconde)

#print(read_Instant())
#print(read_Instant2())

def print_Instant(t:Instant):
    return f'{t.heure}h{t.minute}:min{t.seconde}:s'

def estInstantValide(t :Instant)->bool:
    return (0<=t.heure<=23 and 0<=t.minute<=59 and 0<=t.seconde<=59)

#t=read_Instant2()
#print(print_Instant(t))
#print(t.print_Instant2())
#print(estInstantValide(t))

"""instant=Instant()
print(instant.read_Instant())"""

#print(instant)
"""print(instant.heure,instant.minute,instant.seconde)
demain=Instant()
print(demain.heure,demain.minute,demain.seconde)"""

def suivant(t:Instant)->Instant:
    t.seconde += 1
    return t

def estPlusRecent(t1:Instant, t2:Instant)->bool:
    if t1.heure > t2.heure:
        return True
    elif t1.heure < t2.heure:
        return False
    else:
        if t1.minute > t2.seconde:
            return True
        elif t1.minute < t2.seconde:
            return False
        else:
            if t1.seconde > t2.seconde:
                return True
            elif t1.seconde < t2.seconde:
                return False
            else:
                return 'Les deux instants sont égaux'
            
def estPlusRecent(t1: Instant, t2: Instant) -> bool:
    return (t1.h, t1.m, t1.s) > (t2.h, t2.m, t2.s)

def duree(debut: Instant, fin: Instant) -> Instant:
    s_debut = debut.heure * 3600 + debut.minute * 60 + debut.seconde
    s_fin   = fin.heure * 3600 + fin.minute * 60 + fin.seconde

    diff = s_fin - s_debut
    if diff < 0:
        raise ValueError("fin doit être plus récent que debut")

    h = diff // 3600 # Le nombre d'heure car 1h=3600 secondes . le reste cest pour les secondes et les minutes.
    diff %= 3600 # Pour avoir ce qui reste pour les minutes et les secondes.
    m = diff // 60 # Le nombre de minute qu'on peut avoir car 1min=60s. le reste cest pour les econdes.
    s = diff % 60 # Le reste qui est pour les secondes.
    return Instant(h, m, s)


if __name__=='__main__':
    t1=read_Instant2()
    #suivant(t)
    #print(t)
    t2=read_Instant2()
    #print(estPlusRecent(t1, t2))
    

