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
def longestSubarray(self, nums: List[int], k: int) -> int:






    
