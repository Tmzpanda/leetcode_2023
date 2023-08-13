def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:  
    if root is None:
        return []
        
    res = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            for node in (node.left, node.right):
                if node:
                    queue.append(node)
        res.append(level)
        
    return res
