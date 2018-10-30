from fileinput import input
from math import inf

class Vertex:
    def __init__(self, v):
        self.id = v
        self.adjacent = {}

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

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

    def add_edge(self, origin, dest, cost=0):
        if origin not in self.vertices:
            self.add_vertex(origin)
        if dest not in self.vertices:
            self.add_vertex(dest)

        self.vertices[origin].add_neighbor(self.vertices[dest], cost)
        self.vertices[dest].add_neighbor(self.vertices[origin], cost)

    def get_vertices(self):
        return self.vertices.keys()


try:
    graph = Graph()
    reading_trips = False
    starting_trips = []
    ongoing_trips = []
    for line in input():
        words = line.split(" ")
        if len(words) > 1 and not reading_trips:
            origin = words[0]
            dest = words[1]
            weight = words[2]
            graph.add_edge(origin, dest, weight)
        elif len(words) == 3 and reading_trips:
            origin = words[0]
            dest = words[1]
            current = words[2]
            ongoing_trips.append((origin, dest, current))
        elif len(words) == 2 and reading_trips:
            origin = words[0]
            dest = words[1]
            starting_trips.append((origin, dest))
        else:
            reading_trips = True

    #inicializa o dicionario de pesos com infinito
    #let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
    dist = {}
    for origin in graph.__iter__():
        dist[origin.get_id] = {}
        for dest in origin.get_connections:
            dist[origin.get_id][dest.get_id] = inf #origin.get_weight(dest)

    for u in dist: #each edge (u,v)
        for v in dist[u]:
            dist[u][v] = graph.get_vertex(u).get_weigth(v) #the weight of the edge (u,v)
    
    for v in range(1, len(dist)):
        dist[v][v] = 0
    
    for k in range(1, len(dist)): #1 to |V|
        for i in range(1, len(dist)):
            for j in range(1, len(dist)):
                if dist[i][j] > dist[i][k] + dist[k][j]: 
                    dist[i][j] = dist[i][k] + dist[k][j]

    print(dist)
    print(ongoing_trips)
    print(starting_trips)
except ValueError:
    print("Error")
