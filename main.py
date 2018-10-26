class Vertex:
    def __init__(self, v):
        self.name = v
        self.adjacent = {} 

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.name

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vertices[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def add_edge(self, origin, dest, cost = 0):
        if origin not in self.vertices:
            self.add_vertex(origin)
        if dest not in self.vertices:
            self.add_vertex(dest)

        self.vertices[origin].add_neighbor(self.vertices[dest], cost)
        self.vertices[dest].add_neighbor(self.vertices[origin], cost)

    def get_vertices(self):
        return self.vertices.keys()