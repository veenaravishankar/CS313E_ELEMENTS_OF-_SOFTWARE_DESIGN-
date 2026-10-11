class Node:
    """A node in a binary search tree."""

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    """Inserts a new key into the BST."""
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def count_nodes(root):
    """
    Counts the total number of nodes in the tree.

    Args:
        root: The root node of the BST.

    Returns:
        The integer count of all nodes in the tree.
    """
    # YOUR CODE HERE
    # Implement the logic to count the nodes.
