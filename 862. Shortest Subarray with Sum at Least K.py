def shortestSubarray(self, nums: List[int], k: int) -> int:
    n = len(nums)
    psum = 0
    res = float('inf')

    psumq = deque([(-1, 0)])    # (i, psum)
    for i in range(n):
        psum += nums[i]
        while psumq and psum - psumq[0][1] >= k:
            res = min(res, i-psumq[0][0])
            psumq.popleft()
        while psumq and psum <= psumq[-1][1]:    # mono-increasing
            psumq.pop()
        psumq.append((i, psum))

    return res if res != float('inf') else -1

