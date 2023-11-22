"""
  x----xx------------------x
  4    9 9                 29
x-------------x x------x
2            15 16     23

"""
# O(nlogn)
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

# heap
def minMeetingRooms(intervals: List[List[int]]) -> int:
    intervals.sort()

    ends = []
    heappush(ends, intervals[0][1])
    
    for start, end in intervals[1:]:
        if start >= ends[0]:
            heappop(ends)
        
        heappush(ends, end)

    return len(ends)
