def triParInsertion(lst:list) -> None:
    for i in range(1,len(lst)):
        tmp = lst[i]
        j = i
        while j>0 and lst[j-1] > tmp:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = tmp

MaListe = [12,5,3,4,10,11]
triParInsertion(MaListe)
print(MaListe)