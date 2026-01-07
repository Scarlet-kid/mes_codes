def triInsertion(lst: list) -> None:
    for i in range(1, len(lst)):
        tmp = lst[i]
        j = i
        while j > 0 and lst[j - 1] > tmp:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = tmp
