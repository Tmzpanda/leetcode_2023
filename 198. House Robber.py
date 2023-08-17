def rob(nums: List[int]) -> int:
    n = len(nums)
    memo = {}
    def dfs(i):
        # memo
        if i in memo: 
            return memo[i]
        # base
        if i < 0:
            return 0

        memo[i] = max(nums[i] + dfs(i-2), dfs(i-1))
        return memo[i]

    return dfs(n-1)
