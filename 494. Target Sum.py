def findTargetSumWays(nums: List[int], S: int) -> int:
    n = len(nums)
    memo = {}
    def dfs(i, s):
        # memo
        if (i, s) in memo:
            return memo[(i, s)]
        # base
        if i == n:
            return 1 if s == 0 else 0

        memo[(i, s)] = dfs(i+1, s-nums[i]) + dfs(i+1, s+nums[i])
        return memo[(i, s)]

    return dfs(0, S)
