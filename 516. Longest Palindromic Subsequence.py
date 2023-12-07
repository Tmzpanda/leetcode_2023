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
