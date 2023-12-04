def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right and root.val == targetSum:
        return True
    
    return hasPathSum(root.left, targetSum-root.val) or hasPathSum(root.right, targetSum-root.val)


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    has_path = False
    def dfs(node, current_sum):
        if not node:
            return
        current_sum += node.val
        if not node.left and not node.right and current_sum == sum:
            has_path = True
            return
        
        dfs(node.left, current_sum)
        dfs(node.right, current_sum)

    return has_path
    

