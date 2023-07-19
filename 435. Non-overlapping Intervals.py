"""
Relationships between adjacent intervals:

start >= prevEnd:
x-----x 
      x---x

start < prevEnd:
①
x-----x
    x---x
②
x-----x
  x--x

"""

# O(nlogn)
def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    intervals = sorted(intervals)

    res = 0
    prevEnd = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            res += 1
            prevEnd = min(end, prevEnd)

    return res

