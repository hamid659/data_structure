from stack import Stack
from stack_with_array import StackWithArray

my_stack = Stack()

my_stack.push("google")
my_stack.push("udemy")

my_stack.print_stack()
my_stack.pop()


#Testing the stack created with Array
my_stack_2 = StackWithArray()

my_stack_2.push("Google")
my_stack_2.push("Udemy")
my_stack_2.print_stack()

my_stack_2.pop()
my_stack_2.print_stack()