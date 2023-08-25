def longestIncreasingPath(matrix: List[List[int]]) -> int:
    memo = {}
    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        longest = 1
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                longest = max(longest, 1+dfs(x, y))
                
        memo[(i, j)] = longest
        return memo[(i, j)]

    m, n = len(matrix), len(matrix[0])
    res = [[1] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            res[i][j] = dfs(i, j)

    return max(map(max, res))
