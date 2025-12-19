def triInsertion(lst:list)->None:
    tmp : float
    i : int
    j : int
    for i in range(1,len(lst)): # De 1 car on a considérée que c'est le premier élément de la liste qui constitue la partition triée
        tmp = lst[i]
        j = i
        while j > 0 and lst[j-1] > tmp:
            lst[j] = lst[j-1]
            j = j - 1
<<<<<<< HEAD
        lst[j] = tmp

#teste
=======
        lst[j] = tmp
>>>>>>> abf335b (reduct algo trie)
