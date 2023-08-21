def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordList.append(beginWord)
    n = len(wordList)
    
    pattern_dict = defaultdict(list)       
    for word in wordList:
        for i in range(len(word)):
            pattern_dict[word[:i]+'*'+word[i+1:]].append(word)

    # bfs
    visited = set([beginWord])
    q = deque([beginWord])
    res = 1
    while q:
        for _ in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return res
            for nei in [nei for i in range(len(word)) for nei in pattern_dict[word[:i]+'*'+word[i+1:]]]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        res += 1
    
    return 0




        
