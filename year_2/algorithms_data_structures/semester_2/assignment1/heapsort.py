from random import randint, shuffle

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

def test():
    a = gensorted(10,0)
    b = a
    shuffle(a)
    print("UNSORTED:\n",b,"\n")
    print("SORTED?:\n",heapsort(a),"\n")

    
    
def gensorted(n,k):
    lst = []
    for i in range(n-k):
        lst.append(i)
    pos = randint(0,n-k-1)
    for i in range(n-k,n):
        lst.append(lst[pos])
    return sorted(lst)


