def getSkyline(buildings: List[List[int]]) -> List[List[int]]:
    heightChange = []
    for start, end, height in buildings:
        heightChange.append((start, height))
        heightChange.append((end, -height))
    heightChange.sort(key=lambda x: (x[0], -x[1]))

    res = []
    heap = [0]  # max_heap
    for position, delta in heightChange:
        if delta > 0:  # start
            if delta > -heap[0]:
                res.append([position, delta])
            heappush(heap, -delta)
        else:  # end
            heap.remove(delta) 
            heapify(heap)
            if -delta > -heap[0]:
                res.append([position, -maxHeap[0]])

    return res

            
