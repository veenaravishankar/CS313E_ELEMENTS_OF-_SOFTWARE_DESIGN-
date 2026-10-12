class Node():

    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None


    def in_order_traversal(self,aNode):
        if aNode != None:
            aNode.in_order_traversal(self.lchild)
            print(aNode.key, end=" ")
            aNode.in_order_traversal(self.rchild)

    def pre_order_traversal(self,aNode):
        if aNode != None:
            print(aNode.key, end=" ")
            aNode.pre_order_traversal(self.lchild)
            aNode.pre_order_traversal(self.rchild)


    def post_order_traversal(self,aNode):
        if aNode != None:
            aNode.pre_order_traversal(self.lchild)
            aNode.pre_order_traversal(self.rchild)
            print(aNode.key, end=" ")