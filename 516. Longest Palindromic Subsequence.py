def longestPalindromeSubseq(s: str) -> int:
    return longestCommonSubsequence(s, s[::-1])

# dfs
def longestPalindromeSubseq(s: str) -> int:
    memo = {}
    def dfs(i, j):
        if i == j: return 1
        if i > j: return 0
        if (i, j) in memo:
            return memo[(i, j)]
    
        if s[i] == s[j]:
            memo[(i, j)] = dfs(i+1, j-1) + 2
        else:
            memo[(i, j)] = max(dfs(i+1, j), dfs(i, j-1))
        return memo[(i, j)]
    
    n = len(s)
    return dfs(0, n-1)

# dp

"""
s = "bbbab"
      j 
      b b b a b
  i b 1     o x
    b   1   o o
    b     1 
    a       1
    b         1  
"""
def longestPalindromeSubseq(s: str) -> int:
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i + L - 1
            if s[i] == s[j] and L == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]
