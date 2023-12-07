def isValidPalindrome(s: str, k: int) -> bool:
    return longestPalindromeSubseq(s) + k >= len(s)

# dfs
def isValidPalindrome(self, s: str, k: int) -> bool:
    memo = {}
    def dfs(i, j, k):
        if k < 0: return False
        if i >= j: return True
        if (i, j, k) in memo:
            return memo[(i, j, k)]

        if s[i] == s[j]:
            memo[(i, j, k)] = dfs(i+1, j-1, k) 
        else:
            memo[(i, j, k)] = dfs(i+1, j, k-1) or dfs(i, j-1, k-1)
        return memo[(i, j, k)]

    n = len(s)
    return dfs(0, n-1, k)
