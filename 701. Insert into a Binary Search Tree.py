def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return TreeNode(val)
    
    if root.val > val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)
    
    return root


# another implementation
def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    def dfs(root):
        if not root:
            return TreeNode(val)

        if root.val > val:
            root.left = dfs(root.left)
        else:
            root.right = dfs(root.right)
            
        return root
        
    return dfs(root)
