def minSubArrayLen(target: int, nums: List[int]) -> int:
    n = len(nums)
    total = 0
    res = float('inf')

    start = 0
    for i in range(n):
        total += nums[i]
        while total >= target:
            res = min(res, i - start + 1)
            total -= nums[start]
            start += 1

    return res if res != float('inf') else 0


def minSubArrayLen(target: int, nums: List[int]) -> int:
    n = len(nums)
    psum = 0
    res = float('inf')

    psumq = deque([(-1, 0)])
    for i in range(n):
        psum += nums[i]
        while psumq and psum - psumq[0][1] >= target:
            res = min(res, i - psumq[0][0])
            psumq.popleft()
        psumq.append((i, psum))

    return res if res != float('inf') else 0
