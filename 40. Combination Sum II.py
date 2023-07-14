# O(2^n)
def combinationSum2(nums: List[int], target: int) -> List[List[int]]:
    nums = sorted(nums)
    n = len(nums)
    res = []
    def dfs(start, target, combination):
        if target == 0:
            res.append(list(combination)) 
            return
        if target < 0:
            return 

        # backtrack
        for i in range(start, n):
            if i > 0 and nums[i] == nums[i - 1] and i != start:    # deduplicate
                continue
            combination.append(nums[i])
            dfs(i + 1, target - nums[i], combination)    # used once
            combination.pop()
        
    dfs(0, target, [])
    return res
        
