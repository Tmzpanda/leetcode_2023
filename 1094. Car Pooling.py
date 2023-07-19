def carPooling(trips: List[List[int]], capacity: int) -> bool:
    passChange = []
    for numPass, start, end in trips:
        passChange.append([start, numPass])
        passChange.append([end, -numPass])
    passChange.sort()

    count = 0
    for _, numPass in passChange:
        count += numPass
        if count > capacity:
            return False

    return True
