from fileinput import input
from math import inf
from classes import Graph

def read_input():
    graph = Graph()
    reading_trips = False
    starting_trips = []
    ongoing_trips = []
    for line in input():
        words = line.split(" ")
        if len(words) > 1 and not reading_trips:
            origin = int(words[0])
            dest = int(words[1])
            weight = float(words[2])
            graph.add_edge(origin, dest, weight)
        elif len(words) == 3 and reading_trips:
            origin = int(words[0])
            dest = int(words[1])
            current = float(words[2])
            ongoing_trips.append((origin, dest, current))
        elif len(words) == 2 and reading_trips:
            origin = int(words[0])
            dest = int(words[1])
            starting_trips.append((origin, dest))
        else:
            reading_trips = True
    return (graph, starting_trips, ongoing_trips)

try:
    (graph, starting_trips, ongoing_trips) = read_input()

    #Floyd-Warshall algorithm
    size = graph.get_num_vertices()
    dist = [[inf for x in range(size)] for y in range(size)]
    for edge in graph.get_edges():
        dist[edge.get_origin()][edge.get_dest()] = edge.get_weight()
    for i in range(size):
        dist[i][i] = 0
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    print(dist)
    print(ongoing_trips)
    print(starting_trips)
except ValueError:
    print("Error")
