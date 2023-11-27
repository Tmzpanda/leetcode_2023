def fallingSquares(positions: List[List[int]]) -> List[int]:
    res = []
    highest = 0
    prePositions = []
    for start, size in positions:
        start, end, height = start, start+size, size

        preHighest = 0
        for preStart, preEnd, preHeight in prePositions:
            if start >= preEnd or end <= preStart: continue
            else:
                preHighest = max(preHighest, preHeight)
                
        height += preHighest
        highest = max(highest, height)
        prePositions.append((start, end, height))
        res.append(highest)

    return res

# segment tree
def fallingSquares(self, positions: List[List[int]]) -> List[int]:
    tree = SegmentTree()
    res = []
    highest = 0
    for start, size in positions:
        start, end, height = start, start+size, size
        preHighest = tree.query(tree.root, start, end)
        height += preHighest
        tree.update(tree.root, start, end, height)

        highest = max(highest, height)
        res.append(highest)

    return res
