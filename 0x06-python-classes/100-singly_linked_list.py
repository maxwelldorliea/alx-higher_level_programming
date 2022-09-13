#!/usr/bin/python3

"""Create a new type of type Node."""

class Node:
    """Create a new type of type Node."""

    def __init__(self, data=0, next_node=None):
        """Initialize Node."""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node
    
    @property
    def data(self):
        """Get the value data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the value of data."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node."""
        if not value is None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

"""Create an object of type SinglyLinkedList."""
class SinglyLinkedList:
    """Create an object of type SinglyLinkedList."""

    def __init__(self):
        """Initialize SinglyLinkedList."""
        self.__head = None
    
    def __str__(self):
        """Print str representation of singlelinkedlist."""
        tmp = self.__head
        out = ''
        while tmp:
            out += str(tmp.data) + '\n'
            print(tmp.data)
            tmp = tmp.next_node
        return out
    
    def sorted_insert(self, value):
        """Insert in a sorted order."""
        h = self.__head
        node = Node(value, h);
        h = self.__head
        h = node
        s = node.next_node

        while h:
            while s:
                if h.data > s.data:
                    h.data, s.data = h.data, s.data
                s = s.next_node
            h = h.next_node
