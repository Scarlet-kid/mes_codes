# Exercice 1:
def add_note(L:list[dict]):
    for i in range(len(L)):
        print("Tour de l'élève",L[i]["nom"],L[i]["prenom"])
        laNote=int(input("Sa note:"))
        L[i]["note"] = laNote
    return L

def bestNote(L:list[dict]):
    max = 0
    for i in range(len(L)):
        if L[i]["note"]>max:
            max = L[i]["note"]

    for j in range(len(L)):
        if L[j]["note"] == max:
            print(L[j]["nom"],L[j]["prenom"])
    
    #return max



def prog():
    L=[{"nom":"TOVIEKOU","prenom":"Sosthène"},{"nom":"TOVIEKOU","prenom":"Edgard"},{"nom":"TOVIEKOU","prenom":"Exaucé"},{"nom":"TOVIEKOU","prenom":"Seth"}]
    add_note(L)
    print(bestNote(L))
    
if __name__=="__main__":
    prog()