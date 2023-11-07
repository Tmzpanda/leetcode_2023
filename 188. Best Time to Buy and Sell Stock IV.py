# dp O(k*n)
"""
prices = [3,2,6,5,0,3] k = 2

  3 2 6 5 0 3
0 0 0 0 0 0 0 
1 0 x = max(dp[i][j - 1],
2 0         max(prices[j] - prices[x] + dp[i - 1][x - 1]), where 0 <= x < j

"""
def maxProfit(k, prices):
    if len(prices) <= 1:
        return 0
    
    n = len(prices)
    dp = [[0] * n for _ in range(k + 1)]
  
    for i in range(1, k + 1):
        profit = -sys.maxsize
        for j in range(1, n):
            profit = max(profit, -prices[j - 1] + dp[i - 1][j - 1]) # greedy
            dp[i][j] = max(dp[i][j - 1], prices[j] + profit)

    return dp[-1][-1]

# 3D dp
def maxProfit(self, k: int, prices: List[int]) -> int:
    n = len(prices)
    dp = [[[float('-inf')]*(k+1) for i in range(2)] for j in range(len(prices))]

    for i in range(len(prices)):
        dp[i][0][0] = 0
    dp[0][1][0] = -prices[0]

    for t in range(k+1):
        for i in range(1,len(prices)):
            dp[i][1][t] = max(dp[i-1][0][t]-prices[i], dp[i-1][1][t])
            dp[i][0][t] = max(dp[i-1][0][t], dp[i-1][1][t-1] + prices[i])
    
    return max(dp[n-1][0])


# dp state machine
def maxProfit(k: int, prices: List[int]) -> int:
    n = len(prices)
    buy = [-float('inf')]*(k+1)
    sell = [-float('inf')]*(k+1)

    buy[0], sell[0] = -prices[0], 0
    for i in range(1, n):
        buy[0] = max(buy[0], sell[0]-prices[i])
        for j in range(1, k+1):
            buy[j] = max(buy[j], sell[j]-prices[i])
            sell[j] = max(sell[j], buy[j-1]+prices[i])

    return max(sell)




