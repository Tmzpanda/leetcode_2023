def wordPatternMatch(pattern: str, s: str) -> bool:
    def dfs(pattern, s):
        if not pattern: 
            return not s

        c = pattern[0]
        if c not in charToWord:
            for i in range(len(s)):
                word = s[:i+1]
                if word in wordSet: continue
                # backtrack
                charToWord[c] = word
                wordSet.add(word)
                if dfs(pattern[1:], s[i+1:]): return True
                del charToWord[c]
                wordSet.remove(word)
        else:
            word = charToWord[c]
            if not s.startswith(word): return False
            return dfs(pattern[1:], s[len(word):])

    charToWord = {}
    wordSet = set()
    return dfs(pattern, s)

