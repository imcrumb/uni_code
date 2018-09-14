from stack import Stack

def revStack(stk):
    if isinstance(stk,Stack):
        revstk = Stack()
        length = stk.length()
        for i in range(length):
            n = stk.pop()
            revstk.push(n)
        print('revStack:',revstk)
    else:
        print('Error: revStack function requires Stack object')

def corrBrackets(s):
    bStk = Stack()
    openb = ['(','[','{']
    b = {')':'(',']':'[','}':'{'}
    for char in s:
        if char in openb:
            bStk.push(char)
        else:
            top = bStk.top()
            if b[char] == top:
                bStk.pop()
            else:
                return False
    if bStk.is_empty():
        return True 
    return False
        

def test():
    stk = Stack()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    print(stk)
    revStack(stk)
    s = '[({[({})]})]'
    print('corrBrackets:',corrBrackets(s),s)
