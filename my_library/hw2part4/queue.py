# implamanting Queue using Stack

#Creating empty queue.
class MyQueue():
    
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        #insert the item in the list
        self.items.insert(0,item)