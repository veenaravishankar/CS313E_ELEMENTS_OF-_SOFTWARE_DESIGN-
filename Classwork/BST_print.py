def print_node(self, level=0):
        if self.rChild != None:
            self.rChild.print_node(level + 1)

        print(' ' * 4 * level + '->', self.key)

        if self.lChild != None:
            self.lChild.print_node(level + 1)