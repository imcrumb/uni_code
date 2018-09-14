def isAnagramCountDict(lst1,lst2):

    if len(lst1)!=len(lst2):
        return False

    d = {}
    
    for i in range(len(lst1)):
        if lst1[i] not in d:
            d[lst1[i]] = 0  
        d[lst1[i]] += 1
        #print('i=',i,'step 1:',d)

        if lst2[i] not in d:
            d[lst2[i]] = 0
        d[lst2[i]] -= 1
        #print('i=',i,'step 2:',d)
        
    for pos in d:
        if d[pos] != 0:
            return False

    return True

    
        
def is_anagram_count(list1, list2):

    if len(list1) != len(list2): #anagrams must be same length
        return False

    count_list = [0] * 10000    #the counters for each element in the alphabet

    for i in range(len(list1)):          #step through each position in turn
        elt1 = list1[i]              #element from list1
        count_list[elt1] = count_list[elt1] + 1   #increment counter for elt1
        elt2 = list2[i]              #element from list2
        count_list[elt2] = count_list[elt2] - 1   #decrement counter for elt2

    for pos in count_list:
        if pos != 0:
            return False              #if any element is non-zero

    return True
            

def is_count_dict(lst1,lst2):

    if len(lst1)!=len(lst2):
        return False

    d = {}
    
    for i in range(len(lst1)):
        d[lst1[i]] = 0
        d[lst2[i]] = 0     

    for i in range(len(lst1)):
        d[lst1[i]] += 1
        print('i=',i,'step 1:',d)
        d[lst2[i]] -= 1
        print('i=',i,'step 2:',d)

    for pos in d:
        if d[pos] != 0:
            return False

    return True

    
def c():
    print('This works:\n',is_count_dict([1,2,3],[2,3,1]))
    print('This doesnt work:\n',isAnagramCountDict([1,2,3],[2,3,1]))
        
        
