def findLongestChain(intervals: List[List[int]]) -> int:
    intervals = sorted(intervals, key = lambda x: x[1])
    prevEnd = intervals[0][1]
    res = 1
    for start, end in intervals[1:]:
        if start > prevEnd:
            res += 1
            prevEnd = end
            
    return res
