# soft
"""
[['.', 'F', 'F', 'F', '.'],   
 ['.', '.', 'F', '.', '.'],
 ['#', '.', '.', '#', '.'],
 ['.', '.', '.', '.', '.']]
=> 
[['.', '.', '.', '.', '.']
 ['.', '.', '.', 'F', '.']
 ['#', '.', 'F', '#', '.']
 ['.', 'F', 'F', '.', '.']]
  
"""
def simulate_falling(matrix):
    m, n = len(matrix), len(matrix[0])
    
    for j in range(n):
        spot = m - 1
        for i in range(m - 1, -1 ,-1):
            if matrix[i][j] == '#':
                spot = i - 1
            if matrix[i][j] == 'F':
                matrix[i][j] = '.'
                matrix[spot][j] = 'F'
                spot -= 1
                
    return matrix


# rigid
"""
[['.', 'F', 'F', 'F', '.'],   
 ['.', '.', 'F', '.', '.'],
 ['#', '.', '.', '#', '.'],
 ['.', '.', '.', '.', '.']]
=> 
[['.', '.', '.', '.', '.'],
 ['.', 'F', 'F', 'F', '.'],
 ['#', '.', 'F', '#', '.'],
 ['.', '.', '.', '.', '.']]
 
"""
def simulate_falling(matrix):
    m, n = len(matrix), len(matrix[0])
 
    min_distance = float('inf')   
    for j in range(n):
        spot = m - 1
        for i in range(m - 1, -1 ,-1):
            if matrix[i][j] == '#':
                spot = i - 1
            if matrix[i][j] == 'F':
                min_distance = min(spot-i, min_distance)

    for i in range(m-1, -1, -1):
        for j in range(n):
            if matrix[i][j] == 'F' and min_distance != 0:
                matrix[i+min_distance][j] = 'F'
                matrix[i][j] = '.'
                
    return matrix
