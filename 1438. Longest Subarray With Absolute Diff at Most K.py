def longestSubarray(nums: List[int], limit: int) -> int:
    n = len(nums)
    start = 0
    maxq = deque()
    minq = deque()

    longest = 0
    for i in range(n):
        while maxq and maxq[-1] < nums[i]: # decreasing
            maxq.pop()
        maxq.append(nums[i])

        while minq and minq[-1] > nums[i]: # increasing
            minq.pop()
        minq.append(nums[i])

        while maxq[0] - minq[0] > limit:
            if maxq[0] == nums[start]: maxq.popleft()
            if minq[0] == nums[start]: minq.popleft()
            start += 1

        longest = max(longest, i-start+1)

    return longest
