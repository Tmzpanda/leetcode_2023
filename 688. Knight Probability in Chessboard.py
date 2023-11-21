def knightProbability(n: int, k: int, row: int, column: int) -> float:
    dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k+1)]
    dp[0][row][column] = 1
    for step in range(1, k+1):
        for x in range(n):
            for y in range(n):
                for i, j in [(x-2, y-1), (x-2, y+1), (x+2, y-1), (x+2, y+1), (x-1, y-2), (x-1, y+2), (x+1, y-2), (x+1, y+2)]:
                    if 0 <= i < n and 0 <= j < n:
                        dp[step][x][y] += dp[step-1][i][j] / 8.0

    return sum(dp[k][x][y] for x in range(n) for y in range(n))
