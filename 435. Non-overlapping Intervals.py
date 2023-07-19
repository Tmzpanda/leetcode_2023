"""
relationships between adjacent intervals:

x-----x 
      x---x

x-----x
    x---x

x-----x
  x--x

"""

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

