# O(n)
def maxSubArray(nums):
    res = -float('inf')
    psum = 0

    for num in nums:
        psum += num
        res = max(res, psum)

    return res
