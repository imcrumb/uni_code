from random import randint, shuffle
from time import perf_counter


###############################################################################

def evaluate():

    evaluateall(100,0,10)
    evaluateall(1000,0,100)
    evaluateall(10000,0,1000)
    evaluateall(100000,0,10000)
    evaluateall(100,20,10)
    evaluateall(1000,200,100)
    evaluateall(10000,2000,1000)
    evaluateall(100000,20000,10000)
    evaluateall(100,70,10)
    evaluateall(1000,700,100)
    evaluateall(10000,7000,1000)
    evaluateall(100000,70000,10000)

def evaluateall(n,k,p):

    #base list creation
    sortedlst = gensorted(n,k)
    sortedcopy1 = sortedlst[:]
    sortedcopy2 = sortedlst[:]
    sortedcopy3 = sortedlst[:]
    reverselst = sortedcopy1[::-1]
    partiallst = genpartial(sortedcopy2,n,p)
    randomlst = genrandom(sortedcopy3)

    flist = [bubblesort,heapsort,mergesort,quicksort]
    
    if n > 10000:
        flist = flist[1:4]

    #sorted list check
    sortedcheck = test(sortedlst[:],flist)
    i = 0
    print("\nSorted List")
    for result in sortedcheck:
        print(sortedcheck[flist[i].__name__],"sorted",flist[i].__name__,n,k,p)
        i += 1

    #reverse list check
    reversecheck = test(reverselst[:],flist)
    i = 0
    print("\nReversed List")
    for result in reversecheck:
        print(sortedcheck[flist[i].__name__],"reversed",flist[i].__name__,n,k,p)
        i += 1

    #partial list check
    partialcheck = test(partiallst[:],flist)
    i = 0
    print("\nPartial List")
    for result in partialcheck:
        print(partialcheck[flist[i].__name__],"partial",flist[i].__name__,n,k,p)
        i += 1

    #random list check
    randomcheck = test(randomlst[:],flist)
    i = 0
    print("\nRandom List")
    for result in randomcheck:
        print(randomcheck[flist[i].__name__],"random",flist[i].__name__,n,k,p)
        i += 1

        
def test(lst,flist):
    results = {}
    for f in flist:
        copylst = lst[:]
        start = perf_counter()
        resultlst = f(copylst)
        fin =  perf_counter()
        lstsorted = issorted(copylst,resultlst)
        if lstsorted:
            time = fin - start
            results[f.__name__] = time
        else:
            results[f.__name__] = None
    return results
            

def issorted(lst,other):
    if sorted(other) == lst:
        return True
    return False


def gensorted(n,k):
    lst = []
    for i in range(n-k):
        lst.append(i)
    pos = randint(0,n-k-1)
    for i in range(n-k,n):
        lst.append(lst[pos])
    return sorted(lst)

def genpartial(lst,n,p):
    for i in range(p):
        i1,i2 = randint(0,n-1),randint(0,n-1)
        lst[i1],lst[i2] = lst[i2],lst[i1]
    return lst

def genrandom(lst):
    shuffle(lst)
    return lst
    
###############################################################################
    
def bubblesort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

#-------------------------------------------------------------------------------

def heapsort(lst):
    n = len(lst)
    last = 1
    while last < n:
        bubbleup(last,lst)
        last += 1
    last -= 1
    while last > 0:
        lst[0],lst[last] = lst[last],lst[0]
        last -= 1
        bubbledown(0,last,lst)
    return lst
        
    
def bubbleup(i,lst):
    parent = (i-1)//2
    if parent >= 0 and lst[i] > lst[parent]:
        lst[parent] , lst[i] = lst[i], lst[parent]
        bubbleup(parent,lst)
        
        
def bubbledown(i,last,lst):
    left = (2*i)+1
    right = (2*i)+2
    if left < last and right <= last:
        if lst[left] >= lst[right] and lst[i] < lst[left]:
            lst[i],lst[left] = lst[left],lst[i]
            bubbledown(left,last,lst)
        elif lst[right] >= lst[left] and lst[i] < lst[right]:
            lst[i],lst[right] = lst[right],lst[i]
            bubbledown(right,last,lst)      
    elif left <= last and lst[i] < lst[left]:
        lst[i],lst[left] = lst[left],lst[i]
        bubbledown(left,last,lst)
    elif right <= last and lst[i] < lst[right]:
        lst[i],lst[right] = lst[right],lst[i]
        bubbledown(right,last,lst)
        
#------------------------------------------------------------------------------
        
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

#------------------------------------------------------------------------------

def quicksort(lst):
    n = len(lst)
    for i in range(len(lst)):
        j = randint(0,n-1)
        lst[i],lst[j] = lst[j],lst[i]
    _quicksort(lst,0,n-1)
    return lst

def _quicksort(lst,first,last):
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
        _quicksort(lst, first, b-1)
        _quicksort(lst, b+1, last)

###############################################################################
