def preorderTraversal(root: TreeNode) -> List[int]:
    def dfs(node):
        if node is None:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)

    res = []
    dfs(root)
    return res
