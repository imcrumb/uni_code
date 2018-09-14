from stack import Stack
from random import randint
from time import time

def makeBlocks(n):
    blocklst = []
    for i in range(n):
        block = randint(0,2)
        blocklst.append(block)
    return blocklst

def stackTetris():
    stk = Stack()
    colours = {0:"Red",1:"Blue",2:"Green"}
    blocks = makeBlocks(5)
    score = 0
    top = None

    for block in blocks:
        clock_start = time()
        choice = input("%s?"%colours[block])
        clock_end = time()
        limit = clock_end - clock_start
        #print(limit)
        if limit > 5:
            stk.push(block)
        elif choice == "y":
            stk.push(block)
            if block == top:
                stk.pop()
                stk.pop()
                score += 1
            top = block
    #score -= stk.length()       
    score = max(score - stk.length(),0)
    
    print("Your score:%i"%score)
            
