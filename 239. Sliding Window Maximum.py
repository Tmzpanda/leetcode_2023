# brute force O((n-k)*k)
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    res = []
    for i in range(n - k + 1):
        res.append(max(nums[i:i+k]))

    return res

# mono-decreasing queue
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    q = deque()
    res = []

    l, r = 0, 0
    while r < len(nums):
        while q and nums[q[-1]] <= nums[r]: # mono-decreasing
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popleft()

        if r+1 >= k:
            res.append(nums[q[0]])
            l += 1
            
        r += 1

    return res

