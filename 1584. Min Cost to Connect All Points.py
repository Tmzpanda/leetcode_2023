def minCostConnectPoints(points: List[List[int]]) -> int:
    # build graph
    n = len(points)
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
            graph[i].append((j, dist))
            graph[j].append((i, dist))
    
    # Prim's
    res = 0
    visited = set()
    heap = [(0, 0)]  
    while heap:
        cost, i = heappop(heap)
        if i in visited:
            continue
        visited.add(i)
        res += cost
        if len(visited) == n: 
            return res
        for nei, neiCost in graph[i]:
            if nei not in visited:
                heappush(heap, (neiCost, nei))

