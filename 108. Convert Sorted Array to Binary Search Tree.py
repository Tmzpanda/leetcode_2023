def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    def dfs(l, r):  
        # base
        if l > r:
            return None
            
        # d&q
        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left = dfs(l, mid - 1)
        root.right = dfs(mid + 1, r)
        
        return root

    return dfs(0, len(nums) - 1)
  
