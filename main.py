from fileinput import input
from classes import Graph
from methods.floydwarshall import do_floyd_warshall
from methods.tripmethods import calculate_max_incovenience, get_min_inconvenience

def print_paths(trip_a, trip_b, inconvenience, starting_trips, ongoing_trips):
    if (trip_a in starting_trips):
        index_a = starting_trips.index(trip_a) + 1
    else:
        index_a = ongoing_trips.index(trip_a) + 1
    if (trip_b in starting_trips):
        index_b = starting_trips.index(trip_b) + 1
    else:
        index_b = ongoing_trips.index(trip_b) + 1
    (path, _) = inconvenience
    (a, b, c, d) = path
    print("passageiros: " + str(index_a) + " " + str(index_b) 
        + " percurso: " + str(a) + " " + str(b) + " " + str(c) + " " + str(d))

def print_path(trip, starting_trips, ongoing_trips):
    if (trip in starting_trips):
        index = starting_trips.index(trip) + 1
    else:
        index = ongoing_trips.index(trip) + 1
    (a, b) = trip
    print("passageiro: " + str(index) + " percurso: " + str(a) + " " + str(b))

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

    starting_trips_aux = starting_trips.copy()
    ongoing_trips_aux = ongoing_trips.copy()
    for trip in starting_trips_aux:
        if trip in starting_trips:
            min_inco = get_min_inconvenience(trip, ongoing_trips, starting_trips, dist)
            if (len(min_inco) == 2):
                (trip, _) = min_inco
                print_path(trip, starting_trips_aux, ongoing_trips_aux)
            else:
                (trip_a, trip_b, inconvenience) = min_inco
                print_paths(trip_a, trip_b, inconvenience, starting_trips_aux, ongoing_trips_aux)
except Exception as e: 
    print(e)