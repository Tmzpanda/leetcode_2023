def lowestCommonAncestor(root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':        
    def dfs(root):
        if root is None or root in set(nodes):
            return root
        
        l = dfs(root.left)
        r = dfs(root.right)
        if l and r:
            return root
        else:
            return l or r
    
    return dfs(root)
