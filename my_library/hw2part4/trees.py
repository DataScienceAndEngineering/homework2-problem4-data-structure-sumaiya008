# Binary search Tree Python implementation.

#Defing class node.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        # to optimize memory and make search, insert, delete easier
        