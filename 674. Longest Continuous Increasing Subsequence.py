# greedy
def findLengthOfLCIS(nums: List[int]) -> int:
    res = 1
    flag = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]: 
            flag = i
        res = max(res, i - flag + 1)
        
    return res
