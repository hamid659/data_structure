    
class StackWithArray:
    def __init__(self):
        self.array = []
    
    def peek(self):
        if len(self.array) == 0:
            raise IndexError("Cannot peek from an empty stack")
        return self.array[len(self.array) -1]

    
    def push(self, value):
        self.array.append(value)

    def pop(self):
        if len(self.array) == 0:
            raise IndexError("Cannot pop from an empty stack")
        return self.array.pop()

    
    def print_stack(self):
        print (self.array)
