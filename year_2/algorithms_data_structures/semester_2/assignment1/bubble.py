def bubblesort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def test():
    a = [5,7,1,1,2,8,11,8]
    print(bubblesort(a))
