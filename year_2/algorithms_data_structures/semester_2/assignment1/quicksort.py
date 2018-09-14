#in-place quicksort

def quicksort(lst,first,last):
    if last > first:
        pivot = lst[first]
        f = first + 1
        b = last
        while f <= b:
            while f <= b and lst[f] < pivot:
                f += 1
            while f <= b  and lst[b] > pivot:
                b -= 1
            if f <= b:
                lst[f],lst[b] = lst[b],lst[f]
                f += 1
                b -= 1
        lst[b],lst[first] = lst[first],lst[b]
        quicksort(lst, first, b-1)
        quicksort(lst, b+1, last)

def test():
    a = [2,5,7,2,3,4,6,1]
    end = len(a)-1
    quicksort(a,0,end)
    return a
        
