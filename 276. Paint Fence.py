"""
num_ways(i) = num_ways_diff(i) + num_ways_same(i)
            = num_ways(i-1)*(k-1) + num_ways_diff(i-1)*1
            = num_ways(i-1)*(k-1) + num_ways(i-2)*(k-1)*1
            = (num_ways(i-1)+num_ways(i-2)) * (k-1)
            
"""

def numWays(n: int, k: int) -> int:
    dp = [0] * n
    dp[0], dp[1] = k, k*k

    for i in range(2, n):
        dp[i] = (k-1) * (dp[i-1]+dp[i-2])

    return dp[n-1]
