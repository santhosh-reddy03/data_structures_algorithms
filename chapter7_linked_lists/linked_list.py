
# singly linked list
"""
A singly linked list, in its simplest form, is a collection of nodes that collectively form a linear sequence. Each node stores a reference to an
object that is an element of the sequence, as well as a reference to the next node of the list

The linked list object stores the direct reference to the head(1st node) of linked list and also the length of the linked list
to avoid traversing through entire list to count the number of nodes

The last node is called tail in linked list and have reference of 'none' to next node (doesn't refer any)

the process of moving from head to tail node is called traversing and also known as link hoping or pointer hoping
"""

# creating a stack with single linked list


class _Node:
    """Light weight, nonpublic class storing singly linked lists"""
    __slots__ = '_element', '_next'

    def __int__(self, element, next_node):
        self._element = element
        self._next = next_node
