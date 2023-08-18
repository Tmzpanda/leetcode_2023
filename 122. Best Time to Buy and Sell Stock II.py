def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    res = 0
    for i in range(1, n):
        if prices[i-1] < prices[i]:
            res += prices[i]-prices[i-1]
            
    return res
