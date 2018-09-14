
""" Class definition for an array-based implementation of the Stack ADT.

    For invalid method calls, does not throw exceptions. Instead, returns
    None if a return value is expected, and otherwise ignores the request.

    Also includes a Class test method: run as Stack._test()
"""


class Stack:
    """ An array-based stack. """
    
    def __init__(self):
        self._list = []      #Note that this is meant to be private
                             #_list should only be accessed from the
                             #methods defined in this class.

    def __str__(self):
        """ Display a stack as a string, by listing elements in sequence.

            |- denotes the bottom of the stack
            -> denotes the top of the stack.
            So '|-x-y-z-> denotes a stack with 3 elements, and z at the top.
        """
        retstr = '|-'                             
        for element in self._list:
            retstr = retstr + str(element) + '-'
        retstr = retstr + '->'                    
        return retstr

    def pop(self):
        """ Remove and return the top element of the stack. """
        if len(self._list) == 0:
            return None
        return self._list.pop()

    def push(self, element):
        """ Place element onto the top of the stack. """
        self._list.append(element)

    def top(self):
        """ Return but don't remove the top element of the stack. """
        if len(self._list) == 0:
            return None        
        return self._list[-1]

    def is_empty(self):
        """ Return True if stack has no elements. """
        return len(self._list) == 0

    def length(self):
        """ Return the number of elements on the stack. """
        return len(self._list)

    def _test():
        """ Test the basic functionality of the stack. Class method. """
        print('Testing the array-based stack')
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        print('stack should be |-1-2-3-->, and is', stack)
        print('stack.length should be 3, and is', stack.length())
        print('stack.is_empty() should be False, and is', stack.is_empty())
        print('stack.top() should be 3, and is', stack.top())
        print('stack.pop() should be 3, and is', stack.pop())
        print('stack should now be |-1-2-->, and is', stack)
        print('stack.length() should be 2, and is', stack.length())
        stack.pop()
        stack.pop()
        print('popped two more items; stack.length() should be 0, and is', stack.length())
        print('stack.top() should be None, and is', stack.top())
        print('stack.pop() should be None, and is', stack.top())
        print('stack should be |-->, and is', stack)

