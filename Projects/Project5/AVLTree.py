'''
PROJECT 5 - AVL Trees
Name: Clare Kinery
'''

import random as r      # To use for testing

class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right', 'height'

    def __init__(self, value: object, parent: object = None, left: object = None, right: object = None) -> object:
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)

class AVLTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None    # The root Node of the tree
        self.size = 0       # The number of Nodes in the tree

    def __eq__(self, other):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result

    def visual(self):
        """
        Returns a visual representation of the AVL Tree in terms of levels
        :return: None
        """
        root = self.root
        if not root:
            print("Empty tree.")
            return
        bfs_queue = []
        track = {}
        bfs_queue.append((root, 0, root.parent))
        h = self.height(self.root)
        for i in range(h+1):
            track[i] = []
        while bfs_queue:
            node = bfs_queue.pop(0)
            track[node[1]].append(node)
            if node[0].left:
                bfs_queue.append((node[0].left, node[1] + 1, node[0]))
            if node[0].right:
                bfs_queue.append((node[0].right, node[1] + 1, node[0]))
        for i in range(h+1):
            print(f"Level {i}: ", end='')
            for node in track[i]:
                print(tuple([node[0], node[2]]), end=' ')
            print()

    ### Implement/Modify the functions below ###

    def insert(self, node, value):
        """
        Inserts value as a new node into tree. If value
        already exists in tree, do nothing. Rebalance if
        needed.
        :param node: root of tree
        :param value: value of node to insert
        :return:
        """
        if self.size == 0: #creates root if empty tree
            self.root = Node(value)
            self.size = 1
        elif node.value == value:
            return
        elif node.value < value:
            if node.right is None: #add value as a node to right
                node.right = Node(value, node)
                self.size += 1
            elif node.right.value != value:
                self.insert(node.right, value)
        else:
            if node.left is None: #add value as node to left
                node.left = Node(value, node)
                self.size += 1
            elif node.left.value != value:
                self.insert(node.left, value)

        #change height of node and left/right depending on node

        if node is not None:
            if self.height(node.right) > self.height(node.left):
                node.height = node.right.height + 1

            elif self.height(node.right) < self.height(node.left):
                node.height = node.left.height + 1

            #check/balance
            self.rebalance(node)

        return  #continues updating heights

    def search(self, node, value):
        """
        Searches tree beginning at given node
        for a node with given value. If node does
        not exist returns potential parent node.
        :param node: root of tree
        :param value: value to find
        :return: node with value or potential parent node
        """
        if node is None:
            return node
        elif node.value == value:
            return node
        elif value > node.value:
            if node.right is None:
                return node
            return self.search(node.right, value)
        else:
            if node.left is None:
                return node
            return self.search(node.left, value)

    def inorder(self, node):
        """
        Returns a generator object of the tree from
        given node. Generator object should be inorder.
        :param node: root node
        :return: generator object of the tree
        """
        if node is None:
            return
        yield from self.inorder(node.left)
        yield node
        yield from self.inorder(node.right)

    def preorder(self, node):
        """
        Returns a generator object of the tree from
        given node. generator object should be preorder.
        :param node: root node
        :return: generator object of the tree
        """
        if node is None:
            return
        yield node
        yield from self.preorder(node.left)
        yield from self.preorder(node.right)

    def postorder(self, node):
        """
        Returns a generator object of the tree from
        given node. generator object should be postorder.
        :param node: root node
        :return: generator object of the tree
        """
        if node is None:
            return
        yield from self.postorder(node.left)
        yield from self.postorder(node.right)
        yield node

    def depth(self, value):
        """
        Returns depth of node
        with given value
        :param value: value
        :return: depth of node with value
        """
        depth = 0
        node = self.root
        while node is not None and node.value != value:
            depth +=  1
            if node.value < value:
                node = node.right
            else:
                node = node.left

        if node is None:
            return -1
        else:
            return depth

    def height(self, node):
        """
        Returns height at node
        :param node: root node
        :return: int, height of node
        """
        if node is None:
            return -1
        return node.height

    def min(self, node):
        """
        Finds the minimum value
        in tree beginning at given node.
        :param node: root node
        :return: Minimum value of tree
        """
        if node is None:
            return node
        if node.left is None:
            return node
        return self.min(node.left)

    def max(self, node):
        """
        Finds the maximum value in
        tree beginning at given node.
        :param node: root node
        :return: maximum value of tree
        """
        if node is None:
            return node
        if node.right is None:
            return node
        return self.max(node.right)

    def get_size(self):
        """
        Gets the number of nodes in tree
        :return: int, size of tree
        """
        return self.size

    def get_balance(self, node):
        """
        Returns balance for given node.
        :param node: node
        :return: int, balance of node
        """
        left_height = -1
        if node.left is not None:
            left_height = node.left.height
        right_height = -1
        if node.right is not None:
            right_height = node.right.height
        return left_height - right_height

    def right_rotate(self, root):
        """
        Performs an right rotation
        on tree at given root
        :param root: root to be rotated
        :return: updated root node
        """
        left_right = root.left.right

        if root.parent is not None:
            if root.parent.left is root:
                root.parent.left = root.left
            elif root.parent.right is root:
                root.parent.right = root.left

            if root.left is not None:
                root.left.parent = root.parent

        else:
            self.root = root.left
            self.root.parent = None

        root.left.right = root
        root.parent = root.left

        root.left = left_right
        if left_right is not None:
            left_right.parent = root

        return root.parent

    def left_rotate(self, root):
        """
        Performs an left rotation on
        tree at given root
        :param root: root to be rotated
        :return: updated root node
        """
        right_left = root.right.left

        if root.parent is not None:
            if root.parent.right is root:
                root.parent.right = root.right

            elif root.parent.left is root:
                root.parent.left = root.right

            if root.right is not None:
                root.right.parent = root.parent

        else:
            self.root = root.right
            self.root.parent = None

        root.right.left = root
        root.parent = root.right

        root.right = right_left
        if right_left is not None:
            right_left.parent = root

        return root.parent

    def update_height(self, node):
        """
        Updates the height of given node.
        :param node: Node of tree
        :return:
        """
        left_height = -1
        if node.left is not None:
            left_height = node.left.height
        right_height = -1
        if node.right is not None:
            right_height = node.right.height
        if left_height > right_height:
            node.height = left_height + 1

        else:
            node.height = right_height + 1

    def rebalance(self, node):
        """
        Balances tree at given node
        :param node: root node of tree
        :return: Node, new root
        """
        balance = self.get_balance(node)
        if balance == 2:
            if self.get_balance(node.left) == -1:
                self.left_rotate(node.left)
                if node.left.right is not None:
                    self.update_height(node.left.right)
                if node.left is not None:
                    self.update_height(node.left.left)
                self.update_height(node.left)

                self.update_height(node)

            node = self.right_rotate(node)
        elif balance == -2:
            if self.get_balance(node.right) == 1:
                self.right_rotate(node.right)
                if node.right.right is not None:
                    self.update_height(node.right.right)
                if node.right.left is not None:
                    self.update_height(node.right.left)
                self.update_height(node.right)

                self.update_height(node)

            node = self.left_rotate(node)

        if node.right is not None:
            self.update_height(node.right)
        if node.left is not None:
            self.update_height(node.left)
        self.update_height(node)

        return node


    def remove(self, node, value):
        """
        Remove value from tree. If value doesn't
        exist in tree do nothing. If value to be
        removed has two children, replace with the maximum
        of the left subtree
        :param node: root of tree
        :param value: value of node to be removed
        :return: root of subtree
        """
        if node is None:    #empty tree
            return node
        elif node.value == value: #replace head node

            #Case 1: 2 children
            if node.left is not None and node.right is not None:
                replace_val = self.max(node.left).value
                node.value = replace_val
                self.remove(node.left, replace_val) #removes other

            #Case 2: 1 child
            elif node.right is not None:
                node.value = node.right.value
                node.right = None
                self.size -= 1

            elif node.left is not None:
                node.value = node.left.value
                node.left = None
                self.size -= 1

            #Case 3: No child
            else:
                if node.parent is None:
                    node = None
                    self.root = None
                    self.size -= 1
                    return node
                else:
                    parent = node.parent
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                self.size -= 1

        elif node.value > value: #go left
            self.remove(node.left, value)
        else: #go right
            self.remove(node.right, value)

        # change heights, check balance
        if node is not None:
            if self.height(node.right) > self.height(node.left):
                node.height = node.right.height + 1

            elif self.height(node.right) < self.height(node.left):
                node.height = node.left.height + 1

            #check/balance
            root = self.rebalance(node)

        #return node
        return root

def repair_tree(tree):
    """
    Intake tree, potentially out of order,
    and repairs tree by putting nodes back
    in order.
    :param tree: AVL tree
    :return:
    """
    order = tree.inorder(tree.root)

    #check for potential swaps
    big_node = None
    small_node = None
    pre_node = None
    pre_pre_node = None
    for i in range(tree.get_size()): #looking for 2 values to swap
        node = next(order, None)

        if pre_node is not None:

            if node.value < pre_node.value:

                if pre_pre_node.value < node.value:
                    set = pre_node
                else:
                    set = node
                if small_node is None:
                    small_node = set
                else:
                    big_node = set
        pre_pre_node = pre_node
        pre_node = node


    #swap
    if small_node is not None:
        small_val = small_node.value
        big_val = big_node.value

        small_node.value = big_val
        big_node.value = small_val






