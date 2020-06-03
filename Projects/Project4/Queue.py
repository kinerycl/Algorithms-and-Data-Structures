"""
PROJECT 4 - QUEUES
Name: Clare Kinery
"""


class CircularQueue:
    """
    Circular Queue Class
    """
    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        DO NOT MODIFY.
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0


    def __eq__(self, other):
        """
        DO NOT MODIFY.
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity:
            return False
        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False
        return self.head == other.head and self.tail == other.tail and self.size == other.size

    def __str__(self):
        """
        DO NOT MODIFY.
        String representation of the queue
        :return: the queue as a string
        """
        if self.is_empty():
            return "Empty queue"
        result = ""
        str_list = [str(self.data[(self.head + i)%self.capacity]) for i in range(self.size)]
        return "Queue: " + (", ").join(str_list)

    # -----------MODIFY BELOW--------------
    def __len__(self):
        '''
        Returns size of queue
        :return: int, size of queue
        '''
        return self.size

    def is_empty(self):
        '''
        Returns wheather queue is empty
        :return: Boolean
        '''
        return len(self) == 0

    def head_element(self):
        '''
        Returns head element of queue
        :return: head element of queue
        '''
        return self.data[self.head]

    def tail_element(self):
        '''
        Returns last element of queue
        :return: tail element of queue
        '''
        return self.data[self.tail-1]

    def enqueue(self, val):
        '''
        Adds value to the back of the queue.
        :param val: an element
        :return: None
        '''
        self.data[self.tail] = val
        self.size += 1

        if self.size == self.capacity:
            self.grow()

        #tail circles to beginning if only beginning of list is empty
        if self.tail == self.capacity -1:
            self.tail = 0
        else:
            self.tail += 1

        return None

    def dequeue(self):
        '''
        Remove and return head element if present.
        Otherwise return None. Set new head and size.
        Shrink queue's capacity if necessary.
        :return: head element/None
        '''
        if self.is_empty():
            return None

        ret_val = self.head_element()
        self.data[self.head] = None

        #if head at the end, head moves to beginning
        if self.head == self.capacity - 1:
            self.head = 0
        else:
            self.head += 1

        self.size -= 1
        if (self.size <= (self.capacity / 4)) and ((self.capacity/2) >= 4):
            self.shrink()


        return ret_val

    def tail_dequeue(self):
        '''
        Remove and return element
        from back of queue. If empty
        return None.
        :return: element removed
        '''

        if self.is_empty():
            return None

        ret_val = self.tail_element()
        self.data[self.tail-1] = None
        self.size -= 1
        self.tail -= 1

        if (self.size <= (self.capacity / 4)) and ((self.capacity//2) >= 4):
            self.shrink()

        return ret_val

    def grow(self):
        '''
        Doubles capacity of queue.
        Moves head to front of the newly allocated list.
        :return:
        '''

        new_data = []

        # appends from head to end
        i = 0
        while (self.head + i) < self.capacity:
            new_data.append(self.data[self.head+i])
            i += 1

        # if not all elements in the list
        if len(new_data) != self.size:
            a = self.tail
            while a >= 0:
                new_data.append(self.data[a])
                a -= 1

        self.head = 0
        self.tail = len(new_data) - 1
        self.capacity = self.capacity * 2

        while len(new_data) != self.capacity:
            new_data.append(None)

        self.data = new_data

    def shrink(self):
        '''
        If size is 1/4 or less of capacity, halves
        capacity. Capacity is always greater than
        or equal to 4. Moves head to the front of
        the new list.
        :return:
        '''

        new_data = []

        #appends from head to end
        i = self.head
        a = self.tail - 1
        for j in range(self.size):
            if i < self.capacity:
                new_data.append(self.data[i])
                i += 1
            else: #if tail is in front of head on list
                new_data.append(self.data[a])
                a -= 1

        self.head = 0
        self.tail = len(new_data)
        self.capacity = self.capacity//2

        while len(new_data) != self.capacity:
            new_data.append(None)

        self.data = new_data


def greatest_val(w, values):
    '''
    Find and return list of greatest
    values in an queue. Compare with values
    at a time in queue.
    :param w: size of compare array
    :param values: list of values
    :return: list of greatest values
    '''

    big_values = []
    # puts w vals in queue
    index = 0
    while index + w <= len(values):
        queue = CircularQueue() #reset queue
        for i in range(0, w):
            queue.enqueue(values[index+i])

        big_val = queue.dequeue()   #head of queue to compare

        #finds big val in queue, compares big_val with head
        while queue.is_empty() is False:
            comp_val = queue.dequeue()
            if comp_val > big_val:
                big_val = comp_val

        big_values.append(big_val)
        index += 1

    return big_values



