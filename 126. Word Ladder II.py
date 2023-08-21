def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    wordList.append(beginWord)
    n = len(wordList)
    
    pattern_dict = defaultdict(list)       
    for word in wordList:
        for i in range(len(word)):
            pattern_dict[word[:i]+'*'+word[i+1:]].append(word)

    # bfs
    graph = defaultdict(list)
    distance_dict = {}
    
    visited = set([(beginWord)])
    q = deque([(beginWord, 0)])
    while q:
        for _ in range(len(q)):
            word, distance = q.popleft()
            distance_dict[word] = distance
            for nei in [nei for i in range(len(word)) for nei in pattern_dict[word[:i]+'*'+word[i+1:]]]:
                graph[nei].append(word)
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, distance+1))

    # backtrack
    res = []
    def dfs(word, path):
        if word == beginWord:
            res.append(path[::-1])
            return
        for nei in graph[word]:
            if distance_dict[nei] == distance_dict[word]-1:   # paths of shortest length
                dfs(nei, path+[nei])

    dfs(endWord, [endWord])
    return res

