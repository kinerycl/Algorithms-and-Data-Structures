'''
PROJECT 8 - Graphs
Name: Clare Kinery
'''

import random

def Generate_edges(size, connectedness):
    """
    DO NOT EDIT THIS FUNCTION
    Generates directed edges between vertices to form a DAG
    :return: A generator object that returns a tuple of the form (source ID, destination ID)
    used to construct an edge
    """

    assert connectedness <= 1
    random.seed(10)
    for i in range(size):
        for j in range(i + 1, size):
            if random.randrange(0, 100) <= connectedness * 100:
                yield f'{i} {j}'


# Custom Graph error
class GraphError(Exception): pass


class Vertex:
    """
    Class representing a Vertex in the Graph
    """
    __slots__ = ['ID', 'index', 'visited']

    def __init__(self, ID, index):
        """
        Class representing a vertex in the graph
        :param ID : Unique ID of this vertex
        :param index : Index of vertex edges in adjacency matrix
        """
        self.ID = ID
        self.index = index  # The index that this vertex is in the matrix
        self.visited = False

    def __repr__(self):
        return f"Vertex: {self.ID}"

    __str__ = __repr__

    def __eq__(self, other):
        """
        DO NOT EDIT THIS METHOD
        :param other: Vertex to compare
        :return: Bool, True if same, otherwise False
        """
        return self.ID == other.ID and self.index == other.index

    def out_degree(self, adj_matrix):
        """
        Returns the number of incoming edges from the given
        matrix
        :param adj_matrix: matrix
        :return: int
        """
        vert_lst = adj_matrix[self.index]
        count = 0

        for i in vert_lst:
            if i is not None:
                count += 1

        return count

    def in_degree(self, adj_matrix):
        """
        Returns the number of outgoing edges from the given
        matrix
        :param adj_matrix: matrix
        :return: int
        """
        count = 0
        for lst in adj_matrix:
            if self.ID in lst:
                count += 1

        return count

    def visit(self):
        """
        Returns whether or not a Vertex
        has be visited
        :return: Boolean
        """
        self.visited = True


class Graph:
    """
    Graph Class ADT
    """

    def __init__(self, iterable=None):
        """
        DO NOT EDIT THIS METHOD
        Construct a random Directed Graph
        :param size: Number of vertices
        :param: iterable: iterable containing edges to use to construct the graph.
        """
        self.id_map = {}
        self.size = 0
        self.matrix = []
        self.iterable = iterable
        self.construct_graph()
        if hasattr(iterable, 'close'):
            iterable.close()

    def __eq__(self, other):
        """
        DO NOT EDIT THIS METHOD
        Determines if 2 graphs are Identical
        :param other: Graph Object
        :return: Bool, True if Graph objects are equal
        """
        return self.id_map == other.id_map and self.matrix == other.matrix and self.size == other.size

    def get_vertex(self, ID):
        """
        Returns the vertex based on ID
        :param ID: Vertex ID
        :return: Vertex
        """
        return self.id_map[ID]

    def get_edges(self, ID):
        """
        Returns a set containing all
        edges of the vertex with given ID
        :param ID: Vertex ID
        :return: set of edges
        """
        v= []
        v.extend(self.matrix[self.get_vertex(ID).index])
        while None in v:
            v.remove(None)
        return set(v)


    def construct_graph(self):
        """
        Iterates through the iterable, constructing a
        graph
        :return: None
        """
        if self.iterable is None:
            raise GraphError
        for i in self.iterable:
            s, d = i.split()
            self.insert_edge(int(s), int(d)) #not sure if those are ints



    def insert_edge(self, source, destination):
        """
        Creates vertex object if necessary and adds to graph
        based on IDs given
        :param source: Vertex ID
        :param destination: Vertex ID
        :return: None
        """
        if source not in self.id_map:
            for lst in self.matrix:
                lst.append(None)
            svert = Vertex(source, self.size)
            self.id_map[source] = svert #add to map
            self.size += 1
            self.matrix.append([None for i in range(self.size)]) #not sure

        if destination not in self.id_map:
            for lst in self.matrix:
                lst.append(None)
            dvert = Vertex(destination, self.size)
            self.id_map[destination] = dvert #add to map
            self.size += 1
            self.matrix.append([None for i in range(self.size)]) #not sure

        sindex = self.id_map[source].index
        dindex = self.id_map[destination].index
        self.matrix[sindex][dindex] = destination

    def bfs(self, start, target, path=None):
        """
        Does a breadth search of graph for target beginning at
        start and generates a path to return.
        :param start: Vertex ID
        :param target: Vertex ID
        :param path: None
        :return: set containing the path
        """
        big_lvl = [start]
        level = [start]
        self.get_vertex(start).visited = True
        while len(level) > 0:
            next_level = []
            for u in level:
                for e in self.get_edges(u):
                    if self.get_vertex(e).visited == False:
                        self.get_vertex(e).visited = True
                        next_level.append(e)
                        big_lvl.append(e)

            level = next_level

        if target not in big_lvl:
            return []
        while big_lvl[-1] != target:
            big_lvl.pop()

        last = target
        for i in reversed(big_lvl):
            if i is last:   #skip first iter
                continue
            if last not in self.get_edges(i):
                big_lvl.remove(i)
            else:
                last = i
        return big_lvl

    def dfs(self, start, target, path=None):
        """
        Does a depth search of graph for target beginning at
        start and generates a path to return.
        :param start: Vertex ID
        :param target: Vertex ID
        :param path: list
        :return: set containing the path
        """
        if path is None:
            path = [start]
        else:
            path.append(start)

        vert_start = self.get_vertex(start)
        vert_start.visited = True

        if start is target:
            return path

        for i in self.get_edges(start):
            while path[-1] != start:
                path.pop()

            vert = self.get_vertex(i)

            if vert.visited == False:
                self.dfs(i, target, path)

                if target in path:
                    return path
        if target in path:
            return path
        else:
            return []

def find_k_away(K, iterable, start):
    """
    Creates a graph and eturns Vertex IDs
    K away from given start as a set
    :param K: int
    :param iterable: iterable
    :param start: Vertex ID
    :return: set of Vertex IDs
    """
    graph = Graph(iterable)
    try:
        graph.get_vertex(start).visited
    except KeyError:
        return set()
    if K == 0:
        return {start}
    return get_vert(K, graph, start, start)

def get_vert(K, graph, start, beg):
    """
    Recursively finds the Vertex IDs for a given
    graph K away from the strating Vertex ID
    :param K: int
    :param graph: Graph
    :param start: Vertex ID
    :param beg: Vertex ID, holds initial
    :return: set containing Vertex IDs
    """
    lst = []
    if K == 0 and start is not beg:
        graph.get_vertex(start).visited = False
        return start
    if graph.get_vertex(start) is None:
        return set()

    for i in graph.get_edges(start):

        if graph.get_vertex(i).visited == False:
            graph.get_vertex(i).visited = True
            v = get_vert(K-1, graph, i, beg)
            if isinstance(v, set):
                v = list(v)
            if isinstance(v, list):
                lst.extend(v)
            else:
                lst.append(v)
    return set(lst)
