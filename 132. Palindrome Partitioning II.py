def minCut(s: str) -> int:
    n = len(s)

    memo = {}
    def dfs(start):
        if start == n or isPalindrome(s[start:]):
            return 0

        if start in memo:
            return memo[start]

        minCuts = float('inf')
        for end in range(start, n):
            if isPalindrome(s[start:end+1]):
                minCuts = min(minCuts, 1+dfs(end+1))

        memo[start] = minCuts
        return minCuts

    def isPalindrome(sub):
        return sub == sub[::-1]

    return dfs(0)
