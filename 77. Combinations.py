def combine(n: int, k: int) -> List[List[int]]:
    res = []
    def dfs(index, path):
        if len(path) == k:
            res.append(list(path))
        
        for i in range(index, n + 1):
            path.append(i)
            dfs(i+1, path) 
            path.pop()

    dfs(1, [])
    return res


def combine(n: int, k: int) -> List[List[int]]:
    res = []
    def dfs(index, k, path):
        if k == 0:
            res.append(list(path))
          
        for i in range(index, n + 1):
            path.append(i)
            dfs(i+1, k-1, path) 
            path.pop()

    dfs(1, k, [])
    return res
