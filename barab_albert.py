import numpy as np
import networkx as nx

class BAGraph:
    def __init__(self, m):
        self._m = m
        self._graph = nx.DiGraph()
        self._graph.add_nodes_from(range(m))
    @property
    def graph(self):
        return self._graph
    
    @property
    def m(self):
        return self._m
    
    @property
    def nodes(self):
        return self._graph.nodes
    
    @property
    def timearrivals(self):
        [0]*self.m + list(range(1, len(self.nodes) - self.m + 1))
    
    @m.setter
    def m(self, m):
        self._m = m
    
    def calcProbabilities(self):
        sum_degree = 2*len(self.graph.edges)
        return np.array(list(dict(self.graph.degree).values())) / sum_degree
     
    def addNode(self):
        probs = self.calcProbabilities()
        chosen_nodes = np.random.choice(list(self.graph.nodes),
                                       self._m,
                                       replace = False,
                                       p = probs)
        self.graph.add_node(len(self._graph.nodes))
        for node in chosen_nodes:
            self.graph.add_edge(node, list(self.graph.nodes)[-1])

            
    def buildGraph(self, n):
        for _ in range(n):
            self.addNode()