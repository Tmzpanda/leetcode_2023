def binaryTreePaths(root: TreeNode) -> List[str]:
    res = []
    def dfs(node, path):
        if not node.left and not node.right:
            res.append(list(path))
            return

        # backtrack
        for node in (node.left, node.right):
            if node:
                path.append(str(node.val))
                dfs(node, path)
                path.pop()       
                
    dfs(root, [str(root.val)])
    return ['->'.join(path) for path in res]
