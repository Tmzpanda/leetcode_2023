# O(nlogn)
def canAttendMeetings(intervals: List[List[int]]) -> bool:
    intervals = sorted(intervals)

    prevEnd = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            return False

    return True
