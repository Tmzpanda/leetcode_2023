# bfs
def numIslands(grid):
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])

    def bfs(i, j):
        queue = deque([(i, j)])
        while queue:
            i, j = queue.popleft()
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                    grid[x][y] = "0"        # visited
                    queue.append((x, y))

    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                res += 1
                grid[i][j] = "0"    
                bfs(i, j)        

    return res   


# dfs
def numIslands(grid):
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                grid[x][y] = "0"        # visited
                dfs(x, y)

    res = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                res += 1
                grid[i][j] = "0"
                dfs(i, j)        

    return res  
