#randomly generate a new pair of input lists in range(20)
#check each of our anagram function with each time
#store result for each function for each input pair
#calculate the average runtime for each function

import time
from time import perf_counter

import random
from statistics import mean

def perf_check(k):

    count_res = list()
    count_dict_res = list()
    sort_res = list()
    pure_sort_res = list()
    replace_res = list()

    pairs = listPairGen(20,k)
    #print(pairs)
    for pair in pairs:
        list1 = pair[0]
        list2 = pair[1]
       
        #first the count method
        count_start_time = perf_counter()
        counts = is_anagram_count(list1, list2)
        count_end_time = perf_counter()
        count_res.append(count_end_time - count_start_time)
     
        #now my dictionary method
        dict_start_time = perf_counter()
        dicts = is_anagram_count_dict(list1,list2)
        dict_end_time = perf_counter()
        count_dict_res.append(dict_end_time - dict_start_time)

     
        #now the sort method
        #create copies, so that we don't change data for later methods
        copylist1 = list1.copy()
        copylist2 = list2.copy()
        sort_start_time = perf_counter()
        sorts = is_anagram_sort(copylist1, copylist2)
        sort_end_time = perf_counter()
        sort_res.append(sort_end_time - sort_start_time)
   
        #now do a quick check on the time required just for sorting
        #do this before the replace function, because it changes the lists
        copylist3 = list1.copy()
        copylist4 = list2.copy()
        waypoint_time = perf_counter()
        copylist3.sort()
        copylist4.sort()
        end_time = perf_counter()
        pure_sort_res.append(end_time - waypoint_time)
  
        #now the replace method
        replace_start_time = perf_counter()
        replaces = is_anagram_replace(list1, list2)
        replace_end_time = perf_counter()
        replace_res.append(replace_end_time - replace_start_time)
       
    count_avg = mean(count_res)
    count_dict_avg = mean(count_dict_res)
    sort_avg = mean(sort_res)
    pure_sort_avg = mean(pure_sort_res) 
    replace_avg = mean(replace_res)
    
    print('Average times:\nCount:%f\nAltCount:%f\nSort:%f\nPureSort:%f\nReplace:%f'% (count_avg,count_dict_avg,sort_avg,pure_sort_avg,replace_avg))


def listPairGen(n,k):
    master_lst = list()
    for i in range(n):
        pair = []
        lst1 = []
        for j in range(k):
            lst1.append(random.randint(0,9999))
        lst2 = lst1.copy()
        random.shuffle(lst2)
        pair.append(lst1)
        pair.append(lst2)
        master_lst.append(pair)

    return master_lst
        

###########################################################################  
def is_anagram_replace(list1, list2):
    """Check whether two lists are anagrams, by replacement.

       For each element in the first string, find a match in the second and
       replace it by a null value

       Returns:
           true if lists of same length and all elements replaced
           false otherwise
    """

    if len(list1) != len(list2): #anagrams must be same length
        return False
                                           
    for pos1 in range(len(list1)):      #for each element in list1
        found = False                   #found a match for list1[pos1] yet?
        pos2 = 0
        while pos2 < len(list2) and not found:  #step list2 looking for match
            if list1[pos1] == list2[pos2]:      #if we find the match
                found = True
                list2[pos2] = None              #replace element in the list
            pos2 = pos2 + 1

        if not found:                       #if we didn't find a match
            return False                    #prefix is not in list2

    return True
        
###########################################################################  
def is_anagram_sort(list1, list2):
    """Check whether two lists are anagrams, by sorting and comparing.

       Sort the lists, then step through in parallel checking that the
       elements match

       Returns:
           true if lists of same length and all elements match
           false otherwise
    """

    if len(list1) != len(list2): #anagrams must be same length
        return False

    list1.sort()                   #sort each list
    list2.sort()

    for pos in range(len(list1)):         #step through the lists in parallel
        if list1[pos] != list2[pos]:      #if elements dont match
            return False                  #it can't be an anagram

    return True                          
###########################################################################  
def is_anagram_count(list1, list2):
    """Check whether two lists are anagrams, by counting elements.

       Lists must be composed of elements in {0, ..., 999}
       
       For each element in the alphabet, count +1 for each time it appears
       in the 1st list, and -1 for each time in the second.
       Iterate through the lists in parallel, rather than doing a separate
       sweep for each element

       Returns:
           true if lists of same length and all elements have count 0
           false otherwise
    """

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
###########################################################################  
def is_anagram_count_dict(lst1,lst2):

    if len(lst1)!=len(lst2):
        return False

    d = {}
    
    for i in range(len(lst1)):
        d[lst1[i]] = 0
        d[lst2[i]] = 0     

    for i in range(len(lst1)):
        d[lst1[i]] += 1
        d[lst2[i]] -= 1

    for pos in d:
        if d[pos] != 0:
            return False

    return True
