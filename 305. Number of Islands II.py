def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
    def union(a, b):
        a_root, b_root = find_root(a), find_root(b)
        if a_root == b_root:
            return False
        else:
            parent[a_root] = b_root
            return True

    def find_root(a):
        a_root = a
        while parent[a_root] != -1:
            a_root = parent[a_root]

        return a_root

    parent = defaultdict(lambda: -1)
    count = 0
    visited = set()
    res = []
    directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]

    for i, j in positions:
        if (i, j) not in visited:
            visited.add((i, j))
            count += 1
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if (x, y) in visited and union((i, j), (x, y)):
                    count -= 1
        res.append(count)

    return res
