def mergesort(lst):
    n = len(lst)
    if n > 1:
        lst1 = lst[:n//2]
        lst2 = lst[n//2:]
        mergesort(lst1)
        mergesort(lst2)
        _merge(lst1,lst2,lst)
    return lst

def _merge(lst1,lst2,lst):
    f1 = 0
    f2 = 0
    while f1 + f2 < len(lst):
        if f1 == len(lst1):
            lst[f1+f2] = lst2[f2]
            f2 += 1
        elif f2 == len(lst2):
            lst[f1+f2] = lst1[f1]
            f1 += 1
        elif lst2[f2] < lst1[f1]:
            lst[f1+f2] = lst2[f2]
            f2 += 1
        else:
            lst[f1+f2] = lst1[f1]
            f1 += 1

def test():
    a = [5,7,1,1,2,8,11,8]
    print(mergesort(a))
