# dfs
def climbStairs(n: int) -> int:
    memo = {}
    def dfs(n):
        # memo
        if n in memo:
            return memo[n]
        # base
        if n == 1 or n == 2:
            return n
        
        memo[n] = dfs(n-1) + dfs(n-2)
        return memo[n]

    return dfs(n)

# dp
def climbStairs(n: int) -> int:
    if n == 1 or n == 2:
        return n

    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
