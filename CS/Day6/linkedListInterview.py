"""
@author Christopher Gallo
Linked List Example
"""
from pprint import pprint as pp
class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.back = None
    def __str__(self):
        return str(self.data)

class linked_list():
    def __init__(self):
        self.head = None
        self.current = None
        self.tail = None

    def __str__(self):
        if self.head is None:
            return None
        start = self.head
        out = "%s" % (start)
        while start.next != None:
            start = start.next
            out += ", %s" % str(start)
        return out

    def __iter__(self):
        self.current = None
        return self

    def __getitem__(self,key):
        if not isinstance(key, int):
            raise TypeError
        count = 0
        if self.head is None:
            raise IndexError
        for node in self:
            if count == key:
                return node
            elif node.next is None:
                raise IndexError
            else:
                count = count + 1


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
            self.tail = node
        else:
            node.back = self.tail
            self.tail.next = node
            self.tail = node 

    def insert(self, node, index):
        if self.head == None:
            self.add_node(node)
        try:
            l_node = self[index - 1]
            node.back = l_node
            l_node.next = node
        except IndexError:
            node.next = self.head
            self.head = node
            l_node = None
        try:
            r_node = self[index + 1]
            node.next = r_node
            r_node.back = node
        except IndexError:
            r_node = None
            self.add_node(node)


if __name__ == "__main__":
    my_list = linked_list()
    my_list.insert(Node('asd'),0)
    my_list.add_node(Node('a'))
    my_list.add_node(Node('b'))
    my_list.add_node(Node(100))
    # print(my_list[2])
    
    print(my_list)
    
    