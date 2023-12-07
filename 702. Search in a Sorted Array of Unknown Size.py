def search(reader: 'ArrayReader', target: int) -> int:
    l, r = 0, 1
    while target > reader.get(r):
        r = r * 2

    while l <= r:
        mid = (l + r) // 2
        if reader.get(mid) == target:
            return mid
        if reader.get(mid) < target:
            l = mid + 1
        else:
            r = mid - 1
            
    return -1
