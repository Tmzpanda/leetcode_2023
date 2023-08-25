def preorder(root: 'Node') -> List[int]:
    res = []
    def dfs(node):
        if node is None:
            return
        res.append(node.val)
        for node in node.children:
            dfs(node)
          
    dfs(root)
    return res
