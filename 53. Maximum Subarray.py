# O(n)
def maxSubArray(nums):
    res = -float('inf')
    total = 0
    for num in nums:
        if total < 0:
            total = 0
        total += num
        res = max(res, total)

    return res
