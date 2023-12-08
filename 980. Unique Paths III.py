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

# bit masking dp
def uniquePathsIII(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0]) 
    mask = 0    # represent the state of each cell
    for i in range(m):
        for j in range(n): 
            if grid[i][j] == 1: 
                start_i, start_j = i, j
            if grid[i][j] == -1 or grid[i][j] == 1: 
                mask |= 1 << i*n+j  # set bit

    @cache
    def dfs(i, j, mask):
        if grid[i][j] == 2 and mask == (1<<m*n)-1:  # if all bits are set
            return 1
        
        res = 0
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n:
                k = x*n+y
                if not mask & 1<<k: # if kth bit is set
                    res += dfs(x, y, mask | 1<<k)
                
        return res
    
    
    return dfs(start_i, start_j, mask)
