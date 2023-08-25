def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    n = len(nums)
    res = []
    def dfs(index, subset):
        res.append(list(subset))  
        for i in range(index, n):
            if i != 0 and nums[i] == nums[i-1] and i != index:  # deduplicate
                continue
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
            
    dfs(0, [])
    return res
