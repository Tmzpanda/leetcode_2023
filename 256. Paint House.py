def minCost(costs: List[List[int]]) -> int:
    n = len(costs)
    memo = {}
    def dfs(i, prevC):
        # memo
        if (i, prevC) in memo:
            return memo[(i, prevC)]
        # base
        if i == -1:
            return 0

        res = float('inf')
        for c in range(3):
            if c == prevC:
                continue
            res = min(res, costs[i][c]+dfs(i-1, c))
        
        memo[(i, prevC)] = res
        return memo[(i, prevC)]
        
    return dfs(n-1, -1)
