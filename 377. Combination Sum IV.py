# O(S*n)
# dfs
def combinationSum4(nums: List[int], target: int) -> int:

    memo = {}
    def dfs(s):
        if s == 0:
            return 1
        if s in memo:
            return memo[s]
            
        res = 0
        for num in nums:
            if s - num >= 0:
                res += dfs(s - num)
                
        memo[s] = res
        return res
      
    return dfs(target)

# dp 
def combinationSum4(nums: List[int], target: int) -> int:
    n = len(nums)
    dp = [0 for _ in range(target + 1)]    # dp[s] denotes #of combinations that sum up to s
    dp[0] = 1

    for s in range(1, target + 1):
        for num in nums:
            if s - num >= 0:
                dp[s] += dp[s - num]
    
    return dp[target]
