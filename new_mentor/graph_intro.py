class Graph:

    def __init__(self, graph_dict={}):
        self.graph_dict = graph_dict

    def vertices(self):
        """ return the vertices of a graph """ #doc_string
        return list(self.graph_dict.keys())

    def edges(self):
        """ return the edges of a graph """
        return self.generate_edges()
    
    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in self.graph_dict, a key "vertex"
            with an empty list as a value is added to the dictionary. Otherwise
            nothing has to be done """
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]

    def generate_edges(self):
        """ A static method generating the edges of the graph "graph".
            Edges are represented as sets with one (a loop back to the vertex)
            or two vertices
        """
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        return self.graph_dict
