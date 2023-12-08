# sweep line
def carPooling(trips: List[List[int]], capacity: int) -> bool:
    passChange = []
    for delta, start, end in trips:
        passChange.append((start, delta))
        passChange.append((end, -delta))
    passChange.sort()

    count = 0
    for _, delta in passChange:
        count += delta
        if count > capacity:
            return False

    return True
    
# heap        
def carPooling(trips: List[List[int]], capacity: int) -> bool:
    trips.sort(key=lambda x: x[1])

    heap = []
    count = 0
    for num_passengers, start, end in trips:
        while heap and start >= heap[0][0]:
            count -= heappop(heap)[1]

        count += num_passengers
        if count > capacity:
            return False
        
        heappush(heap, (end, num_passengers))

    return True
