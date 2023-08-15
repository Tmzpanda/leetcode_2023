def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    # build graph
    graph = defaultdict(list)
    for f, t, w in times:
        graph[f].append((t, w))

    # dijkstra
    heap = [(0, k)] 
    visited = set()
    while heap:
        w, i = heappop(heap)
        visited.add(i)
        if len(visited) == n:
            return w
        for nei, neiWeight in graph[i]:      # directed graph
            heappush(heap, (w+neiWeight, nei)) 

    return -1
