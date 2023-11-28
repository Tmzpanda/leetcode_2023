class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.total = 0

class SegmentTree:
    def __init__(self, nums):
        def build(l, r):
            if l > r:
                return None
            if l == r:
                node = TreeNode(l, r)
                node.total = nums[l]
                return node
            
            root = TreeNode(l, r)
            mid = (l + r) // 2
            root.left = build(l, mid)
            root.right = build(mid+1, r)
            root.total = root.left.total + root.right.total

            return root

        self.root = build(0, len(nums)-1)

    def update(self, index, val):
        def dfs(root):
            if root.start == root.end:
                root.total = val
                return

            mid = (root.start + root.end) // 2
            if index <= mid:
                dfs(root.left)
            else:
                dfs(root.right)

            root.total = root.left.total + root.right.total

        dfs(self.root)

    def query(self, left, right):
        def dfs(root, left, right):
            if root.start == left and root.end == right:
                return root.total
            
            mid = (root.start + root.end) // 2
            if right <= mid:
                return dfs(root.left, left, right)
            elif left >= mid+1:
                return dfs(root.right, left, right)
            else:
                return dfs(root.left, left, mid) + dfs(root.right, mid+1, right)

        return dfs(self.root, left, right)

class NumArray:
    def __init__(self, nums: List[int]):
        self.tree = SegmentTree(nums)
        
    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(left, right)

