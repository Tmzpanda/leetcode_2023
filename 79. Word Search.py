def exist(board: List[List[str]], word: str) -> bool:
    def dfs(i, j, index):
        if index == len(word):
            return True
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and board[x][y] == word[index]:
                visited.add((x, y)) 
                if dfs(x, y, index + 1):
                    return True
                visited.remove((x, y))  # backtrack         
        return False

    m, n = len(board), len(board[0])
    visited = set()
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                visited.add((i, j))
                if dfs(i, j, 1):
                    return True
                visited.remove((i, j))
                
    return False
    
            
