class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

class NumArray:
    def __init__(self, nums: List[int]):
        def createTree(nums, l, r):
            if l > r: 
                return None
            if l == r: 
                node = Node(l, r)
                node.total = nums[l]
                return node

            mid = (l+r) // 2
            root = Node(l, r)
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid + 1, r)
            root.total = root.left.total + root.right.total

            return root
        self.root = createTree(nums, 0, len(nums)-1)
        
    def update(self, index: int, val: int) -> None:
        def updateTree(root, i, val):
            if root.start == root.end:
                root.total = val
                return val

            mid = (root.start + root.end) // 2
            if i <= mid:
                updateTree(root.left, i, val)
            else:
                updateTree(root.right, i, val)
            
            root.total = root.left.total + root.right.total
            return root.total

        return updateTree(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def queryTree(root, i, j):
            if root.start == i and root.end == j:
                return root.total
            
            mid = (root.start + root.end) // 2
            if j <= mid:
                return queryTree(root.left, i, j)
            elif i >= mid + 1:
                return queryTree(root.right, i, j)
            else:
                return queryTree(root.left, i, mid) + queryTree(root.right, mid + 1, j)

        return queryTree(self.root, left, right)
