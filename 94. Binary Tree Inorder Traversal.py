def inorderTraversal(root: TreeNode) -> List[int]: 
    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)

    res = []    
    dfs(root) 
    return res
