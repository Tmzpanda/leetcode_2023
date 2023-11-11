# dfs
def numDecodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0

    memo = {}
    def dfs(s):
        if s in memo:
            return memo[s]
        if not s:
            return 1

        res = 0 
        for i in (1, 2):
            if len(s[:i]) == i and isValid(s[:i]):
                res += dfs(s[i:])

        memo[s] = res
        return memo[s]

    def isValid(s):
        n = len(s)
        num = int(s)
        if (n == 1 and 1 <= num <= 9) or (n == 2 and 10 <= num <= 26):
            return True
        return False

    return dfs(s)
