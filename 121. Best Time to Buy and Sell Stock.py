def maxProfit(prices: List[int]) -> int:
    minPrice = float('inf')
    res = 0
    for price in prices:
        res = max(res, price - minPrice)
        minPrice = min(price, minPrice)

    return res
