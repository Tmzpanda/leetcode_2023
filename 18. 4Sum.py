# O(n^3)
def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums = sorted(nums)
    n = len(nums)
    res = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:    # deduplicate
            continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            l, r = j + 1, n - 1
            while l < r: 
                s = nums[i] + nums[j] + nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:    # deduplicate
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        
    return res
