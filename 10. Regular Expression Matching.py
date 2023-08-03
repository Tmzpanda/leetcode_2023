"""
s = "aab"
p = "c*a*b"

                "c*"
              + /  \ -   
              "c"  ""    
     (i + 1, j)      (i, j+ 2)     
          

"""
def isMatch(s: str, p: str) -> bool:
    i, j = len(s) - 1, len(p) - 1
    def dfs(i, j):
        if j == -1 and i == -1: return True
        if j == -1 and i != -1: return False

        if i == -1 and p[j] != '*': return False
        if i == -1 and p[j] == '*':
            k = j
            while k != -1 and p[k] == '*':
                k -= 2
            return k == -1

        if p[j] == '.' or s[i] == p[j]:
            if dfs(i - 1, j - 1): return True

        if p[j] == '*':
            if dfs(i, j - 2): return True
            if (p[j - 1] == s[i] or p[j - 1] == '.') and dfs(i - 1, j): return True
        
        return False
      
    return dfs(i, j)

