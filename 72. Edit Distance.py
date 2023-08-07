def minDistance(self, word1: str, word2: str) -> int:
    memo = {}
    def dfs(i, j):
        # memo
        if (i, j) in memo:
            return memo[(i, j)]
          
        # word1 is used out
        if i == len(word1) and j == len(word2): return 0
        if i == len(word1):
            memo[(i, j)] = dfs(i, j+1) + 1
            return memo[(i, j)]
        # word2 is used out
        if j == len(word2):
            memo[(i, j)] = dfs(i+1, j) + 1
            return memo[(i, j)]
          
        # ==
        if word1[i] == word2[j]:
            memo[(i, j)] = dfs(i+1, j+1)
        # !=
        else:
            memo[(i, j)] = min(
                dfs(i, j+1),    # insert
                dfs(i+1, j),    # delete
                dfs(i+1, j+1)   # replace
                ) + 1
        return memo[(i, j)]

    return dfs(0, 0)
