def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
    psum_dict = defaultdict(int)
    psum_dict[0] = 1
    count = 0

    def dfs(node, psum):
        nonlocal count
        if not node:
            return
        
        psum += node.val
        if psum-targetSum in psum_dict:
            count += psum_dict[psum-targetSum]
            
        psum_dict[psum] += 1
        
        dfs(node.left, psum)
        dfs(node.right, psum)

        psum_dict[psum] -= 1

    dfs(root, 0)
    return count
