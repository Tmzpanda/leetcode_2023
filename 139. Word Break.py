def wordBreak(s: str, wordDict: List[str]) -> bool:
    memo = {}
    def dfs(s):
        # memo
        if s in memo:
            return memo[s]
        # base
        if not s:
            return True

        for i in range(len(s)):
            word = s[:i+1]
            if word in wordDict and dfs(s[i+1:]) == True:
                memo[s] = True
                return memo[s]
        
        memo[s] = False
        return memo[s]

    return dfs(s)
                
