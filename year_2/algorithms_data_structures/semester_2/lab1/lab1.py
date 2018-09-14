"""
1. Revision

a. Standard methods offered by Priority Queue ADT

-add(key,value) - add a new element to priority queue
-min() - report minimum key value (highest priority)
-remove_min() - remove and return minimum key and value
-is_empty() - return true if no items in priority queue false otherwise
-length() - return number of item in priority queue

b. What are the properties of a binary heap? What are the algorithms for adding
and removing from binary heap?

Binary heap properties:
a binary tree where each node has a lower key than its children
every level (except maybe the last) is complete
the lowest level is always filled from the left

Adding to binary heap:
-create key-value element
-add element at last position pointer
-bubble element up
-if current key < parent key:
-swap
-bubble up parent
-update last position pointer
-update heap size

Removing from binary heap(removing top element):
-extract root value
-copy last element to root
-remove last element
-bubble root element down
-if children
-target = child with min key
-if current key is > target key
-swap element with target
-bubble element down
-update last position pointer
-update heap size

c. What is the array based representation of a binary heap? How do you compute
the index of a nodes parent or children?

Array Based Representation of Binary Heap:
Each node in the heap is given an index in the array-based list starting from
the first node which is labelled 0 and continuing left to right down the tree
assigning increasing indexes

Computing Parent and Children positions:
When all nodes have been assigned their appropriate indexes we can compute
parent and child indexes using the follwing formulae:
-leftchild(i) = 2*i + 1
-rightchild(i) = 2*i + 2
-parent(i) = (i-1)//2
"""
###############################################################################
#bubblesort
###############################################################################

def bubblesort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

###############################################################################
#insertionsort
###############################################################################

def insertion_sort(lst):
    n = len(lst)
    i = 1
    while i < n:
        j = i - 1
        while lst[i] < lst[j] and j > -1:
            j -= 1
        temp = lst[i]
        k = i - 1
        while k > j:
            lst[k+1] = lst[k]
            k -= 1
        lst[k+1] = temp
        i += 1
            
###############################################################################
#selectionsort
###############################################################################

def selection_sort(lst):
    n = len(lst)
    i = 0
    while i < n:
        smallest = i
        j = i+1
        while j < n:
            if lst[j] < lst[smallest]:
                smallest = j
            j += 1
        lsl[i],lst[smallest] = lst[smallest],lst[i]
        i += 1

###############################################################################
#in-place heapsort
###############################################################################

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

            
        
###############################################################################
#test functions
###############################################################################
from time import perf_counter
from random import shuffle
from statistics import mean

def test(inlist):
    n = len(inlist)
    start = perf_counter()
    sortlist = heapsort(inlist)
    stop = perf_counter()
    result = stop - start
    for i in range(n-1):
        if sortlist[i] > sortlist[i+1]:
            print("ERROR: List not sorted!")
            return -1
    return result

def testrandom(n):
    randlist = []
    for i in range(n):
        randlist.append(i)
    shuffle(randlist)
    testtime = test(randlist)
    return testtime

def testaverage(n,number):
    timelist = []
    while number > 0:
        timelist.append(testrandom(n))
        number -= 1
    average = mean(timelist)
    return average
    
    

    






    
