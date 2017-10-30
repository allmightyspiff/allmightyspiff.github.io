"""
@author Christopher Gallo
Linked List Example
"""
from pprint import pprint as pp

class Node():

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return str(self.data)

class linked_list():

    def __init__(self):
        self.head = None
        self.current = None
    def __iter__(self):
        self.current = None
        return self

    def next(self):
        if self.head and not self.current:
            self.current = self.head
            return self.current
        elif self.current.next:
            self.current = self.current.next
            return self.current
        else:
            raise StopIteration


    def add_node(self, node):
        if self.head is None:
            self.head = node
            self.current = node
        else:
            self.current.next = node
            self.current = node 
    def __str__(self):
        if self.head is None:
            return ''
        current = self.head
        out = "%s" % (current)
        while (current.next != None):
            current = current.next
            out += ", %s" % str(current)
        return out
if __name__ == "__main__":
    my_list = linked_list()
    my_list.add_node(Node('a'))
    my_list.add_node(Node('b'))
    # my_list.add_node(Node(100))
    for node in my_list:
        print(node)