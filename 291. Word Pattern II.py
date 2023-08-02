def wordPatternMatch(pattern: str, s: str) -> bool:
    def dfs(pattern, s):
        if not pattern:
            return not s

        c = pattern[0]
        if c in charToWord:
            word = charToWord[c]
            if not s.startswith(word):
                return False
            return dfs(pattern[1:], s[len(word):])
        
        # else
        for i in range(len(s)):
            word = s[:i+1]
            if word in wordToChar:
                continue

            charToWord[c] = word
            wordToChar[word] = c
            
            if dfs(pattern[1:], s[i+1:]):
                return True
            
            del charToWord[c]
            del wordToChar[word]

    charToWord = {}
    wordToChar = {}
    return dfs(pattern, s)

    
    
