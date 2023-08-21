def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordList.append(beginWord)
    n, m = len(wordList), len(beginWord)
    
    # build graph
    graph = defaultdict(list)       
    for word in wordList:
        for j in range(m):
            pattern = word[:j]+'*'+word[j+1:]
            graph[pattern].append(word)

    # bfs
    visited = set([beginWord])
    q = deque([beginWord])
    res = 1
    while q:
        for _ in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return res
            for j in range(m):
                pattern = word[:j]+'*'+word[j+1:]
                for nei in graph[pattern]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
        res += 1
    
    return 0








        
