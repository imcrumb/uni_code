from time import perf_counter
from math import floor

def test():
    a=read_garda_stations_tuples()

    copy_start = perf_counter()
    b=copyList(a)
    copy_end = perf_counter()

    rev_start = perf_counter()
    c=revList(a)
    rev_end = perf_counter()

    linear_start = perf_counter()
    d = linear_search(a,'Youghal')
    linear_end = perf_counter()

    binary_start = perf_counter()
    e = binary_search(a,'Youghal')
    binary_end = perf_counter()

    copy_time = copy_end - copy_start
    rev_time = rev_end - rev_start
    linear_time = linear_end - linear_start
    binary_time = binary_end - binary_start
    
    print('Append:',copy_time,'\nInsert:',rev_time,'\nLinear:',linear_time,'\nBinary:',binary_time)
    

def read_garda_stations_tuples():
    """ Read and return a list of garda stations. """
    all_stations = []
    file = open('garda_stations.txt', 'r')
    for line in file:
        line = line.replace('\n','')
        new_tuple = tuple(line.split('\t'))
        all_stations.append(new_tuple)
    file.close()
    return all_stations

def copyList(lst):
    copy = []
    for item in lst:
        copy.append(item)
    return copy
        
def revList(lst):
    rev = []
    for item in lst:
        rev.insert(0,item)
    return rev
    
def linear_search(lst,station):
    for item in lst:
        if item[0] == station:
            return True
    return False

def binary_search(lst,station):
    lo = 0
    hi = len(lst) - 1

    while lo <= hi:
        i = floor((hi+lo)/2)
        if lst[i][0] == station:
            return True
        if lst[i][0] < station:
            lo = i+1
        else:
            hi = i-1
    return False
    
def py_sort(lst):
    return lst.sort(key=lambda x:int(x[2]),reverse=True)


        
    
