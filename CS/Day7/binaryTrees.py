from pprint import pprint as pp

class Node():
    def __init__(self, key):
        self.right = None
        self.left = None
        self.key = key
        self.parent = None

    def __str__(self): 
        return str(self.key)

class BTree():
    def __init__(self):
        self.root = None

    # prints breadth first
    def __str__(self):
        return_string = ''
        this_level = [self.root]
        while this_level:
            next_level = list()
            for node in this_level:
                height = self.height(node)
                return_string = ("%s %s" % (return_string,node))
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            return_string = ("%s\n" % return_string)
            this_level = next_level
        return(return_string)

    # prints depth first
    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)
        else:
            print("EMPTY")

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(node)
            self._printTree(node.right)

    def height(self, node=None):
        if node is None:
            return 0
        else: 
            return max(self.height(node.left), self.height(node.right)) + 1


    def add_node(self, key, node=None):
        if node is None:
            node = self.root
        if self.root is None:
            self.root = Node(key)
        else:
            # LEFT insert
            if key <= node.key:
                if node.left is None:
                    node.left = Node(key)
                    node.left.parent = node
                    return
                else:
                    # Recurse left
                    return self.add_node(key, node=node.left)
            # RIGHT insert
            else:
                if node.right is None:
                    node.right = Node(key)
                    node.right.parent = node
                    return
                else:
                    # Recurse right
                    return self.add_node(key, node.right)


if __name__ == "__main__":
    print("Starting up")
    tree = BTree()
    tree.add_node(10)
    tree.add_node(25)
    tree.add_node(7)
    tree.add_node(6)
    tree.add_node(11)
    # print(tree)
    # tree.printTree()
    print("Height is %s" % tree.height(tree.root))