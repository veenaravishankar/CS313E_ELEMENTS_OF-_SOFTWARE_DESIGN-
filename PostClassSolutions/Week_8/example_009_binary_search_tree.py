class Node():
    '''This class represents a single Node.'''

    def __init__(self, key):
        self.key = key
        self.lChild = None
        self.rChild = None
    """It prints the right subtree first, then the current node, then the left subtree.
    The level parameter controls indentation: each level adds 4 spaces before the node key.
    This creates a "sideways" tree where the root is toward the left, the right child is higher, and the left child is lower."""

    def print_node(self, level=0):
        if self.rChild != None:
            self.rChild.print_node(level + 1)

        print(' ' * 4 * level + '->', self.key)

        if self.lChild != None:
            self.lChild.print_node(level + 1)
    
      # In-order traversal - left, center, right
    def inOrder(self, aNode):
        if (aNode != None):
            aNode.inOrder(aNode.lChild)
            print(aNode.key, end=" ")
            aNode.inOrder(aNode.rChild)

    # Pre-order traversal - center, left, right
    def preOrder(self, aNode):
        if (aNode != None):
            print(aNode.key, end=" ")
            aNode.preOrder(aNode.lChild)
            aNode.preOrder(aNode.rChild)

    # Post-order traversal - left, right, center
    def postOrder(self, aNode):
        if (aNode != None):
            aNode.postOrder(aNode.lChild)
            aNode.postOrder(aNode.rChild)
            print(aNode.key, end=" ")


class BST():
    '''This class represents a Binary Search Tree.'''

    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    # Search for a node with the key
    def search(self, key):
        current = self.root
        while ((current != None) and (current.key != key)):
            if (key < current.key):
                current = current.lChild
            else:
                current = current.rChild
        return current

    # Insert a node in the tree
    def insert(self, val):
        newNode = Node(val)

        if (self.root == None):
            self.root = newNode
        else:
            current = self.root
            parent = self.root
# seearch 
            while (current != None):
                parent = current
                if (val < current.key):
                    current = current.lChild
                else:
                    current = current.rChild
# insert 
            if (val < parent.key):
                parent.lChild = newNode
            else:
                parent.rChild = newNode


    # Find the node with the smallest value
    def minimum(self):
        current = self.root
        parent = current
        while (current != None):
            parent = current
            current = current.lChild
        return parent

    # Find the node with the largest value
    def maximum(self):
        current = self.root
        parent = current
        while (current != None):
            parent = current
            current = current.rChild
        return parent

    # Delete a node with a given key
    def delete(self, key):
        current = self.root
        parent = None
        isLeft = False

        # Find the node to delete.
        while current is not None and current.key != key:
            parent = current

            if key < current.key:
                current = current.lChild
                isLeft = True
            else:
                current = current.rChild
                isLeft = False

        # Empty tree or key not found.
        if current is None:
            return False

        deleteNode = current

        # Case 1: No children — disconnect the leaf.
        if deleteNode.lChild is None and deleteNode.rChild is None:
            if deleteNode is self.root:
                self.root = None
            elif isLeft:
                parent.lChild = None
            else:
                parent.rChild = None

        # Case 2 / 3.2: Only a left child.
        # The left child and its subtree take the deleted node's place.
        elif deleteNode.rChild is None:
            if deleteNode is self.root:
                self.root = deleteNode.lChild
            elif isLeft:
                parent.lChild = deleteNode.lChild
            else:
                parent.rChild = deleteNode.lChild

        # Case 2 / 3.1: Only a right child.
        # The right child and its subtree take the deleted node's place.
        elif deleteNode.lChild is None:
            if deleteNode is self.root:
                self.root = deleteNode.rChild
            elif isLeft:
                parent.lChild = deleteNode.rChild
            else:
                parent.rChild = deleteNode.rChild

        # Cases 3.3 and 3.4: Two children.
        else:
            # Find the successor: smallest node in the right subtree.
            successor = deleteNode.rChild
            successorParent = deleteNode

            while successor.lChild is not None:
                successorParent = successor
                successor = successor.lChild

            # Case 3.4: Successor is farther down the right subtree.
            if successor is not deleteNode.rChild:
                # Replace the successor at its old position
                # with its right child, which may be None.
                successorParent.lChild = successor.rChild

                # Give the successor the deleted node's right subtree.
                successor.rChild = deleteNode.rChild

            # Case 3.3: Successor is the immediate right child.
            # Its right subtree is already correct; skip the block above.

            # Both cases: Put the successor in the deleted node's position.
            if deleteNode is self.root:
                self.root = successor
            elif isLeft:
                parent.lChild = successor
            else:
                parent.rChild = successor

            # Give the successor the deleted node's left subtree.
            successor.lChild = deleteNode.lChild

        return True


###############################
#                             #
#   Example run of a BST run  #
#                             #
###############################

def main():
    bst = BST()

    bst.insert(10)
    bst.insert(40)
    bst.insert(5)
    bst.insert(15)
    bst.insert(22)
    bst.insert(4)

    bst.print(2)
    print("##############")
    bst.delete(10)
    bst.print(2)
    print("##############")

    print("Print In-Order")
    bst.root.inOrder(bst.root)

    print()
    print("Print Pre-Order")
    bst.root.preOrder(bst.root)

    print()
    print("Print Post-Order")
    bst.root.postOrder(bst.root)

if __name__ == '__main__':
    main()
