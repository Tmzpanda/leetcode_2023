def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    left_height = self.maxDepth(root.left)
    right_height = self.maxDepth(root.right)

    return max(left_height, right_height) + 1 


def maxDepth(root: Optional[TreeNode]) -> int:
    max_depth = 0

    def dfs(node, depth):
        nonlocal max_depth
        if not node:
            return

        depth += 1
        max_depth = max(max_depth, depth)
        dfs(node.left, depth)
        dfs(node.right, depth)

    dfs(root, 0)
    return max_depth
