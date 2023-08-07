def kthSmallest(root, k):
    stack = []
    while root:
        stack.append(root)
        root = root.left
        
    for i in range(k):
        node = stack.pop()
        res = node

        node = node.right
        while node:
            stack.append(node)
            node = node.left
            
    return res.val
