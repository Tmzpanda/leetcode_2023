def exist(board: List[List[str]], word: str) -> bool:
    m, n = len(board), len(board[0])
    directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    
    def dfs(i, j, index):
        if index == len(word):
            return True

        for delta_i, delta_j in directions:
            x, y = i + delta_i, j + delta_j
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and (x, y) not in visited and board[x][y] == word[index]:
                visited.add((x, y))
                if dfs(x, y, index + 1):
                    return True
                visited.remove((x, y))         # backtrack
        return False

    visited = set()
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                visited.add((i, j))
                if dfs(i, j, 1):
                    return True
                
    return False
    
