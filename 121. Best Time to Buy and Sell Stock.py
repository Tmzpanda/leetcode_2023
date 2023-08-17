def maxProfit(prices: List[int]) -> int:
    minPrice = float('inf')
    profit = 0
    for price in prices:
        profit = max(price - minPrice, profit)
        minPrice = min(price, minPrice)

    return profit
