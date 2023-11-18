# backtrack
def uniquePathsIII(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0]) 
    empty = 0 
    for i in range(m):
        for j in range(n): 
            if grid[i][j] == 1: 
                start_i, start_j = i, j
            elif grid[i][j] == 0: 
                empty += 1

    res = 0
    def dfs(i, j, empty):
        nonlocal res    # nonlocal
        if grid[i][j] == 2:
            if empty == -1:
                res += 1
            return
        
        grid[i][j] = -1 
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] != -1: 
                dfs(x, y, empty-1)
        grid[i][j] = 0      # backtrack
    
    dfs(start_i, start_j, empty)
    return res
