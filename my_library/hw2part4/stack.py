#program to implement a stack using queue

from collections import deque

class MyStack(object):
    def __init__(self):
        """
        Create an empty stack here.
        """
        self.queue = deque([])

# push element in stack
    def push(self, x):
        """
        @param x
        return nothing
        """
        self.queue.append(x)
        for i in range(len(self.queue)):
            self.queue.append(self.queue.popleft())

    def pop(self):
        """
        pop one item
        return nothing
        """
        if self.queue.empty():
            return False
        else:
            return self.queue.popleft()

    def top(self):
        """
        return top element
        """
        if self.queue.empty():
            return False
        else:
            return self.queue[0]

    def empty(self):
        """
        check stack empty or not.
        """
        return len(self.queue) == 0        