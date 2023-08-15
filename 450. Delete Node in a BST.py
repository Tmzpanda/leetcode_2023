def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
        return
    
    if root.val > key:
        root.left = deleteNode(root.left, key)
    elif root.val < key:
        root.right = deleteNode(root.right, key)
    else:
        # no child or one child
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        # two children
        else:
            temp = findSmallest(root.right)
            root.val = temp.val
            root.right = deleteNode(root.right, temp.val)
        
    return root

def findSmallest(root):
    while root.left:
        root = root.left
    return root
