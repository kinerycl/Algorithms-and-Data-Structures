"""
PROJECT 2 - Recursion
Name: Clare Kinery
"""

class LinkedNode:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'next_node'

    def __init__(self, value, next_node=None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next_node: pointer to the next node, default is None
        """
        self.value = value  # element at the node
        self.next_node = next_node  # reference to next node


    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self.value)

    __str__ = __repr__

def insert(value, node=None):
    """
    Inserts a node into the end of a linked list
    :param value: value of node
    :param node: head of linked list
    :return: head node
    """
    if node is None: #initailzes linked nodes
        node = LinkedNode(value)
    elif node.next_node is not None:
        insert(value, node.next_node)
    else:
        node.next_node = LinkedNode(value)
    return node


def string(node):
    """
    Puts values of linked list into a single string
    :param node: head of linked list
    :return: string of elements in linked list
    """
    if node is None:
        return ""
    str_rep = str(node)
    if node.next_node is not None:
        str_rep += ", "
        str_rep += string(node.next_node)
    return str_rep

def remove(value, node):
    """
    Removes the first instance of node with found value
    :param value: value wanted to remove
    :param node: head of linked list
    :return: head of linked list
    """
    #head to be removed
    if node.value == value:
        node = node.next_node
    #mid removed
    elif node.next_node is not None and node.next_node.value == value:
        node.next_node = node.next_node.next_node
    #accounts for end of linkedlist
    elif node.next_node is not None:
        remove(value, node.next_node)
    return node


def remove_all(value, node):
    """
    Removes all of the instances of nodes
    containing value
    :param value: value wanted to remove
    :param node: head of linked list
    :return: head of linked list
    """
    #remove current node if contains value
    if node.next_node is not None and node.value == value:
        node = remove_all(value, node.next_node)
    #checks succeeding element
    elif node.next_node is not None and node.next_node.value == value:
        node.next_node = remove_all(value, node.next_node)
    elif node.next_node is not None:
        remove_all(value, node.next_node)
    #end case
    elif node.value == value:
        node = None
    return node

def search(value, node):
    """
    Searches linked list for value
    :param value: value to search for
    :param node: head of linked list
    :return: boolean value
    """
    ret = False
    if node.value == value:
        ret = True
    elif node.next_node is not None:
        ret = search(value, node.next_node)
    return ret


def length(node):
    """
    Finds the amount of nodes in linked list
    :param node: head of linked list
    :return:  int number of nodes in linked list
    """
    len = 0
    if node is not None:
        len += 1
    if node.next_node is not None:
        len += length(node.next_node)
    return len


def sum_all(node):
    """
    Sums all the values in linked list
    :param node: head of linked list
    :return: int, sum of all node values
    """
    sum = 0
    if node is not None:
        sum += node.value
    if node.next_node is not None:
        sum += sum_all(node.next_node)
    return sum


def count(value, node):
    """
    Counts the number of nodes with value as value
    :param value: value to search for
    :param node: head of linked list
    :return: int, number of nodes with value
    """
    cnt = 0
    if node.value == value:
        cnt += 1
    if node.next_node is not None:
        cnt += count(value, node.next_node)
    return cnt


def palindrome(node, length, nodes):
    """
    Checks if linked list is a palindrome: values
    read the same backwards/forwards
    :param node: head of linked list
    :param length: int, number of nodes in linked list
    :param nodes: list containing one node for comparison
    :return: boolean value
    """
    nodes = [node]
    if length not in (0, 1): #for even/odd
        palindrome(node.next_node, length-2, nodes)
    for i in range(length-1):
        nodes[0] = nodes[0].next_node
    if node.value != nodes[0].value:
        return False
    return True

ll = LinkedNode(6)
insert(1, ll)
print(ll)
