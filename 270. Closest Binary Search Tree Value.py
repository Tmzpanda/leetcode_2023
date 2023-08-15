def closestValue(root: Optional[TreeNode], target: float) -> int:
    p1, p2 = root, root
    while root:
        if target > root.val:
            p1 = root
            root = root.right
        elif target < root.val:
            p2 = root
            root = root.left
        else:
            return root.val

    return min(p1.val, p2.val, key=lambda x: abs(x-target))
