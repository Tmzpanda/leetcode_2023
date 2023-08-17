# dfs
def fib(n: int) -> int:
    memo = {}
    def dfs(n):
        # memo
        if n in memo:
            return memo[n]
        # base
        if n == 0 or n == 1:
            return n

        memo[n] = dfs(n - 1) + dfs(n - 2)
        return memo[n]
    
    return dfs(n)


# dp
def fib(self, n: int) -> int:
    if n == 0 or n == 1:
        return n

    # base
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]
