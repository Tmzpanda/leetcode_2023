def maxProfit(prices: List[int], fee: int) -> int:
    n = len(prices)
    noShare, withShare = 0, -prices[0]
    for i in range(1, n):
        noShare = max(noShare, withShare+prices[i]-fee)
        withShare = max(withShare, noShare-prices[i])

    return noShare
