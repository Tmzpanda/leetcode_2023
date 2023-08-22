def rob(nums: List[int]) -> int:
    n = len(nums)
    if n == 0: return 0
    if n == 1: return nums[0]

    def dfs(nums, i, memo):
        if i in memo:
            return memo[i]
        if i < 0:
            return 0

        memo[i] = max(nums[i] + dfs(nums, i-2, memo), dfs(nums, i-1, memo))
        return memo[i]

    return max(
        dfs(nums[1:], n-2, {}), 
        dfs(nums[:-1], n-2, {})
        ) 
