# O(nlogn)
def merge(intervals: List[List[int]]) -> List[List[int]]:  
    intervals = sorted(intervals)

    res = [intervals[0]]
    for start, end in intervals[1:]:
        prevEnd = res[-1][1]
        if start > prevEnd:
            res.append([start, end])
        else:
            res[-1][1] = max(prevEnd, end)
        
    return res
