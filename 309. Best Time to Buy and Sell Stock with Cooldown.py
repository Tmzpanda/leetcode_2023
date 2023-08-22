# dfs
def maxProfit(self, prices: List[int]) -> int:
    memo = {}
    n = len(prices)
    def dfs(i, buying):
        if (i, buying) in memo:
            return memo[(i, buying)]
        if i >= n: 
            return 0
        
        cooldown = dfs(i+1, buying)
        if buying:
            buy = dfs(i+1, not buying) - prices[i]
            memo[(i, buying)] = max(buy, cooldown)
        else:
            sell = dfs(i+2, not buying) + prices[i]
            memo[(i, buying)] = max(sell, cooldown)

        return memo[(i, buying)]

    return dfs(0, True)

# dp
def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    withShare, cooldown, noShare = -prices[0], 0, 0
    for i in range(1, n):
        withShare = max(withShare, cooldown-prices[i])
        cooldown = max(cooldown, noShare)
        noShare = max(noShare, withShare+prices[i]) 

    return noShare
  
