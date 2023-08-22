# dfs
def minCostII(costs: List[List[int]]) -> int:
    n = len(costs)
    k = len(costs[0])
    memo = {}
    def dfs(i, prevC):
        # memo
        if (i, prevC) in memo:
            return memo[(i, prevC)]
        # base
        if i == -1:
            return 0

        res = float('inf')
        for c in range(k):
            if c == prevC:
                continue
            res = min(res, costs[i][c]+dfs(i-1, c))
        
        memo[(i, prevC)] = res
        return memo[(i, prevC)]
        
    return dfs(n-1, -1)

# dp O(n*k)
def minCostII(costs: List[List[int]]) -> int:
    n = len(costs)
    k = len(costs[0])
    
    dp = [[0] * k for _ in range(n)]
    for i in range(k):
        dp[0][i] = costs[0][i]
    
    for i in range(1, n):
        for j in range(k):
            dp[i][j] = costs[i][j] + min(dp[i-1][:j] + dp[i-1][j+1:])

    return min(dp[n-1])

# space optimization O(2*k)
def minCostII(costs: List[List[int]]) -> int:
    n = len(costs)
    k = len(costs[0])
    
    prev_dp = costs[0][:]
    for i in range(1, n):
        curr_dp = [0] * k
        for j in range(k):
            curr_dp[j] = costs[i][j] + min(prev_dp[:j] + prev_dp[j + 1:])
        prev_dp = curr_dp

    return min(prev_dp)


