def wordPattern(pattern: str, s: str) -> bool:
    words = s.split(" ")
    if len(pattern) != len(words): 
        return False
    
    charToWord = {}
    wordSet = set()

    for c, w in zip(pattern, words):
        if c in charToWord and charToWord[c] != w: 
            return False
        if c not in charToWord and w in wordSet:
            return False

        charToWord[c] = w
        wordSet.add(w)
    
    return True
