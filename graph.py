# a simple graph that will allow us to impliment a graph data structure

import heapq


class SimpleGraph(object):

    def __init__(self, edges=None):
        self.dict_graph = {}

    def nodes(self):
        '''return a iterator through of all nodes in the graph'''
        return self.dict_graph.iterkeys()

    def edges(self):
        '''return a list of all edges in the graph'''
        edges = []
        for key, value in self.dict_graph.iteritems():
            for item in value:
                edges.append((key, item))
        return edges

    def add_node(self, n):
        '''adds a new node 'n' to the graph'''
        self.dict_graph.setdefault(n, {})

    def add_edge(self, n1, n2, weight=0):
        '''adds a new edge to the graph connecting 'n1' and 'n2',
        if either n1 or n2 are not already present in the graph,
        they should be added.'''
        self.dict_graph.setdefault(n2, {})
        if n1 in self.dict_graph:
            self.dict_graph[n1][n2] = weight
        else:
            self.dict_graph[n1] = {n2: weight}

    def cost(self, n1, n2):
        '''Return the cost to go from source to target directly.'''
        return self.dict_graph[n1][n2]
