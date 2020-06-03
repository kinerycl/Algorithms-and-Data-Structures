'''
PROJECT 7 - Hash Tables
Name: Clare Kinery
'''

class HashNode:
    """
    DO NOT EDIT
    """
    __slots__ = ["key", "value", "deleted"]

    def __init__(self, key, value, deleted=False):
        self.key = key
        self.value = value
        self.deleted = deleted

    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value


class HashTable:
    """
    Hash Table Class
    """
    __slots__ = ['capacity', 'size', 'table', 'collisions', 'prime_index']

    primes = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
        181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
        281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
        397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
        503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
        743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
        863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
        997)

    def __init__(self, capacity=8):
        """
        DO NOT EDIT
        Initializes hash table
        :param capacity: capacity of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

        i = 0
        while HashTable.primes[i] <= self.capacity:
            i += 1
        self.prime_index = i - 1

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        """
        DO NOT EDIT
        Represents the table as a string
        :return: string representation of the hash table
        """
        represent = ""
        bin_no = 0
        for item in self.table:
            represent += "[" + str(bin_no) + "]: " + str(item) + '\n'
            bin_no += 1
        return represent



    def __setitem__(self, key, value):
        """
        DO NOT EDIT
        Allows for the use of the set operator to insert into table
        :param key: string key to insert
        :param value: value to insert
        :return: None
        """
        return self.insert(key=key, value=value)

    def __getitem__(self, item):
        """
        DO NOT EDIT
        Allows get operator to retrieve a value from the table
        :param item: string key of item to retrieve from table
        :return: HashNode
        """
        return self.get(item)

    def __contains__(self, item):
        """
        DO NOT EDIT
        Checks whether a given key exists in the table
        :param item: string key of item to retrieve
        :return: Bool
        """
        if self.get(item) is not None:
            return True
        return False

    def _hash_1(self, key):
        """
        ---DO NOT EDIT---
        Converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)
        return hashed_value % self.capacity

    def _hash_2(self, key):
        """
        ---DO NOT EDIT---
        Converts a string x into a hash
        :param x: key to be hashed
        :return: a hashed value
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)

        prime = HashTable.primes[self.prime_index]

        hashed_value = prime - (hashed_value % prime)
        if hashed_value % 2 == 0:
            hashed_value += 1
        return hashed_value


    """ **************** Student Section Below ******************************"""

    
    def hash(self, key, inserting=False):
        """
        Uses double hashing to find the index of where
        the given key should be in the hash table. If
        inserting is true finds next available bin. If key
        already in table, return that index.
        :param key: string
        :param inserting: boolean
        :return: int, index
        """
        hash1 = self._hash_1(key)
        hash2 = self._hash_2(key)
        hash = hash1
        i = 1 #iterator to find hash

        if inserting is False:
            while self.table[hash] is not None:
                if self.table[hash].key == key: #check if in table
                    return hash
                hash = (hash1 + i * hash2) % self.capacity #update hash
                i += 1
        else:
            while self.table[hash] is not None and self.table[hash].deleted == False: #finding none or deleted position
                if self.table[hash].key == key: #check if in table
                    return hash
                hash = (hash1 + i * hash2) % self.capacity #update hash
                i += 1

        return hash

    def insert(self, key, value):
        """
        Inserts a HashNode into the hashtable with
        the given key and value. If the load factor is
        0.5, increase grow table.
        :param key: string
        :param value: int
        :return: None
        """
        index = self.hash(key)

        self.table[index] = HashNode(key, value)
        self.size += 1
        if self.size >= (self.capacity//2):
            self.grow()
        return None

    def get(self, key):
        """
        Finds and returns the HashNode with the given key.
        If it does not exist return None.
        :param key: string
        :return: HashNode or None
        """
        if key is None:
            return None
        index = self.hash(key)
        return self.table[index]

    def delete(self, key):
        """
        Deletes a HashNode from the hashtable
        if with the given key if it exists.
        :param key: string
        :return: None
        """
        del_in = self.hash(key)
        if self.table[del_in].key == key:
            self.table[del_in].key = None
            self.table[del_in].value = None
            self.table[del_in].deleted = True
            self.size -= 1


    def grow(self):
        """
        Increases the capacity of the hashtable by 2 and
        rehashes HashNodes present in hashtable.
        :return: None
        """
        dbl_capacity = self.capacity * 2

        new_hash_tbl = HashTable(capacity= dbl_capacity)

        for node in self.table:
            if node is None:
                continue
            if node.deleted == True:
                continue
            new_hash_tbl.insert(node.key, node.value)

        self.capacity = dbl_capacity
        self.table = new_hash_tbl.table
        self.size = new_hash_tbl.size
        self.prime_index = new_hash_tbl.prime_index


def word_frequency(string, lexicon, table):
    """
    Returns a hashtable of the distinct words and frequency of those words
    that the string can be split into perfectly.
    :param string: string
    :param lexicon: list
    :param table: hashtable
    :return: hashtable
    """
    for i in lexicon:
        table.insert(i,0)
    word = ""
    index = 0
    for char1 in string:
        flag = 0
        word += char1
        index += 1
        if word in lexicon:
            if index == len(string):
                table.get(word).value += 1
            next = string[index:]
            next_word =""
            old_word = word
            for i in next:
                next_word += i
                if next_word in lexicon and flag == 0:
                    table.get(word).value += 1
                    word = ""
                    flag = 1
                if old_word + next_word in lexicon and flag == 1:
                    word = old_word
                    table.get(word).value -=1
                    break
    return table
