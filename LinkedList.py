########################################
# PROJECT 1 - Linked List
# Author:  Clare Kinery
########################################


class Node:
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

    def __eq__(self, other):
        """
        DO NOT EDIT
        Determine if two nodes are equal (same value)
        :param other: node to compare to
        :return: True if nodes are equal, False otherwise
        """
        if other is None:
            return False
        if self.value == other.value:
            return True
        return False

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self.value)

    __str__ = __repr__


class LinkedList:
    def __init__(self):
        """
        DO NOT EDIT
        Create/initialize an empty linked list
        """
        self.head = None   # Node
        self.tail = None   # Node
        self.size = 0      # Integer

    def __eq__(self, other):
        """
        DO NOT EDIT
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        """
        if self.size != other.size:
            return False
        if self.head != other.head or self.tail != other.tail:
            return False

        # Traverse through linked list and make sure all nodes are equal
        temp_self = self.head
        temp_other = other.head
        while temp_self is not None:
            if temp_self == temp_other:
                temp_self = temp_self.next_node
                temp_other = temp_other.next_node
            else:
                return False
        # Make sure other is not longer than self
        if temp_self is None and temp_other is None:
            return True
        return False

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a linked list
        :return: string of list of values
        """
        temp_node = self.head
        values = []
        if temp_node is None:
            return None
        while temp_node is not None:
            values.append(temp_node.value)
            temp_node = temp_node.next_node
        return str(values)

    __str__ = __repr__

    ###### students modify the below functions #####

    # ------------------------Accessor Functions---------------------------

    def length(self):
        """
        evaluates the length of a linked list
        :return: int representing length of linked list
        """
        return self.size

    def is_empty(self):
        """
        checks if linked list is empty
        :return: boolean, True or False
        """
        return self.size == 0

    def front_value(self):
        """
        finds value of head node if exists
        :return: int value of node
        """
        if self.size == 0:
            return None
        return self.head.value

    def back_value(self):
        """
        finds value of tail node if exists
        :return: int value of node
        """
        if self.size == 0:
            return None
        return self.tail.value

    def count(self, val):
        """
        counts all instances of given value
        in linked list
        :param val: int value
        :return: int
        """
        cnt = 0
        node = self.head
        while node != None:
            if node.value == val:
                cnt += 1
            node = node.next_node

        return cnt


    def find(self, val):
        """
        expresses if given value is
        present in linked list
        :param val: int value
        :return: boolean, True or False
        """
        node = self.head
        while node != None:
            if node.value == val:
                return True
            node = node.next_node

        return False

    # ------------------------Mutator Functions---------------------------

    def push_front(self, val):
        """
        creates new node with given value
        and defines it as the head of
        linked list
        :param val: int value
        :return: no return
        """

        #initalizes linked list
        if self.size == 0:
            int_node = Node(val)
            self.head = int_node
            self.tail = self.head

        #inserts
        else:
            self.head = Node(val, self.head)

        self.size += 1


    def push_back(self, val):
        """
        creates new node with given value
        and defines it as the tail of
        linked list
        :param val: int value
        :return: no return
        """

        #initalizes linked list
        if self.size == 0:
            int_node = Node(val)
            self.head = int_node
            self.tail = self.head

        # inserts
        else:
            new_tail = Node(val)
            self.tail.next_node = new_tail
            self.tail = new_tail

        self.size += 1

    def pop_front(self):
        """
        Removes head node if linked list's
        size is greater than zero
        :return: int value of node removed
        """

        if self.size > 0:
            val = self.head.value
            self.head = self.head.next_node
            self.size -= 1
            return val
        return None

    def pop_back(self):
        """
        Removes tail node if linked list's
        size is greater than zero
        :return: int value of node removed
        """

        if self.size > 0:
            val = self.tail.value
            node = self.head

            while node.next_node != self.tail:
                node = node.next_node

            self.tail = node
            node.next_node = None
            self.size -= 1

            return val
        return None


def partition(linked_list, x):
    """
    sorts values less than x before
    values greater than x. Does not
    change order of values in linked
    list
    :param linked_list: linked list of
    nodes
    :param x: int value
    :return: updated linked list
    """
    val = linked_list.front_value()
    front_val = val
    front_val_cnt = linked_list.count(front_val)
    front_val_it = 0
    while val >= x:
        if val == front_val:
            front_val_it += 1
        if front_val_it == front_val_cnt + 1:
            break
        linked_list.pop_front()
        linked_list.push_back(val)
        val = linked_list.front_value()

    return linked_list