# O(n^2) O(1)
def threeSum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    n = len(nums)
    res = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:    # deduplicate
            continue

        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]]) 
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:    # deduplicate
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    
    return res


      
