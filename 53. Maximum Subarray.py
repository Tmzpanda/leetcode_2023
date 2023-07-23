# O(n)
def maxSubArray(nums):
    res = -float('inf')
    psum = 0
    for num in nums:
        if psum < 0:
            psum = 0
        psum += num
        res = max(res, psum)

    return res
