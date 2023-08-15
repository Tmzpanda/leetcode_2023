class BSTIterator:
  def __init__(self, root: Optional[TreeNode]):
      self.stack = []
      while root:
          self.stack.append(root)
          root = root.left
        
  def hasNext(self) -> bool:
      return len(self.stack) > 0

  def next(self) -> int:
      node = self.stack.pop()
      res = node
  
      node = node.right
      while node:
          self.stack.append(node)
          node = node.left
  
      return res.val
      
