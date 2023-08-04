def isMatch(s: str, p: str) -> bool:
    memo = {}

    def dfs(i, j):
        # memo
        if (i, j) in memo:
            return memo[(i, j)]
        # p is used out
        if j == len(p) and i == len(s): return True
        if j == len(p) and i < len(s): return False
        # i is used out
        if i == len(s) and p[j] != '*': return False
        if i == len(s) and p[j] == '*':
            res = dfs(i, j + 1)
        # *
        elif p[j] == '*':
            res = dfs(i, j + 1) or dfs(i + 1, j + 1) or dfs(i + 1, j)
        # ?
        elif p[j] == '?' or p[j] == s[i]:
            res = dfs(i + 1, j + 1)
        else:
            res = False
                 
        memo[(i, j)] = res
        return res

    return dfs(0, 0)



            
