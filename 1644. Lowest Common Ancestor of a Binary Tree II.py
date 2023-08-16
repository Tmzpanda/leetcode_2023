def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def dfs(root, p, q):
        if root is None or root == p or root == q:
            return root

        l = dfs(root.left, p, q)
        r = dfs(root.right, p, q)
        if l and r:
            return root
        else:
            return l or r

    lca = dfs(root, p, q)
    if lca is None: 
        return None
    elif (lca == p and dfs(root, q, q) is None) or (lca == q and dfs(root, p, p) is None): 
        return None
    else: 
        return lca
