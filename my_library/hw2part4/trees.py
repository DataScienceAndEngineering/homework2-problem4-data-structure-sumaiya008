# Binary search Tree Python implementation.

#Defing class node.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        # to optimize memory and make search, insert, delete easier

#creating class BTS.
class BinarySearchTree(object):

    #creating an empty BST.
    def __init__(self, root):
        self.root = None
