# in-place
def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n//2 + n%2):
        for j in range(n//2):
            temp = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i] = matrix[i][j]
            matrix[i][j] = temp


# general
def rotate(matrix: List[List[int]]):
    n = len(matrix)
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[j][n-1-i] = matrix[i][j]

    return res
