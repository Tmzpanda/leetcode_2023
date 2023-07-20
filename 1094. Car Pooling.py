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
    
        
