class Element:
    def __init__(self,k,v,i):
        self._key = k
        self._value = v
        self._index = i

    def __eq__(self,other):
        return self._key == other._key

    def __lt__(self,other):
        return self._key < other._key

    def _wipe(self):
        self._key = None
        self._value = None
        self._index = None

    def __str__(self):
        return str((self._key,self._value,self._index))

class APQHeap:
    def __init__(self):
        self._body = []
        self._next = 0

    def add(self,key,item):
        new = Element(key,item,self._next)
        self._body.append(new)
        self._bubbleup(self._next)
        self._next += 1
        return new

    def _bubbleup(self,i):
        parent = (i-1)//2
        if parent >= 0 and self._body[i] < self._body[parent]:
            self._body[parent], self._body[i] = self._body[i], self._body[parent]
            self._body[parent]._index = parent
            self._body[i]._index = i
            self._bubbleup(parent)

    def min(self):
        if len(self._body) == 0:
            return None
        return self._body[0]

    def remove_min(self):
        if len(self._body) == 0:
            return None
        else:
            if len(self._body) > 1:
                self._body[0], self._body[self._next-1] = self._body[self._next-1], self._body[0]
                self._body[0]._index = 0
                mini = self._body.pop()
                self._next -= 1
                self._bubbledown(0)
            elif len(self._body) == 1:
                mini = self._body.pop()
                self._next -= 1
        return mini._key, mini._value

    def _bubbledown(self,i):
        print("i:",i)
        left = (2*i)+1
        right = (2*i)+2
        print("left:",left)
        print("right:",right)
        if left < self._next-1 and right <= self._next-1:
            if self._body[left] < self._body[right] and self._body[left] < self._body[i]:
                self._body[i], self._body[left] = self._body[left], self._body[i]
                self._body[i]._index = i
                self._body[left]._index = left
                self._bubbledown(left)
            elif self._body[right] < self._body[left] and self._body[right] < self._body[i]:
                self._body[i], self._body[right] = self._body[right], self._body[i]
                self._body[i]._index = i
                self._body[right]._index = right
                self._bubbledown(right)
        elif left <= self._next-1 and self._body[left] < self._body[i]:
            self._body[i], self._body[left] = self._body[left], self._body[i]
            self._body[i]._index = i
            self._body[left] = left
            self._bubbledown(left)

        
    def is_empty(self):
        if len(self._body) == 0:
            return True
        return False
        
    def update_key(self,element,newkey):
        element._key = newkey
        self._rebalance(element._index)

    def _rebalance(self,i):
        self._bubbleup(i)
        self._bubbledown(i)
        
    def get_key(self,element):
        return element._key
        
    def remove(self,element):
        if self._body[element._index] == self._body[self._next-1]:
            elmt = self._body[element._index].pop()
        else:
            self._body[element._index], self._body[self._next-1] = self._body[self._next-1], self._body[element._index]
            self._body[element._index]._index = element._index
            elmt = self._body.pop()
            self._rebalance(element._index)
        return elmt._key, elmt._value

    def length(self):
        return len(self._body)

    def __str__(self):
        result = "["
        for i in range(len(self._body)):
            if i == 0:
                result += str(self._body[i])
            else:
                result += "," + str(self._body[i])
        result += "]"
        return result
            
            
if __name__ == "__main__":

    heap = APQHeap()
    a = heap.add(1,"a")
    b = heap.add(2,"b")
    c = heap.add(3,"c")
    d = heap.add(4,"d")
    e = heap.add(5,"e")
    f = heap.add(6,"f")
    while heap.length()!=0:
        print(heap)
        heap.remove_min()
        print(heap)
        print()

        


        
