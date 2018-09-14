from stack import Stack
from myqueue import myQueue

def revQueue(q):
    stk = Stack()
    newq = myQueue()
    qlen = q.length()
    while stk.length() < qlen:
        item = q.dequeue()
        stk.push(item)
    while qlen >= 0:    
        newitem = stk.pop()
        newq.enqueue(newitem)
        qlen -= 1
    return newq


def test():
    """q1 = myQueue()
    q1.enqueue("a")
    q1.enqueue("b")
    q1.enqueue("c")
    print(q1)
    print(revQueue(q1))
    print(q1)"""
    q1 = myQueue()
    q1.enqueue("a")
    q1.enqueue("b")
    q1.dequeue()
    q1.enqueue("c")
    q1.enqueue("e")
    print(q1)
    print(revQueue(q1))
