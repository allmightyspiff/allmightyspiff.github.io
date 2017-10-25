"""
@author Christopher Gallo
Linked List Example
"""
from pprint import pprint as pp

class Node():

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class linked_list():

    def __init__(self):
        self.head = None
        self.current = None

    def add_node(self, node):
        if self.head is None:
            self.head = node
            self.current = node
        else:
            self.current.next = node
            self.current = node 



if __name__ == "__main__":
    my_list = linked_list()
    my_list.add_node(Node('a'))
    my_list.add_node(Node('b'))
    my_list.add_node(Node(100))
    print(my_list.head.next.data)