class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0 
    

    def peek(self):
        return self.first
    
    def dequeue(self):
        # If the queue is empty 
        if self.length == 0 :
            print ("The queue is empty")
            return 
        
        # If there is only on item in the queue
        if self.length == 1:
            self.first = None
            self.last = None
            return 

        else:
            self.first = self.first.next
            self.length -=1
    
    def enqueue(self,value):
        new_node = Node(value)

        # Check if queue is empty
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length +=1

   
    def print_queue(self):
        elements = []
        current = self.first
        while current :
            elements.append(current.value)
            current = current.next
        print("Qeueu (first to last):", " -> ".join(map(str, elements))) 