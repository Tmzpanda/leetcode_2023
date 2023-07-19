"""
  x----xx------------------x
  4    9 9                 29
x-------------x x------x
2            15 16     23

start = [2, 4, 9, 16]
         ^s         
end = [9, 15, 23, 29]
       ^e
       
"""
# O(nlogn)
def minMeetingRooms(intervals: List[List[int]]) -> int:
    start = sorted([interval[0] for interval in intervals])
    end = sorted([interval[1] for interval in intervals])

    s, e = 0, 0
    count, res = 0, 0

    while s < len(intervals):  
        if start[s] < end[e]:
            count += 1
            s += 1
        else:
            count -= 1
            e += 1
        res = max(res, count)

    return res

  
