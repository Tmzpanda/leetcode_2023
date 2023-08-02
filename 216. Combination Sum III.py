# O(C(9,k))
def combinationSum3(k: int, n: int) -> List[List[int]]:
    res = []
    def dfs(start, target, path):
        if target == 0 and len(path) == k:
            res.append(list(path))
            return
        if target < 0 or len(path) > k:
            return

        # backtrack
        for i in range(start, 10):
            path.append(i)
            dfs(i + 1, target - i, path)
            path.pop()
    
    dfs(1, n, [])
    return res

# another implementation
def combinationSum3(k: int, n: int) -> List[List[int]]:
    res = []
    def dfs(start, total, path):
        if total == n and len(path) == k:
            res.append(list(path))
            return
        if total > n or len(path) > k:
            return
        
        for i in range(start, 10):
            path.append(i)
            dfs(i + 1, total + i, path)
            path.pop()
    
    dfs(1, 0, [])
    return res
