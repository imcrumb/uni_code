
""" Some example functions using a Stack.
"""

import stackA
from stackA import Stack

def palindrome_check(string):
    """ Determine whether string is a palindrome, using a stack.    """
    mylist = list(string)
    size = len(mylist)
    mid = size // 2
    even = True
    if size % 2 == 1:
        even = False
    print('Midpoint is', mid, '; string is of EVEN length:', even)
    stack = Stack()   #create and return a stack object
    pos = 0
    while pos < mid:        #push first half of the string onto the stack
        stack.push(mylist[pos])
        pos = pos + 1
    if not even:
        pos = pos + 1
    while pos < len(mylist):  #now pop and compare the two half lists
        print('mylist[', pos, ']=', mylist[pos], '; stack.top() =', stack.top())
        if mylist[pos] != stack.pop():
            return False
        pos = pos+1
    print('This is a palindrome')
    return True


def palindrome_check_list(inlist):
    """ Determine whether inlist is a palindrome, using a stack.    """
    size = len(inlist)
    mid = size // 2
    even = True
    if size % 2 == 1:
        even = False
    print('Midpoint is', mid, '; inlist is of EVEN length:', even)
    stack = Stack()
    pos = 0
    while pos < mid:
        stack.push(inlist[pos])
        pos = pos + 1
    if not even:
        pos = pos + 1
    while pos < len(inlist):
        print('mylist[', pos, ']=', inlist[pos], '; stack.top() =', stack.top())
        #if inlist[pos] != stack.pop():
        if not inlist[pos].is_equal(stack.pop()):
            return False
        pos = pos+1
    return True

def objlistcheck():
    """ Test the function which checks palindrom lists.

        Create a list of 'Card' objects, and pass that in to palindrome ...
    """
    
    cardlist = []

    print('Checking an empty list of playing cards, should be True')
    print(palindrome_check_list(cardlist))

    cardlist.append(Card(3,3))
    cardlist.append(Card(1,4))
    cardlist.append(Card(12,2))
    cardlist.append(Card(7,1))
    cardlist.append(Card(12,2))
    cardlist.append(Card(1,4))
    cardlist.append(Card(3,3))

    print('Checking a palindromic list of playing cards, should be True')
    print(palindrome_check_list(cardlist))

    cardlist[2] = Card(11,2)
    print('Checking a non-palindromic list of playing cards, should be False')
    print(palindrome_check_list(cardlist))

def postfix(string):
    """ Evaluate the postfix string, using a stack.

        Elements must be separated by spaces.
    """
    tokenlist = string.split()
    stack = Stack()
    for token in tokenlist:
        if token in ["+", "-", "*", "/"]:
            second = stack.pop()
            first = stack.pop()
            if token == "+":
               stack.push(first + second)
            elif token == "-":
               stack.push(first - second)
            elif token == "*":
               stack.push(first * second)
            else:
               stack.push(first / second)
        else:
            stack.push(int(token))
    return stack.pop()
       
def postfix_verbose(string):
    """ Evaluate the postfix string, using a stack.

        Elements must be separated by spaces.
        Display progress on screen.
    """
    tokenlist = string.split()
    stack = Stack()
    for token in tokenlist:
        print('next token taken from string is', token)
        if token in ["+", "-", "*", "/"]:
            second = stack.pop()
            first = stack.pop()
            print('   Op, so pop twice, and evaluate <2nd-top> <op> <top>',
                   first, token, second)
            if token == "+":
                print('    = ', first + second)
                stack.push(first + second)
            elif token == "-":
                print('    = ', first - second)
                stack.push(first - second)
            elif token == "*":
                print('    = ', first * second)
                stack.push(first * second)
            else:
                print('    = ', first / second)
                stack.push(first / second)
            print('   and push back onto stack')
        else:
            print('   Value (=', token, ') so push onto stack')
            stack.push(int(token))
        print('Stack is now:', stack)
    print('No tokens left in string, so pop from stack (of length 1):', stack)
    return stack.pop()
            
class Card:
    """A standard playing card. """

    def __init__(self, rank, suit):
        """ Initialise the card.

            rank should be an integer in {1,2,...,13}
            suit should be an integer in {1,2,3,4}

        """
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return '' + self.name_rank() + self.name_suit()

    def name_rank(self):
        """ Return a string representation of the rank. """
        if self.rank == 1:
            return 'A'
        elif self.rank == 11:
            return 'J'
        elif self.rank == 12:
            return 'Q'
        elif self.rank == 13:
            return 'K'
        else:
            return '' + str(self.rank)

    def name_suit(self):
        """ Return a string representation of the suit. """
        if self.suit == 1:
            return 'S'
        elif self.suit == 2:
            return 'H'
        elif self.suit == 3:
            return 'D'
        else:
            return 'C'

    def is_equal(self, card):
        """ Determine whether this instance is the same card as another. """
        if self.rank == card.rank and self.suit == card.suit:
            return True
        return False

        
    def test():
        """ Test the Card class.

             Run this each time the implementation of Card changes, to make
             sure the changes are correct and that no unintended effects
             were generated.

        """
        
        c1 = Card(3,3)
        c2 = Card(13,1)
        c3 = Card(8,2)
        c4 = Card(8,2)

        print('c1 (should be 3D) = ', c1)
        print('c2 (should be KS) = ', c2)
        print('c3 (should be 8H) = ', c3)

        errors = 0;

        if c1.rank != 3:
            print('ERROR: c1.rank gave ', c1.rank,
                ' but should be 3')
            errors = errors + 1
        if c2.rank != 13:
            print('ERROR: c2.rank gave ', c2.rank,
                ' but should be 13')
            errors = errors + 1
        if c3.suit != 2:
            print('ERROR: c3.suit gave ', c3.suit,
                ' but should be 2')
            errors = errors + 1
        if not c3.is_equal(c4):
            print('ERROR: c3.is_equal(c4) gave ', c3.is_equal(c4),
                ' but should be True')
            errors = errors + 1
        if c3.is_equal(c2):
            print('ERROR: c3.is_equal(c2) gave ', c3.is_equal(c4),
                ' but should be False')
            errors = errors + 1
        print('Tests complete, with ', errors, ' errors')
