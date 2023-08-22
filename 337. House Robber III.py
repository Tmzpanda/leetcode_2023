def rob(root: Optional[TreeNode]) -> int:
    def dfs(root):
        if not root:
            return (0, 0)
        left = dfs(root.left)
        right = dfs(root.right)
        
        return (
            root.val+left[1]+right[1],  # withRoot
            max(left[0], left[1]) + max(right[0], right[1]) # withoutRoot
            )

    return max(dfs(root))
