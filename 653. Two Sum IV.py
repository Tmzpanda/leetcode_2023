def findTarget(root: Optional[TreeNode], k: int) -> bool:
    vals = set()
    def dfs(node):
        if not node:
            return False
        if k - node.val in vals:
            return True

        vals.add(node.val)

        return dfs(node.left) or dfs(node.right)

    return dfs(root)
