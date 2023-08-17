def minCost(costs: List[List[int]]) -> int:
    n = len(costs)
    memo = {}
    def dfs(i, prevColor):
        # memo
        if (i, prevColor) in memo:
            return memo[(i, prevColor)]
        # base
        if i == -1:
            return 0

        res = float('inf')
        for c in range(3):
            if c == prevColor:
                continue
            res = min(res, costs[i][c]+dfs(i-1, c))
        
        memo[(i, prevColor)] = res
        return memo[(i, prevColor)]
        
    return dfs(n-1, -1)
