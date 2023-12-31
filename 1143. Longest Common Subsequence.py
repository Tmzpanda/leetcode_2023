# dfs
def longestCommonSubsequence(text1: str, text2: str) -> int:
    memo = {}
    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == len(text1) or j == len(text2): 
            return 0

        if text1[i] == text2[j]:
            memo[(i, j)] = dfs(i+1, j+1) + 1
        else:
            memo[(i, j)] = max(
                dfs(i+1, j),
                dfs(i, j+1)
            )
        return memo[(i, j)]

    return dfs(0, 0)

# dp
"""
dp[i][j] denotes length of LCS that ends at text1[:i] and text2[:j]
"""
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                
    return dp[m][n]
