# dp
"""
prices = [7,1,5,3,6,4]
      state    
        0    1
 i  0   0    -7
    1   o
    2        o
    3        x
    4   o    o
    5   x denotes the maximum profit that can be obtained till day i, with state 0/1 (noShare/withShare)

"""
def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    dp = [[0]*2 for _ in range(n)]
    dp[0][1] = -prices[0]
    
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        dp[i][1] = max(dp[i-1][1], (dp[i-2][0] if i > 1 else 0) - prices[i])
    
    return dp[n-1][0]


# state machine
def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    noShare, withShare, cooldown = 0, -prices[0], 0
    for i in range(1, n):
        noShare = max(noShare, withShare+prices[i]) 
        withShare = max(withShare, cooldown-prices[i])
        cooldown = max(cooldown, noShare)
        
    return noShare
  
