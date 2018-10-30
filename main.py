from fileinput import input
from math import inf
from classes.Graph import Graph

def read_input():
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
    return (graph, starting_trips, ongoing_trips)

try:
    (graph, starting_trips, ongoing_trips) = read_input()

    # inicializa o dicionario de pesos com infinito
    # let dist be a |V| x |V| array of minimum distances initialized to (infinity)
    dist = {}
    for origin in graph.__iter__():
        dist[origin.get_id] = {}
        for dest in origin.get_connections():
            dist[origin.get_id][dest.get_id] = inf  # origin.get_weight(dest)

    for u in dist:  # each edge (u,v)
        for v in dist[u]:
            dist[u][v] = graph.get_vertex(u).get_weigth(
                v)  # the weight of the edge (u,v)

    for v in range(1, len(dist)):
        dist[v][v] = 0

    for k in range(1, len(dist)):  # 1 to |V|
        for i in range(1, len(dist)):
            for j in range(1, len(dist)):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    print(dist)
    print(ongoing_trips)
    print(starting_trips)
except ValueError:
    print("Error")
