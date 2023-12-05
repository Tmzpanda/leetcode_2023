def maxPathSum(root: Optional[TreeNode]) -> int:
    res = float('-inf')

    def dfs(root):
        nonlocal res
        if not root:
            return 0
        
        leftMax = dfs(root.left)
        rightMax = dfs(root.right)
        res = max(res, root.val + leftMax + rightMax)  

        return max(root.val + max(leftMax, rightMax), 0)  # at most once

    dfs(root)
    return res
