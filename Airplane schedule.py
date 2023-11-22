"""
Ask:
a) if its possible to fly from starting airport to ending airport with timing in mind
b) path taken

Input: Starting Airport, Ending Airport, List of Flight Schedule with corresponding flying & landing time (e.g. (AirportA, 1) -> (AirportB, 4))

e.g.: can you fly from A to C with following flight schedule:
Flight 1: A,1 -> B,4
Flight 2: B,3 -> C,5
Ans: no because you cannot "go back in time". When you land at B, flight 2 has already taken off.

"""
def can_fly(start, end, flights):
    # build graph
    graph = defaultdict(list)
    for (src, start_time), (dest, end_time) in flights:
        graph[src].append((dest, start_time, end_time))

    heap = [(0, start, [])]  # (current time, current airport, path taken)
    while heap:
        current_time, current_airport, path = heapq.heappop(heap)

        if current_airport == end:
            return True, path

        for next_airport, departure_time, arrival_time in graph[current_airport]:
            if departure_time >= current_time:
                heapq.heappush(heap, (arrival_time, next_airport, path + [(current_airport, departure_time, next_airport, arrival_time)]))

    return False, []

