class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:

    def __init__ (self):
        self.top = None
        self.bottom = None
        self.length = 0
    

    def peek(self):
        if self.top:
            return self.top.data
        
        return None
    
    def pop(self):
        if not self.top:
            return None
        
        #When ther is only one item in thw stack 
        if self.top == self.bottom:
            self.bottom = None

        poped_node = self.top
        self.top = self.top.next
        self.length -= 1
        return poped_node.data
    

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top

        self.top = new_node
        self.length += 1
        return self
    
    def print_stack(self):
        elements = []
        current = self.top
        while current :
            elements.append(current.data)
            current = current.next
        print("Stack (top to bottom):", " -> ".join(map(str, elements))) 

