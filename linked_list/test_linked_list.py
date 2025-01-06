from linked_list import LinkedList
ll = LinkedList()

#from doubly_linked_list import DoublyLinkedList
#ll = DoublyLinkedList()

print("Linked List:")
ll.display()

ll.append(10)
ll.append(11)
ll.append(12)

ll.display()

# ll.prepend(1)
# ll.insert(2,5)
# ll.insert(10,99)


# ll.display()
#ll.remove(2)

ll.reverse()
ll.display()