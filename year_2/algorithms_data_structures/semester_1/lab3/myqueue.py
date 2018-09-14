class myQueue:
    def __init__(self):
        self._body = [None]*8
        self._head = 0
        self._tail = 0
        self._size = 0
        
    def enqueue(self,item):
        if self._size == 0:
            self._body[0] = item
            self._size = 1
            self._tail = 1
        else:
            self._body[self._tail] = item
            self._size += 1
            if self._size == len(self._body):
                self.grow()
            elif self._tail == len(self._body) - 1:
                self._tail = 0
            else:
                self._tail += 1
                    
    def dequeue(self):
        if self._size == 0:
            return None
        item = self._body[self._head]
        self._body[self._head] = None
        if self.length()/len(self._body) <= 0.25:
            self.shrink()
        if self._size == 1:
            self._head = 0
            self._size = 0
            self._tail = 0
        elif self._head == len(self._body) - 1:
                self._head = 0
                self._size -= 1
        else:
            self._head += 1
            self._size -= 1

        return item

    def first(self):
        return self._body[self._head]

    def length(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def grow(self):
        oldbody = self._body
        self._body = [None]*(2*self._size)
        oldpos = self._head
        pos = 0
        if self._head < self._tail:
            while oldpos <= self._tail:
                self._body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None
                pos += 1
                oldpos += 1
        else:
            while oldpos < len(oldbody):
                self._body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None
                pos += 1
                oldpos += 1
            oldpos = 0
            while oldpos <= self._tail:
                self._body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None
                pos += 1
                oldpos += 1
        self._head = 0
        self._tail = self._size

    def shrink(self):
        oldbody = self._body
        self._body = [None]*(len(self._body)//2)
        oldpos = self._head
        pos = 0
        if self._head < self._tail:
            while oldpos <= self._tail:
                self._body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None
                pos += 1
                oldpos += 1
        else:
            while oldpos < len(oldbody):
                self._body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None
                pos += 1
                oldpos += 1
            oldpos = 0
            while oldpos <= self._tail:
                self._body[pos] = oldbody[oldpos]
                oldbody[oldpos] = None
                pos += 1
                oldpos += 1
        self._head = 0
        self._tail = self._size

    def __str__(self):
        return ("%s"%(self._body))

if __name__ == "__main__":
    #for init => self._body = [None]*3
    q1 = myQueue()
    q1.enqueue("a")
    q1.enqueue("b")
    print(q1)
    q1.dequeue()
    print(q1)
    q1.dequeue()
    print(q1)
    q1.enqueue("a")
    q1.enqueue("b")
    print(q1)
    q1.dequeue()
    print(q1)
    q1.dequeue()
    print(q1)
    
