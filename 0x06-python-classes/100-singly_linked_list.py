#!/usr/bin/python3
"""singly list module node """


class Node:
    """singly list class node"""

    def __init__(self, data, next_node=None) -> None:
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__node = value


class SinglyLinkedList:
    """Singly linked list class"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        n = Node(value)
        n.next_node = None

        if self.__head is None:
            self.__head = n

        elif self.__head.data > value:
            n.next_node = self.__head
            self.__head = n

        else:
            tmp = self.__head
            while tmp.next_node is not None:
                if tmp.next_node.data < value:
                    tmp = tmp.next_node
                else:
                    break

            n.next_node = tmp.next_node
            tmp.next_node = n

    def __str__(self):
        tmp = self.__head
        while tmp is not None:
            print(
                "{}".format(tmp.data),
                end="\n" if tmp.next_node is not None else "",
            )
            tmp = tmp.next_node
        return ""
