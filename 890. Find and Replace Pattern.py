def findAndReplacePattern(words: List[str], pattern: str) -> List[str]:
    def match(word):
        charToWord = {}
        wordSet = set()

        for c, w in zip(pattern, word):
            if c in charToWord and charToWord[c] != w: 
                return False
            if c not in charToWord and w in wordSet:
                return False

            charToWord[c] = w
            wordSet.add(w)

        return True

    return filter(match, words)
