import math
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

INF = math.inf 

class UndirectedGraph:
    def __init__(self):
        self._graph = nx.Graph()

    def add_node(self, node):
        self._graph.add_node(node)

    def add_edge(self, node1, node2, weight):
        self._graph.add_edge(node1, node2, weight = weight)
    
    def add_nodes(self, nodes):
        for node in nodes:
            self._graph.add_node(node)
    
    def add_edges(self, edges):
        for edge in edges:
            u, v, w = edge 
            self._graph.add_edge(u, v, weight = w)

    def get_nodes(self):
        return list(self._graph.nodes())

    def get_edges(self):
        return list(self._graph.edges())

    def get_neighbors(self, node):
        return list(self._graph.neighbors(node))

    def has_node(self, node):
        return self._graph.has_node(node)

    def has_edge(self, node1, node2):
        return self._graph.has_edge(node1, node2)

    def remove_node(self, node):
        self._graph.remove_node(node)

    def remove_edge(self, node1, node2):
        self._graph.remove_edge(node1, node2)

    def get_weight(self, node1, node2):
        return self._graph[node1][node2]["weight"]

    def __str__(self):
        return f"Nodes: {self.get_nodes()}\nEdges: {self.get_edges()}"
    
    def __len__(self):
        return len(self._graph)
    
    def __iter__(self):
        return iter(self._graph)
    
    def get_edge_distance_matrix(self):
        nodes = self.get_nodes()
        num_nodes = len(nodes)
        distance_matrix = np.zeros((num_nodes, num_nodes), dtype = float)

        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if self._graph.has_edge(nodes[i], nodes[j]):
                    distance = self._graph[nodes[i]][nodes[j]]["weight"]
                    distance_matrix[i][j] = distance
                    distance_matrix[j][i] = distance
                else:
                    distance_matrix[i][j] = INF

        return distance_matrix
    
    def plot_graph(self, filename = "images/graph_plot.png"):
        plt.title("Graph", fontsize = 20)

        pos = nx.spring_layout(self._graph)
        nx.draw(self._graph, pos = pos, with_labels = True, font_weight = "bold")

        labels = nx.get_edge_attributes(self._graph, "weight")
        nx.draw_networkx_edge_labels(self._graph, pos = pos, edge_labels = labels)

        plt.savefig(filename)
        plt.close()

    def index_to_node(self, i):
        nodes = self.get_nodes()
        return nodes[i]

    def plot_TSP_cycle(self, solver, filename = "images/tsp_cycle.png"): 
        _, index_path, node_path = solver.solve() 
        n = len(node_path)
        
        distances = self.get_edge_distance_matrix()

        cycle = UndirectedGraph()
        for i in range(n - 1):
            cycle.add_node(node_path[i])

        for i in range(n - 1):
            cycle.add_edge(node_path[i], node_path[i + 1], weight = distances[index_path[i]][index_path[i + 1]])
        
        cycle.plot_graph(filename)

    def plot_overlay_TSP(self, solver, filename = "images/overlay_tsp_cycle.png"):
        plt.title("Graph and TSP Solution", fontsize = 20)
        labels = nx.get_edge_attributes(self._graph, "weight")

        _, _index_path, node_path = solver.solve()
        n = len(node_path)

        edge_colors = set()
        for i in range(n - 1):
            edge_colors.add((node_path[i], node_path[i + 1]))

        pos = nx.spring_layout(self._graph)
        colors = ["r" if (i, j) in edge_colors or (j, i) in edge_colors else "b" for i, j in self.get_edges()]

        nx.draw(self._graph, pos = pos, edge_color = colors, with_labels = True, font_weight = "bold")
        nx.draw_networkx_edge_labels(self._graph, pos = pos, edge_labels = labels)

        plt.savefig(filename)
        plt.close()