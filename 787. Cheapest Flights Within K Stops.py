def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    prices = [float("inf")] * n
    prices[src] = 0
    for i in range(k+1):
        tempPrices = prices.copy()

        for f, t, w in flights:    # edge list
            if prices[f] != float("inf"):
                tempPrices[t] = min(tempPrices[t], prices[f]+w)
        prices = tempPrices

    return prices[dst] if prices[dst] != float("inf") else -1 
