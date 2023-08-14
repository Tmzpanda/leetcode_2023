def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    # build graph
    graph = defaultdict(list)
    for f, t, w in times:
        graph[f].append((t, w))

    # dijkstra
    heap = [(0, k)] 
    visited = set()
    while heap:
        weight, node = heappop(heap)
        visited.add(node)
        if len(visited) == n: 
            return weight
        for next_node, next_weight in graph[node]:      # directed graph
            heappush(heap, (weight+next_weight, next_node)) 

    return -1
