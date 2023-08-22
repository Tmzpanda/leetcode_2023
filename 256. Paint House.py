# dfs
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

# dp O(n*3)
"""
costs = [[17,2,17],[16,16,5],[14,3,19]]

      c
      0  1  2 
house 0  0  0 
    0 
    1 o  o
    2       x = dp[i][c] denotes costs of paint the first i houses, while painting ith house with color c

"""
def minCost(costs: List[List[int]]) -> int:
    n = len(costs)
    dp = [[0] * 3 for _ in range(n)]
    dp[0][0], dp[0][1], dp[0][2] = costs[0][0], costs[0][1], costs[0][2]
    for i in range(1, n):
        dp[i][0], dp[i][1], dp[i][2] = (
            costs[i][0] + min(dp[i-1][1], dp[i-1][2]), 
            costs[i][1] + min(dp[i-1][0], dp[i-1][2]), 
            costs[i][2] + min(dp[i-1][0], dp[i-1][1])
        )

    return min(dp[n-1])

# space optimization O(2*3)
def minCost(costs: List[List[int]]) -> int:
    n = len(costs)
    prev_dp = costs[0][:]
    for i in range(1, n):
        curr_dp = [0] * 3
        curr_dp[0], curr_dp[1], curr_dp[2] = (
            costs[i][0] + min(prev_dp[1], prev_dp[2]),
            costs[i][1] + min(prev_dp[0], prev_dp[2]),
            costs[i][2] + min(prev_dp[0], prev_dp[1]))
        prev_dp = curr_dp

    return min(prev_dp)






