def wordBreak(s: str, wordDict: List[str]) -> List[str]:
  
    res = []
    def dfs(s, path):
        if not s:
            res.append(" ".join(path))

        for i in range(len(s)): 
            word = s[:i+1]
            if word in wordDict:
                path.append(word)
                dfs(s[i+1:], path)
                path.pop()

    dfs(s, [])
    return res
