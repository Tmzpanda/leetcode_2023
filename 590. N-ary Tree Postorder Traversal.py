def postorder(root) -> List[int]:
    res = []
    def dfs(node):
        if node is None:
            return
        for child in node.children:
            dfs(child)
        res.append(node.val)

    dfs(root)
    return res
