def maxSubArrayLen(target: int, nums: List[int]) -> int:
    n = len(nums)
    total = 0
    res = 0

    start = 0
    for i in range(n):
        while total > target:
            total -= nums[start]
            start += 1
        total += nums[i]
        res = max(res, i - start + 1)

    return res if res != float('inf') else 0


def maxSubArrayLen(target: int, nums: List[int]) -> int:
    n = len(nums)
    total = 0
    res = 0

    psumq = deque([(-1, 0)])
    for i in range(n):
        psum += nums[i]
        while pusmq and psum - psumq[0][1] >= target:
        while total > target:
            total -= nums[start]
            start += 1
        total += nums[i]
        res = max(res, i - start + 1)

    return res if res != float('inf') else 0



# Longest Subarray with Sum at Most K
def longestSubarray(self, nums: List[int], k: int) -> int:
    n = len(nums)
    psum = 0
    res = float('inf')

    monoq = deque([(-1, 0)])    # (i, psum)
    for i in range(n):
        psum += nums[i]
        while monoq and psum - monoq[0][1] > k:
            monoq.popleft()
        while monoq and psum <= monoq[-1][1]:    
            monoq.pop()
        monoq.append((i, psum))

    return res if res != float('inf') else -1
