# dp
def maximalSquare(matrix: List[List[str]]) -> int:
    m , n = len(matrix), len(matrix[0])
    dp = [[1 if matrix[i][j] == '1' else 0 for j in range(0, n)] for i in range(0, m)]

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

    res = max(map(max, dp))
    return res ** 2 
  
