# def saisirNotesPromo(lstP:list[dict])->None:
#     for etu in lstP:
#         print("Saisir la note de :",etu["nom"],etu["prenom"],":")
#         etu["note"] = float(input())
# 
# 
# def meilleureNote(lstP:list[dict])->list[tuple]:
#     res = [(lstP[0]["nom"],lstP[0]["prenom"])]
#     bestNote = lstP[0]["note"]
#     for i in range(1,len(lstP)):
#         if lstP[i]["note"] > bestNote:
#             res = [(lstP[i]["nom"],lstP[i]["prenom"])]
#             bestNote = lstP[i]["note"]
#         elif lstP[i]["note"] == bestNote:
#             res.append((lstP[i]["nom"],lstP[i]["prenom"]))
#     return res
#             
# 
# laPromo = [{"nom":"Onyme","prenom":"Anne"},
#            {"nom":"Dupont","prenom":"Jean"}
#            ]
# print(laPromo)
# saisirNotePromo(laPromo)
# print(laPromo)
# meilleureNote((laPromo))
# print(laPromo)
from random import randint
# def Frequence(notes:list[float])->list[int]:
#     re:list[int] = [0]*21
#     for valeur in notes:
#         res[int(valeur)] = res[int(valeur)]+1
#     return res
# mesNotes = []
# for i in range(25):
#     mesNotes[i] = randint(0,200)/10
# print(mesNotes)
# print(Frenquence(mesNotes))
mesNotes = [i for i in range(10)]
print(mesNotes[::2])



    
