# def palindrome(s:str)->bool:
#     i:int
#     ok=True
#     i=0
#     while i<=len(s)//2 and ok:
#         if(s[i]!=s[-1-i]):
#             ok = False
#         i += 1
#     return ok
# def palindromeR(s:str)->bool:
#     if len(s)<2:
#         return True
#     if s[0] == s[-1]:
#         return palindromeR(s[1:-1])
#     else:
#         return False


# def combien(s1:str)->int:
#     def combien(s1:str,s2:str)->int:
#     cpt=0
#     i=0
#     while i<=len(s1)-len(s2):
#         if(s1[i] == s2[0]):
#             j=1
#             ok=True
#             while ok and j<len(s2):
#                 if(s1[i+j]!=s2[j]):
#                     ok = False
#                 else:
#                     j+=1
#             if(ok):
#                 cpt+=1
#         i+=1
#     return cpt
# Apres réécrire une fonction qui fait la meme chose de maniere récuresive

# def Voyelle(s:str):
#     voy = ['a','e','o','y','i','u']
#     cpt = 0
#     for i in s:
#         if i in voy:
#             cpt+=1
#     return cpt
# def VoyelleMR(ch):
#     voy:list
#     voy='aeiouyAEIOUY'
#     cpt = 0
#     for lettre in ch:
#         if (lettre in voy):
#             cpt+=1
#     return cpt
            

# def Convertie(s:str):
#     for i in s:
#         print(i.lower(),end='')
# 
# def Convertie2(s):
#     lst=[]
#     for lettre in s:
#         lst.append(lettre.lower())
#     m = "".join(lst)   
#     return m
# 
# def maj2minus(ch):
#     delta = ord('a')-ord('A')
#     res=""
#     for lettre in ch:
#         if lettre<='Z' and lettre>='A':
#             car = chr(ord(lettre)+delta)
#         else:
#             car = lettre
#         res = res+car
#     return res

def anagramme(s1:str,s2:str)->bool:
    # Photo de mon tel
def communes(s1,s2):
    # A faire
        
                

if __name__ == "__main__":
    print(anagramme('chine','nichp'))
