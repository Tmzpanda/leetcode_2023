def subsets(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    res = []
    def dfs(index, subset):
        res.append(list(subset))
        for i in range(index, n):
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
    
    dfs(0, [])
    return res
