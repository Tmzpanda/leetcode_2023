# backtrack O(3^(m*n)) TLE
def minimumEffortPath(heights: List[List[int]]) -> int:
    m, n = len(heights), len(heights[0])
    visited = set()

    def dfs(i, j, max_diff):
        if i == m-1 and j == n-1:
            return max_diff

        min_effort = float('inf')
        
        visited.add((i, j))
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                current_diff = abs(heights[x][y] - heights[i][j])
                new_max_diff = max(max_diff, current_diff)
                effort = dfs(x, y, new_max_diff)
                min_effort = min(min_effort, effort)
        visited.remove((i, j))

        return min_effort

    return dfs(0, 0, 0)


# heap O(m*n*log(m*n))
def minimumEffortPath(self, heights: List[List[int]]) -> int:
    
    m, n = len(heights), len(heights[0])

    heap = [(0, 0, 0)] 
    visited = set([(0, 0)])
    while heap:
        diff, i, j = heapq.heappop(heap)
        if i == m - 1 and j == n - 1:
            return diff 

        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                current_diff = abs(heights[x][y] - heights[i][j])
                max_diff = max(diff, current_diff)
                heapq.heappush(heap, (max_diff, x, y))
                visited.add((x, y))

    return 0

