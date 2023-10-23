import math 
import functools
import itertools
import networkx as nx
import matplotlib.pyplot as plt

INF = math.inf 

class TSPSolver:
    def __init__(self, graph):
        self._graph = graph
        self._distances = graph.get_edge_distance_matrix()
        self._N = len(graph)

    def solve(self, start = 0, bitmask = 1 << 0):
        cost, index_path = self.__cost(start, bitmask)

        index_path.reverse()
        index_path += [index_path[0]]

        node_path = [self._graph.index_to_node(i) for i in index_path]
        return cost, index_path, node_path
    
    @functools.lru_cache(maxsize = None)
    def __cost(self, j, visited):
        if visited == ((1 << self._N) - 1):
            return self._distances[j][0], [j]
         
        res = INF 
        path = []
        for i in range(self._N):
            if visited & (1 << i) == 0:

                cost, subpath = self.__cost(i, visited | (1 << i))
                cost += self._distances[j][i]
                if cost < res:
                    res = cost
                    path = subpath + [j]

        return res, path
    
class BruteForceTSPSolver(TSPSolver):
        
    def __init__(self, graph):
        self._graph = graph
        self._distances = graph.get_edge_distance_matrix()
        self._N = len(graph)
    
    def __cost(self, ordering):
        cost = sum(self._distances[ordering[i]][ordering[(i + 1)]] for i in range(self._N - 1))
        cost += self._distances[ordering[-1]][ordering[0]]

        return cost

    def solve(self, start = 0):
        orderings = itertools.permutations(range(self._N))

        res = INF 
        index_path = []
        for ordering in orderings:
            if self.__cost(ordering) < res:
                res = self.__cost(ordering)
                index_path = list(ordering) + [ordering[0]]

        node_path = [self._graph.index_to_node(i) for i in index_path]
        return res, index_path, node_path