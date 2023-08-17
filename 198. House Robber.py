def rob(nums: List[int]) -> int:
    n = len(nums)
    memo = {}
    def dfs(i):
        # memo
        if i in memo: 
            return memo[i]
        # base
        if i == 0: 
            return nums[0]
        if i == 1: 
            return max(nums[0], nums[1])

        memo[i] = max(nums[i] + dfs(i-2), dfs(i-1))
        return memo[i]

    return dfs(n-1)
