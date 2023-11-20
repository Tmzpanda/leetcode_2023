# dfs
def numDecodings(s: str) -> int:
    MOD = 10**9 + 7

    if not s or s[0] == '0':
        return 0

    memo = {}
    def dfs(s):
        if s in memo:
            return memo[s]
        if not s:
            return 1

        res = 0 
        # one char decoding
        if s[0] == '*':
            res += 9 * dfs(s[1:]) 
        elif s[0] != '0':
            res += dfs(s[1:]) 

        # two cahr decoding
        if len(s[:2]) == 2:
            if s[0] == '*':
                res += (15 if s[1] == '*' else((2 if s[1] <= '6' else 1))) * dfs(s[2:]) # 11-19 and 21-26
            elif s[0] == '1':
                res += (9 if s[1] == '*' else 1) * dfs(s[2:])
            elif s[0] == '2':
                res += (6 if s[1] == '*' else (1 if s[1] <= '6' else 0)) * dfs(s[2:])

        memo[s] = res % MOD
        return res % MOD

    return dfs(s)


# dp
def numDecodings(s: str) -> int:
    MOD = 10**9 + 7
    n = len(s)
    if not s or s[0] == '0':
        return 0
    
    # dp[i] represents the number of ways to decode the string s[:i]
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        if s[i-1] == '*':
            dp[i] = 9 * dp[i-1]
        elif s[i-1] != '0':
            dp[i] = dp[i-1]

        if i > 1:
            if s[i-2] == '*':
                dp[i] += (15 if s[i-1] == '*' else((2 if s[i-1] <= '6' else 1))) * dp[i-2]
            elif s[i-2] == '1':
                dp[i] += (9 if s[i-1] == '*' else 1) * dp[i-2]
            elif s[i-2] == '2':
                dp[i] += (6 if s[i-1] == '*' else (1 if s[i-1] <= '6' else 0)) * dp[i-2]
        
        dp[i] %= MOD

    return dp[n]
