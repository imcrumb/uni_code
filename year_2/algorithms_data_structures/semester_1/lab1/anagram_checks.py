def is_anagram_replace():
    
    if len(lst1)!=len(lst2):   #check if lists are the same length
        return False
    
    for pos1 in range(len(lst1)):  #for each position in lst1
        found = False              #init found to false
        pos2 = 0                   #init position in lst2 to 0
        while pos2 < len(lst2)and not found: #while position in lst2 is less than the length of lst2 and a match is not found
            if lst1[pos1] == lst2[pos2]:     #check for a match between position in lst1 to position in lst2
                found = True                 #if match found is true
                lst2[pos2] = None            #replace lst2 item with None
            pos2 += 1                        #increment position in lst2 to check next position

        if not found:              #if a match is not found at any point false is returned
            return False

    return True                    #if each check results in a match at the end then the lists are anagrams

    

def is_anagram_sort(lst1,lst2):
    
    if len(lst1)!=len(lst2):
        return False

    lst1.sort()
    lst2.sort()

    for pos in range(len(lst1)):
        if lst1[pos]!=lst2[pos]:
            return False
        
    return True

def is_anagram_count(lst1,lst2):
    
    if len(lst1)!=len(lst2):
        return False

    count_lst = [0]*10000

    for i in range(len(lst1)):
        elt1 = lst1[i]
        count_lst[elt1] = count_lst[elt1]+1
        elt2 = lst2[i]
        count_lst[elt2] = count_lst[elt2]-1
    
    for pos in count_lst:
        if pos != 0:
            return False
        
    return True
                
