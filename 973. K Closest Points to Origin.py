def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    origin = [0, 0]
    
    max_heap = []
    for x, y in points:
        distance = x**2 + y**2
        heapq.heappush(max_heap, (-distance, x, y))

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    res = []
    while max_heap:
        _, x, y = heapq.heappop(max_heap)
        res.append([x, y])

    res.reverse()
    return res
