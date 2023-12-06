# rotate groups of four
def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n//2 + n%2):
        for j in range(n//2):
            temp = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i] = matrix[i][j]
            matrix[i][j] = temp

# transpose and reverse
def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    for i in range(n):
        matrix[i].reverse()
