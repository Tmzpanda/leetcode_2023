# diag_dict
def findDiagonalOrder(nums: List[List[int]]) -> List[int]:
    diag_dict = defaultdict(list)
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            diag_dict[i+j].append(nums[i][j])

    res = []
    for diag in sorted(diag_dict.keys()):
        res.extend(diag_dict[diag][::-1])


    return res


# bfs
def findDiagonalOrder(nums: List[List[int]]) -> List[int]:
    res = []
    queue = deque([(0, 0)])
    while queue:
        i, j = queue.popleft()
        res.append(nums[i][j])
        if j == 0 and i+1 < len(nums):
            queue.append((i+1, j))
        if j+1 < len(nums[i]):
            queue.append((i, j+1))

    return res
