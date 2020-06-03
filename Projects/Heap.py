'''
PROJECT 6 - Heaps
Name: Clare Kinery
'''

class Node:
    """
    Class definition shouldn't be modified in anyway
    """
    __slots__ = ('_key', '_val')

    def __init__(self, key, val):
        self._key = key
        self._val = val

    def __lt__(self, other):
        return self._key < other._key or (self._key == other._key and self._val < other._val)

    def __gt__(self, other):
        return self._key > other._key or (self._key == other._key and self._val > other._val)

    def __eq__(self, other):
        return self._key == other._key and self._val == other._val

    def __str__(self):
        return '(k: {0} v: {1})'.format(self._key, self._val)

    __repr__ = __str__

    @property
    def val(self):
        """
        :return: underlying value of node
        """
        return self._val


class Heap:
    """
    Class definition is partially completed.
    Method signatures and provided methods may not be edited in any way.
    """
    __slots__ = ('_size', '_capacity', '_data')

    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity + 1  # additional element space for push
        self._data = [None for _ in range(self._capacity)]

    def __str__(self):
        return ', '.join(str(el) for el in self._data if el is not None)

    __repr__ = __str__

    def __len__(self):  # allows for use of len(my_heap_object)
        return self._size

#    DO NOT MODIFY ANYTHING ABOVE THIS LINE
#    Start of Student Modifications
    def swap(self, parent, node):
        """
        Swaps two elements in the array
        :param parent: Index of node
        :param node: Index of node
        :return: None
        """
        self._data[node], self._data[parent] = self._data[parent], self._data[node]
        return None

    def _percolate_up(self):
        """
        Percolates element in last spot up to valid position.
        :return: None
        """
        parent = (self._size-1)//2
        node = self._size-1

        while node > 0 and self._data[node] < self._data[parent]:
            self.swap(parent, node)
            node = parent
            parent = (parent - 1) // 2

        return None

    def _percolate_down(self):
        """
        Percolates element in first spot down to valid position.
        :return: None
        """
        node = 0

        while node < self._size - 1: #not right
            small_child_index = self._min_child(node)
            if small_child_index == -1: #if no children
                return None
            if self._data[small_child_index] < self._data[node]:
                self.swap(node, small_child_index)
                #change node, right, left
                node = small_child_index
            else:
                 break #if no more swaps

        return None

    def _min_child(self, i):
        """
        Takes an index of a Node and returns the
        index of its smallest child. If Node has no children
        return -1.
        :param self: Heap
        :param i: Int, index of Node
        :return: Int, index of smallest child Node
        """
        small_child = -1 #if no children
        right = 2*i +2
        left = 2*i +1

        if left <= self._size - 1:
            small_child = left
            if right <= self._size - 1:
                if self._data[right] < self._data[left]:
                    small_child = right

        return small_child


    def push(self, key, val):
        """
        Intakes a key and value. Adds a Node to the heap.
        If heap capacity is full, deletes the smallest Node
        after pushing in the new Node.
        :param self: Heap
        :param key: Key of Node
        :param val: Value of Node
        :return: None
        """

        self._data[self._size] = Node(key, val)
        self._size += 1
        self._percolate_up()

        if self._size > self._capacity -1:
            self.pop()

        return None

    def pop(self):
        """
        Removes the smallest Node from the heap.
        :param self: Heap
        :return: None
        """
        if self._size == 0: #empty heap
            return None

        elif self._size == 1: #one item in heap
            item = self._data.pop(0)
            self._size -= 1
            return item._val

        self.swap(0, self._size -1)
        item = self._data.pop(self._size -1)
        self._data.append(None)
        self._size -= 1

        self._percolate_down()

        return item._val

    @property  # do not remove
    def empty(self):
        """
        Checks if heap is empty.
        :return: Boolean, True/False
        """
        return self._size == 0

    @property  # do not remove
    def top(self):
        """
        Finds the top of heap and returns
        the value of Node. If heap is empty,
        returns None.
        :return: Value of Node
        """
        if self._size == 0:
            return None
        else:
            return self._data[0]._val

    @property  # do not remove
    def levels(self):
        """
        Creates a list containing levels of heap. Each
        level is represented by a list containing all Nodes
        within that level.
        :return: List of lists
        """
        #make this recursive for bonus points

        ret_lst = []
        begin = 0
        count = 0

        while begin < self._size: #eventually just change to count
            end = begin * 2 + 1
            count += len(self._data[begin:end])

            if count > self._size:
                ret_lst.append(self._data[begin:self._size])
            else:
                ret_lst.append(self._data[begin:end])

            begin = end

        return ret_lst

def most_x_common(vals, X):
    """
    Creates and returns a set containing the
    specified amount, X, of the most common values
    in list, vals.
    :param vals: List
    :param X: Int
    :return: Set
    """
    dict = {}
    ordered_lst = []
    for i in vals:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    heap = Heap(len(dict))

    for key, value in dict.items(): #add items to heap
        heap.push(value, key)

    while heap.empty is False:      #create a list ordered from least occuring to most
        ordered_lst.append(heap.pop())

    ret_set = set()
    for i in range(X):
        val = ordered_lst.pop()
        ret_set.add(val)

    return ret_set