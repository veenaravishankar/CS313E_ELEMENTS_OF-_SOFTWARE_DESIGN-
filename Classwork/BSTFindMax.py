class Node:
   def __init__(self, key):
       self.left = None
       self.right = None
       self.val = key

def insert(root, key):
   if root is None: return Node(key)
   if root.val < key:
       root.right = insert(root.right, key)
   else:
       root.left = insert(root.left, key)
   return root

def find_min(root):
   """Finds the minimum key in a subtree."""
   current = root
   while current.left is not None:
       current = current.left
   return current

def find_max(root):
    """
    Finds the maximum key in a subtree.

    Args:
        root: The root node of the BST.

    Returns:
        The greatest integer in the subtree.
    """
    # YOUR CODE HERE
    # Implement the logic to find the maximum.