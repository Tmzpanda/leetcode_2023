def shortestSubarray(self, nums: List[int], k: int) -> int:
    n = len(nums)
    psum = 0
    res = float('inf')

    monoq = deque([(-1, 0)])    # (i, psum)
    for i in range(n):
        psum += nums[i]
        while monoq and psum - monoq[0][1] >= k:
            res = min(res, i-monoq[0][0])
            monoq.popleft()
        while monoq and psum <= monoq[-1][1]:   
            monoq.pop()
        monoq.append((i, psum))

    return res if res != float('inf') else -1
    
