def maxSubArrayLen(target: int, nums: List[int]) -> int:
    n = len(nums)
    total = 0
    res = 0

    start = 0
    for i in range(n):
        total += nums[i]
        while total > target:
            total -= nums[start]
            start += 1
        res = max(res, i - start + 1)

    return res


def maxSubArrayLen(target: int, nums: List[int]) -> int:
    n = len(nums)
    total = 0
    res = 0
    
    psumq = deque([(-1, 0)])
    for i in range(n):
        psum += nums[i]
        while pusmq and psum - psumq[0][1] > target:
            psumq.popleft()
        res = max(res, i - psumq[0][0])
        psumq.append(i, psum)

    return res



# Longest Subarray with Sum at Most K (with negative values)
"""
index     -1 0  1  2   3 
            [1, 2, 3, -1]    k = 5
psum       0 1  3  6   5
psumq      0 1  3      5


"""
def longestSubarray(nums: List[int], k: int) -> int:
    n = len(nums)
    psum = 0
    res = 0
    psumq = deque([(-1, 0)])

    for i in range(n):
        psum += nums[i]

        for p_i, p_psum in psumq:    # since we can have negative numbers, we can't simply popleft, we need to check all valid subarrays
            if psum - p_psum <= k:
                res = max(res, i - p_i)
                continue

        while psumq and psum < psumq[-1][1]:     # non-decreasing
            psumq.pop()
            
        psumq.append((i, psum))

    return res






    
