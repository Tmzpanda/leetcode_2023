def closestKValues(root: Optional[TreeNode], target: float, k: int) -> List[int]:
    res = deque()

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        if len(res) == k:
            if not abs(target-node.val) < abs(target-res[0]):
                return
            res.popleft()
        res.append(node.val)
        dfs(node.right)

    dfs(root) 
    return res
