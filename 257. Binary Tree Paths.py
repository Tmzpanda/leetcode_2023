def binaryTreePaths(root: TreeNode) -> List[str]:
    res = []
    def dfs(node, path):
        if not node:
            return 
        if not node.left and not node.right:
            res.append(list(path + [str(node.val)]))
            return

        dfs(node.left, path + [str(node.val)])
        dfs(node.right, path + [str(node.val)])
        
    dfs(root, [])

    return ['->'.join(path) for path in res]
