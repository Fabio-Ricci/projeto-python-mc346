from functools import reduce
from math import inf

def calculate_max_incovenience_ongoing(ongoing_trip, starting_trip, dist):
    (origin_a, dest_a, current_a) = ongoing_trip
    (origin_b, dest_b) = starting_trip

    base_time_a = dist[current_a][dest_a]
    base_time_b = dist[origin_b][dest_b]

    possible_paths = []

    # A,X,C,B,D
    path = (origin_a, current_a, origin_b, dest_a, dest_b)
    incovenience_a = (dist[current_a][origin_b] +
                      dist[origin_b][dest_a]) / base_time_a
    incovenience_b = (dist[origin_b][dest_a] +
                      dist[dest_a][dest_b]) / base_time_b
    possible_paths.append((path, max(incovenience_a, incovenience_b)))

    # A,X,C,D,B
    path = (origin_a, current_a, origin_b, dest_b, dest_a)
    incovenience_a = (dist[current_a][origin_b] +
                      dist[origin_b][dest_b] +
                      dist[dest_b][dest_a]) / base_time_a
    incovenience_b = 1.0
    possible_paths.append((path, max(incovenience_a, incovenience_b)))

    result = reduce((lambda a, b: a if a[1] < b[1] else b), possible_paths)

    return result


def calculate_max_incovenience(trip_a, trip_b, dist):
    (origin_a, dest_a) = trip_a
    (origin_b, dest_b) = trip_b

    base_time_a = dist[origin_a][dest_a]
    base_time_b = dist[origin_b][dest_b]

    possible_paths = []

    # A C B D
    path = (origin_a, origin_b, dest_a, dest_b)
    incovenience_a = (dist[origin_a][origin_b] +
                      dist[origin_b][dest_a]) / base_time_a
    incovenience_b = (dist[origin_b][dest_a] +
                      dist[dest_a][dest_b]) / base_time_b
    possible_paths.append((path, max(incovenience_a, incovenience_b)))

    # A C D B
    path = (origin_a, origin_b, dest_b, dest_a)
    incovenience_a = (dist[origin_a][origin_b] +
                      dist[origin_b][dest_b] +
                      dist[dest_b][dest_a]) / base_time_a
    incovenience_b = 1.0
    possible_paths.append((path, max(incovenience_a, incovenience_b)))

    # C A D B
    path = (origin_b, origin_a, dest_b, dest_a)
    incovenience_a = (dist[origin_a][dest_b] +
                      dist[dest_b][dest_a]) / base_time_a
    incovenience_b = (dist[origin_b][origin_a] +
                      dist[origin_a][dest_b]) / base_time_b
    possible_paths.append((path, max(incovenience_a, incovenience_b)))

    # C A B D
    path = (origin_b, origin_a, dest_a, dest_b)
    incovenience_a = 1.0
    incovenience_b = (dist[origin_b][origin_a] +
                      dist[origin_a][dest_a] +
                      dist[dest_a][dest_b]) / base_time_b
    possible_paths.append((path, max(incovenience_a, incovenience_b)))

    result = reduce((lambda a, b: a if a[1] < b[1] else b), possible_paths)

    return result

def get_min_inconvenience(trip, ongoing_trips, starting_trips, dist):
    inconveniences = [] 
    # inconvenience for starting_trips
    for i in range(len(starting_trips)):
        inconveniences.append((trip, calculate_max_incovenience(trip, starting_trips[i], dist)))
    
    # inconveniences for ongoing_trips
    for i in range(len(ongoing_trips)):
        inconveniences.append((trip, calculate_max_incovenience_ongoing(ongoing_trips[i], trip, dist)))

    min_inconvenience = inf
    for i in range(len(inconveniences)):
        (_, inco) = inconveniences[i]
        if inco == 1.0:
            inconvenience_1 = inconveniences[i]
        elif inco < min_inconvenience:
            inconvenience = inconveniences[i]
            min_inconvenience = inco

    if min_inconvenience > 1.4:
        return inconvenience_1

    return inconvenience