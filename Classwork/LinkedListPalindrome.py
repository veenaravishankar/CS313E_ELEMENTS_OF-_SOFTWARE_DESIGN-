class Node:
   """A simple node for a singly linked list."""
   def __init__(self, data=0, next_node=None):
       self.data = data
       self.next = next_node


class LinkedList:
   """A simple linked list class for demonstration purposes."""
   def __init__(self):
       self.head = None


   def append(self, data):
       """Appends a new node with the given data to the end of the list."""
       if not self.head:
           self.head = Node(data)
           return
       current = self.head
       while current.next:
           current = current.next
       current.next = Node(data)


   def print_list(self):
       """Prints the elements of the list."""
       nodes = []
       current = self.head
       while current:
           nodes.append(str(current.data))
           current = current.next
       print(" -> ".join(nodes))


def reverse_and_clone(node):
   """
   This function intends to reverse and clone a linked list.


   Args:
       node: The head node of the linked list to reverse and clone.


   Returns:
       The head node of the new, reversed linked list.

   COMPLETE THE FUNCTION
   """




def is_equal(one, two):
   """
   This function intends to compare two linked lists to see if they are identical.


   Args:
       one: The head node of the first linked list.
       two: The head node of the second linked list.


   Returns:
       True if the lists are equal, False otherwise.


   COMPLETE THIS FUNCTION
   """


def is_palindrome(head):
   reversed_head = reverse_and_clone(head)
   return is_equal(head, reversed_head)
