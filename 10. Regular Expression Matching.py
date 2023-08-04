def isMatch(s: str, p: str) -> bool:
    memo = {}
    def dfs(i, j):
        # memo
        if (i, j) in memo:
            return memo[(i, j)]

        # p is used out
        if j == -1 and i == -1: return True
        if j == -1 and i != -1: return False
        # i is used out
        if i == -1 and p[j] != '*': return False
        if i == -1 and p[j] == '*':
            k = j
            while k != -1 and p[k] == '*':
                k -= 2
            res = (k == -1)
        # *
        elif p[j] == '*':
            res = (
                (dfs(i - 1, j) and (p[j - 1] == s[i] or p[j - 1] == '.')) or
                dfs(i, j - 2)       
            )
        # .
        elif p[j] == '.' or s[i] == p[j]:
            res = dfs(i - 1, j - 1)
        else:
            res = False
        
        memo[(i, j)] = res
        return res
    
    i, j = len(s) - 1, len(p) - 1
    return dfs(i, j)


            
            


        
