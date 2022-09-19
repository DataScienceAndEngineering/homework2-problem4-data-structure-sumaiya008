#program to implement a stack using queue

from collections import deque

class MyStack(object):
    def __init__(self):
        """
        Create an empty stack here.
        """
        self.queue = deque([])