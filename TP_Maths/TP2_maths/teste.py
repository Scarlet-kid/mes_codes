def concatene(A:list[list[int]],B:list[int]):
    r=[]
    for i in range(len(A)):
        r.append(A[i] + [B[i]])
    return r

def affichage2(l:list):
    return f'x = {l[0]}, y = {l[1]}, z = {l[2]}'