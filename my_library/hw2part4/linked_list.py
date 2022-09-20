# Simple linked list implementation

# creating class node.
from hashlib import new


class Node(object):
    # node carry data and a pointer which points to next data.
    def __init__(self, data, next = None):
        self.data = data;
        self.next = next;

#creating LinkedList class.
class LinkedList(object):
    #Defining head
    def __init__( self ):
        self.head = None

    # Adding node at the biginning.
    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    #remove a node
    def remove(self, data):
        new_node = self.head
        # if data is in head node.
        if (new_node.next is not None):
            if(new_node.data == data):
                self.head = new_node.next
                new_node = None
                return
            else:
                #  else search all the nodes
                while(new_node.next != None):
                    if(new_node.data == data):
                        break
                    prev_node = new_node
                    new_node = new_node.next
                
                # node not found
                if new_node == None:
                    return
                prev_node.next = new_node.next
                return

    def printList(self):
        new_node = self.head
        while(new_node != None):
            print(new_node, end=' ')
            new_node = new_node.next