class Instant:
    def __init__(self, heure=0, minute=0, seconde=0):
        self.heure=heure
        self.minute=minute
        self.seconde=seconde

    def __str__(self):
        return f'{self.heure:02} {self.minute:02} {self.seconde:02}'

    def __int__(self):
        return 3600*self.heure+60*self.minute+self.seconde

    def isValid(self):
        pass

    def __ge__(self, other)->bool: # est ce que self est plus recent que other?
        if self.heure>other.heure:
            return True
        elif self.heure > other.heure:
            return False
        elif self.minute>other.minute:
            return True

    def __sub__(self, other):
        sec = self.seconde-other.seconde
        rm=0
        rh=0

    def oneSecMore(self):
        return self+Instant(0,0,1)

    def duration(self,other):
        if self>=other:
            return self-other
        else:
            print("On permute")
            return other-self

    def __add__(self, t1,t2):
        sec=t1.seconde+t2.seconde
        rm = 0
        rh=0
        if sec>59:
            sec=sec-60
            rm=1
        minu = t1.minute+t2.minute+rm
        if minu>59:
            minu=minu-60
            rh=1
        hr=t1.heure+t2.heure+rh
        if hr>23:
            hr=hr-24
        return Instant(hr,minu,sec)



def read_instant():
    heure = int(input("heure:"))
    minute = int(input("minute:"))
    seconde = int(input("seconde:"))
    return (Instant(heure, minute, seconde))

def print_Intant(inst)->None:
    print(inst)

now = read_instant()
duration = read_instant()
newTime = now.__add__(duration)
print(newTime)

