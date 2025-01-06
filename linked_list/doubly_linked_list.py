class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.prev = None
        self.length = 0

    def display(self):
        current = self.head
        while current:
            print (current.data, end=",")
            current = current.next
        print ("----") 

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.prev = None
            return
        else:
            self.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
            
    
    def prepend (self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1

    def insert (self, index, data):
        if index < 0 :  # Handle invalid indices
            raise IndexError("Index out of range")
        
        if index > self.length: # Append if index is at the end
            self.append(data)
            return
        
        new_node = Node(data)
        
        if index == 0 :
            new_node.next = self.head
            self.head = new_node
            if self.length == 0 :
                self.tail = new_node
        else:
            leader = self.travers_to_index(index - 1)
            holding_pointer = leader.next

            leader.next = new_node
            new_node.next = holding_pointer
        self.length +=1
    
    def travers_to_index (self, index):
        current_node = self.head
        counter = 0
        while counter < index:
            current_node = current_node.next
            counter +=1
        return current_node
    
    def remove (self, index):
        if index < 0 or index > self.length:  # Handle invalid indices
            raise IndexError("Index out of range")
        
        if index == 0: # Special case for removing the first node
            unwanted_node = self.head
            self.head = unwanted_node.next
            if self.length == 1:
                self.tail = None

        else:
            leader = self.travers_to_index(index - 1)
            unwanted_node = leader.next
            leader.next = unwanted_node.next
            if unwanted_node.next:
                follower = unwanted_node.next
                follower.prev = leader
            else:  # If the removed node was the tail
                self.tail = leader


        self.length -=1
        