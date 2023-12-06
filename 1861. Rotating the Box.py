def rotateTheBox(box: List[List[str]]) -> List[List[str]]:
    r, c = len(box), len(box[0])
    res = [['' for _ in range(r)] for _ in range(c)]

    for i in range(r):
        spot = c - 1
        for j in range(c - 1, -1, -1):
            if box[i][j] == '*':    # obstacle
                spot = j - 1
            elif box[i][j] == '#':  # figure
                box[i][j] = '.'
                box[i][spot] = '#'
                spot -= 1

    # clockwise rotate
    for i in range(r):
        for j in range(c):
            res[j][r-1-i] = box[i][j]

    return res

