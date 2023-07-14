# O(S*n)
# dfs
def coinChange(coins, amount):
    memo = {}
    def dfs(s):
        if s == 0:
            return 0
        if s in memo:
            return memo[s]
        
        res = float('inf')
        for coin in coins:
            if coin <= s:
                res = min(res, dfs(s - coin) + 1)
        
        memo[s] = res
        return res

    res = dfs(amount)
    return res if res != float('inf') else -1
  

# dp
def coinChange(coins, amount):
    dp = [sys.maxsize for _ in range(amount + 1)]
    dp[0] = 0
    
    for s in range(1, amount + 1):
        for coin in coins:
            if coin <= s:
                dp[s] = min(dp[s], dp[s - coin] + 1)
    
    return dp[amount] if dp[amount] != sys.maxsize else -1
