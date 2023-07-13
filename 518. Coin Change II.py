# O(n*S)
# dfs
def change(amount: int, coins: List[int]) -> int:
    n = len(coins)
    memo = {}
    def dfs(i, s):
        if s == 0:
            return 1
        if i == n:
            return 0
        if (i, s) in memo:
            return memo[(i, s)]

        if coins[i] <= s:
            memo[(i, s)] = dfs(i, s - coins[i]) + dfs(i + 1, s)
        else:
            memo[(i, s)] = dfs(i + 1, s)
            
        return memo[(i, s)]

    return dfs(0, amount)


# dp
"""
coins = [1, 2, 5], amount = 5

    0  1  2  3  4  5  amount
coins
0   1  
1   1   
2   1              o
5   1o             x = dp[i][s] denotes #of ways to make change for amount s with coins[:i]
"""
def change(amount: int, coins: List[int]) -> int:
    n = len(coins)
    dp = [[0] * (amount + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for s in range(1, amount + 1):
            if coins[i - 1] <= s:
                dp[i][s] = dp[i][s - coins[i-1]] + dp[i-1][s]
            else:
                dp[i][s] += dp[i-1][s]

    return dp[n][amount]    # or dp[-1][-1]


# space optimization
def change(amount: int, coins: List[int]) -> int:
    dp = [0] * (amount + 1)    
    dp[0] = 1

    for coin in coins:
        for s in range(coin, amount + 1):
            dp[s] += dp[s - coin]

    return dp[amount]
