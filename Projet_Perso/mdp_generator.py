import string
import random 
def generer_password(longeur):
    all = string.printable
    var = ""
    for i in range(longeur):
        var += random.choice(all)
    return var

print(generer_password(12))