def pathSum(root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    res = []
    def dfs(node, target, path):
        if not node:
            return
        
        path.append(node.val)
        if not node.left and not node.right and target == node.val:
            res.append(list(path))
        dfs(node.left, target-node.val, path)
        dfs(node.right, target-node.val, path)
        path.pop()
        
    dfs(root, targetSum, [])

    return res
    
