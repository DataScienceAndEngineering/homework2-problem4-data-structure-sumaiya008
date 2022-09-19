#program to implement a stack using queue

from collections import deque

class Stack(object):
    def __init__(self):
        """
        Create an empty stack here.
        """
        self.q = deque()
        
# push element in stack
     def push(self, x):
        """
        @param x, an int
        return nothing
        """
        self.q.append( x )