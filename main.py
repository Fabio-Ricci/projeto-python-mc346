from fileinput import input
from classes import Graph
from methods.floydwarshall import do_floyd_warshall
from methods.tripmethods import calculate_max_incovenience, get_min_inconvenience

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
            current = int(words[2])
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
    dist = do_floyd_warshall(graph)

    print(dist)
    print(ongoing_trips)
    print(starting_trips)
    print(calculate_max_incovenience(starting_trips[0], starting_trips[2], dist))
    print(get_min_inconvenience(ongoing_trips, starting_trips, dist))

except ValueError:
    print("Error")
