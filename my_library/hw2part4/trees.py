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

    #inserting elements to the tree.
    def add(self, root, data):
        if self.root is None:
            return self.Node(data)

        if data < root.data:
            root.left = self.add(root.left, data)
        elif data > root.data:
            root.right = self.add(root.right, data)
        else:
            root.data = data
        return root

    #Deleting elements from the tree.
    def remove(self, root, data):
        if data < root.data:
            root.left = self.remove(root.left, data)
        elif data > root.data:
            root.right = self.rempve(root.right, data)
        else:
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

    def height(self, root):
        if self.root is None:
            return 0
        return self.root.height()

    