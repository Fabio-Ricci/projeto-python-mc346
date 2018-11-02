from functools import reduce

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
    incovenience_a = (dist[origin_a][origin_b] + dist[origin_b]
                      [dest_b] + dist[dest_b][dest_a]) / base_time_a
    incovenience_b = 1
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
    incovenience_a = 1
    incovenience_b = (dist[origin_b][origin_a] + dist[origin_a]
                      [dest_a] + dist[dest_a][dest_b]) / base_time_b
    possible_paths.append((path, max(incovenience_a, incovenience_b)))

    result = reduce((lambda a, b: a if a[1] < b[1] else b), possible_paths)

    return result
