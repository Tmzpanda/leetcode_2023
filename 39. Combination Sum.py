def combinationSum(nums: List[int], target: int) -> List[List[int]]:
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
            combination.append(nums[i])
            dfs(i, target - nums[i], combination)    # unlimited
            combination.pop()
        
    dfs(0, target, [])
    return res
