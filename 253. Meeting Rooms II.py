"""
  x----xx------------------x
  4    9 9                 29
x-------------x x------x
2            15 16     23

"""
# O(nlogn)
def minMeetingRooms(intervals: List[List[int]]) -> int:
    start = sorted([interval[0] for interval in intervals])
    end = sorted([interval[1] for interval in intervals])

    s, e = 0, 0
    count, res = 0, 0
    while s < len(intervals):    # sweep line
        if start[s] < end[e]:
            count += 1
            s += 1
        else:
            count -= 1
            e += 1
        res = max(res, count)

    return res


# another implementation
def minMeetingRooms(intervals: List[List[int]]) -> int:
    roomChange = []
    for interval in intervals:
        roomChange.append((interval[0], 1))
        roomChange.append((interval[1], -1))
    roomChange.sort()
        
    res = 0
    count = 0
    for _, delta in roomChange:
        count += delta
        res = max(res, count)
        
    return res

