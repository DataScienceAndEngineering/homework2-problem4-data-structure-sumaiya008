# implamanting Queue using Stack

#Creating empty queue.
class MyQueue():
    
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        #insert the item to the front in the list
        self.items.insert(0,item)

    def dequeue(self):
        # removes and returns the last item in the list
        if self.items.empty():
            return False
        else:
            return self.items.pop()

    # Checking empty or not
    def isEmpty(self):
        return self.items == []

    # return size of the items
    def size(self):
        return len(self.items)
    